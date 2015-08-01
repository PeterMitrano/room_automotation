import sys
from sys import byteorder
from array import array
from struct import pack
import time
import os
import pyaudio
import wave
import parseSTT

THREASHOLD = 2750
LOUD_COUNT=0
CHUNK_SIZE = 1600
FORMAT = pyaudio.paInt16
RATE = 16000

def record(duration):
	p = pyaudio.PyAudio()
	stream = p.open(format=FORMAT, channels=1, rate=RATE,
		input=True, output=True,
		frames_per_buffer=CHUNK_SIZE)

	num_silent = 0
	snd_started = False

	r = array('h')
	silent=True
	start = time.time()   
	LOUD_COUNT=0
	print 'recording'
	while True:
		# little endian, signed short
		snd_data = array('h', stream.read(CHUNK_SIZE))
#		print max(snd_data)
		if byteorder == 'big':
			snd_data.byteswap()
		r.extend(snd_data)
		num_silent += 1
		if max(snd_data)>THREASHOLD:
			silent=False
		if (time.time()-start>=duration):
			break
	print 'stopped'
	sample_width = p.get_sample_size(FORMAT)
	stream.stop_stream()
	stream.close()
	p.terminate()

	return silent, sample_width, r

def rec(queue):
	while True:
		#eventually record length wont matter
		silent, sample_width, data = record(5)
		data = pack('<' + ('h'*len(data)), *data)
		wf = wave.open('/home/pi/Room/stt.wav', 'wb')
		wf.setnchannels(1)
		wf.setsampwidth(sample_width)
		wf.setframerate(RATE)
		wf.writeframes(data)
		wf.close()
		#maybe also do this async
		if not silent:
			translations = parseSTT.parse()
			queue.put(translations)
			#indicate this came from mic
			queue.put("rec")

def testRec():
	silent, sample_width, data = record(5)
	data = pack('<' + ('h'*len(data)), *data)
	wf = wave.open('/home/pi/Room/stt.wav', 'wb')
	wf.setnchannels(1)
	wf.setsampwidth(sample_width)
	wf.setframerate(RATE)
	wf.writeframes(data)
	wf.close()
	print 'parse',parseSTT.parse()

if __name__ == '__main__':
	testRec()
