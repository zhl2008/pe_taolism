#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import sys
import json
import config
from function import *
import time

reload(sys)
sys.setdefaultencoding('utf-8')


def main_handle(my_dir):
	count = 1
	func_dir = config.runtime_path  + my_dir + '/tmp/func'
	os.chdir(func_dir)

	# loop to read the function entries
	while True:

		while not os.path.isfile(str(count)) or not os.path.isfile(str(count) + '_pcode'):
			print '[*] waiting for entry %d...' % count
			time.sleep(2)

		handle_func(count)

		count += 1



def handle_func(func_id):
	regex_file = os.getcwd() + '/../regex/' + str(func_id)
	# if the regex file already exists, then skip this function id
	if os.path.isfile(regex_file):
		print '[*] skip id %d' % func_id
		return

	pcode_file = str(func_id) + '_pcode'
	func_info = json.loads(open(str(func_id)).read())
	pcode = open(pcode_file).readlines()
	str_regex(pcode,func_info)


def gen_html(tmp_info):
	func_info = tmp_info['func_info']
	color = ['#96de78','#efef70','#7ccdec']
	human = ['haozi','craso','cm']
	tmp = '''<div class="panel-heading" style="background-color:%s">
        	<h3 class="panel-title">ID(%s) : %s</h3>
			</div>
			<div class="panel-body">
			''' % (color[func_info['id']%3],human[func_info['id']%3],str(func_info['id']))

	for i in range(len(tmp_info['regex_info'])):
		match = tmp_info['regex_info'][i]
		print match

		# real pcode path


		tmp += '''<div>
					<p>字符串：'''+ match['content'] +'''</p><a data-toggle="collapse" data-parent="#accordion" href="#collapse'''+str(func_info['id']) + '_' + str(i)+'''" aria-expanded="false" class="collapsed">查看详情</a>
					<button class="btn" data-clipboard-text="%s	%s	%s	%s''' %(str(func_info['id']),func_info['file_path'],func_info['start'],func_info['end'])
		tmp += '''">
				复制结果
			</button>
			<div id="collapse'''+str(func_info['id']) + '_' + str(i)+'''" class="panel-collapse collapse" aria-expanded="false" style="height: 0px;">
				<div class="alert alert-info">文件路径 : <a href="http://%s/f.php?f=%s" target="_blank" >%s</a>''' %( config.ip_addr,os.getcwd().replace(config.main_path,'') + '/' + str(func_info['id']) + '_pcode' ,func_info['file_path'])
		tmp +='''<br>
					匹配规则 : ''' + config.regex_rules[match['rule']]
		tmp +='''<br>
					匹配行数 : ''' + str(match['line'])
		tmp +='''<br>
					函数名 : ''' + 'sub_' + func_info['start'] + '_' + func_info['end']
		tmp +='''<br>
				匹配内容 : ''' + match['content'] + '''<br>
			</div>
		</div>
	</div>'''
	return tmp + '</div>'
	
	


def str_regex(pcode,func_info):
	regex_rules = config.regex_rules
	res = [0 for i in regex_rules]
	# to test wether the rules have been hit
	flag = 0
	tmp_info = {}
	tmp_info['func_info'] = func_info
	tmp_info['regex_info'] = []
	for j in range(len(regex_rules)):
		for i in range(len(pcode)):
			r = re.search(regex_rules[j],pcode[i],re.IGNORECASE)
			if r:
				
				tmp = ""
				tmp += "#"*15 +"\n"
				tmp +=  str(regex_rules[j]) +"\n"
				tmp += "#"*15 +"\n"
				print func_info
				tmp += func_info['file_path'] + "\n"
				tmp += "#"*15 + "\n"
				tmp += str(i) + "\n"
				tmp += "#"*15 + "\n"
				tmp += "sub_" + func_info['start'] + '_' + func_info['end'] + "\n"
				tmp += "#"*15 + "\n"
				tmp += pcode[i] + "\n"
				tmp +=  "#"*15 + "\n\n"
				print(tmp)
				open(config.log_file,'a').write(tmp)
				res[j] += 1
				flag = 1
				tmp_info['regex_info'].append({"rule":j,"line":i,"content":pcode[i]})

				
	if flag:
		print res
		tmp = [str(x) for x in res]

		regex_dir = os.getcwd() + '/../regex/'
		if not os.path.isfile(regex_dir):
			os.system('mkdir -p ' + regex_dir)
		# record the regex result and the regex log at the same time
		open(regex_dir + str(func_info['id']),'w').write(json.dumps(tmp_info))
		record_info = str(func_info['id']) + ',' + func_info['file_path'] + ',' +func_info['start'] + ',' + func_info['end'] + ',' + ','.join(tmp) 
		open(config.regex_log_file,'a').write(record_info + "\n")

		open(config.html_log_file,'a').write(gen_html(tmp_info))

	return res



if __name__ == '__main__':
	os.chdir(config.runtime_path)
	my_dirs = os.listdir('./')
	# if the file content of html log is empty, then write the html header
	if not os.path.isfile(config.html_log_file) or open(config.html_log_file,'r').read().strip() == '':
		open(config.html_log_file,'w').write(config.html_headers)
	for my_dir in my_dirs:
		if my_dir[:2] == 'p_':
			main_handle(my_dir)