#!/usr/bin/env python

import os
import config

def find_pe_file(project):
	res_1 = os.popen('find ./ -name "*.dll"').read()
	res_2 = os.popen('find ./ -name "*.exe"').read()
	res = res_1 + res_2
	res = [ x.replace('.//','') for x in res.split('\n') if x]
	print res
	return res


