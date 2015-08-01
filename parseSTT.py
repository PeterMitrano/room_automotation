import subprocess as sub
import json
import httplib

def post():
	print "posting..."
	with open("stt.wav", "r+") as f:
		audio=f.read()
	url = "www.google.com"
	path = "/speech-api/v2/recognize?lang=en-us&key=AIzaSyAzliO_woZ24h2dbJjLYYv9msUM7-ls_ns"
	headers = { "Content-type": "audio/l16; rate=16000" };
	conn = httplib.HTTPSConnection(url)
	conn.request("POST", path, audio, headers)
	response = conn.getresponse()
	data = response.read()
	split=data.split("\n")
	print "posted"
	return json.loads(split[len(split)-2])

def parse():
	translations=[]
	data=post()
	if len(data['result'])>0:
		alt = data['result'][0]['alternative']
		for item in alt:
			trans=item['transcript']
			if (len(trans)>1):
				translations.append(trans)
	return translations

if __name__ == '__main__':
	parse()
