#!/usr/bin/env python

import codecs

def rot13(text, decode=True):
	"""
	By default rot13 will return a decoded rot13 message. If you wish to encode a message pass
	a second argument to the rot13, for example rot13("This is text I want encoded", decode=False)
	"""

	if decode:
		try:
			return codecs.decode(text, 'rot13')
		except:
			print "Error decoding text"
	else:
		try:
			return codecs.encode(text, 'rot13')
		except: 
			print "Error encoding text"



if __name__ == '__main__':
	encrypted_text = "Zntargvp sebz bhgfvqr arne pbeare"
	decoded_text = rot13(encrypted_text)
	bullshit = "bullshit"
	print decoded_text
	print rot13(decoded_text, decode=False)

	# Tests
	assert (rot13(decoded_text, decode=False) == encrypted_text)
	assert (rot13(encrypted_text) == decoded_text)
	

