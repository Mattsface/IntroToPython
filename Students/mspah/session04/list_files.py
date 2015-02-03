#!/usr/bin/env python

import pathlib

def main():
 	
 	pth = pathlib.Path('./')

 	for f in pth.iterdir():
             print f.resolve()


if __name__ == "__main__":
	main()
