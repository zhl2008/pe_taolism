#!/usr/bin/env python

import os
import config
from function import *

def ida_handle(pe_file):
	print 'start handling %s...' % pe_file
	os.system('ida -c -A -S%s/main.py %s/%s' % (config.main_path, config.runtime_path, pe_file))
	os.system('find ./ -name  "*.id*"   -delete ')
	os.system('find ./ -name  "*.nam"   -delete ')
	os.system('find ./ -name  "*.til"   -delete ')
	print 'end...'

if __name__ == '__main__':
	os.chdir(config.runtime_path)
	my_dirs = os.listdir('./')
	for my_dir in my_dirs:
		if my_dir[:2] == 'p_':
			pe_files = find_pe_file(my_dir)
			for pe_file in pe_files:
				ida_handle(pe_file)
	


