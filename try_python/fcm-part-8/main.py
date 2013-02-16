#!/usr/bin/env python

from mutagen.mp3 import MP3
import os
from os.path import join,getsize,exists
import sys
import apsw

def MakeDataBase():
	pass
def S2HMS(t):
	pass
def WalkThePath(musicpath):
	pass
def main():
	pass
def usage():
	message = (
		'=====================================================\n'
		'mCat - Finds all *.mp3 files in a given folder (and sub-folders), \n'
		'\tread the ID3 tags, and write that information to a SQLite database. \n\n'
		'\t{0} <foldername>\n'
		'\t WHERE <foldername>\n'
		'Author: Greg Walters\n'
		'For Full Circle Magazine\n'
		'=====================================================\n'
		).format(sys.argv[0])
	error(message)
	sys.exit(1)


if __name__=='__main__':
	main()
