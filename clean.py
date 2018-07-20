#!/usr/bin/env python

import os
import config


# clean log.txt
os.system('rm ' + config.log_file)

# clean regex_log.txt
os.system('rm ' + config.regex_log_file)

# clean out.html
os.system('rm ' + config.html_log_file)

# clean everything in project file
for my_dir in os.listdir(config.runtime_path):
    if os.path.isdir(config.runtime_path + my_dir):
        now_dirs = os.listdir(config.runtime_path + my_dir)
        if 'tmp' in now_dirs:
            os.system('rm -r ' + config.runtime_path + my_dir + '/tmp')
    
