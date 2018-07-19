#!/usr/bin/env python

import re
import os
import sys
import json
import config
from function import *
import time



def main_handle(my_dir):
	count = 1
	func_dir = config.runtime_path  + my_dir + '/tmp/func'
	os.chdir(func_dir)

	# loop to read the function entries
	while True:

		while not os.path.isfile(str(count)):
			print '[*] waiting for entry %d...' % count
			time.sleep(2)

		handle_func(count)

		count += 1




def handle_func(func_id):
	pcode_file = str(func_id) + '_pcode'
	print json.loads(str(func_id))
	pcode = open(pcode_file).readlines()





if __name__ == '__main__':
	os.chdir(config.runtime_path)
	my_dirs = os.listdir('./')
	for my_dir in my_dirs:
		if my_dir[:2] == 'p_':
			main_handle(my_dir)