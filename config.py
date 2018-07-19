#!/usr/bin/env python

runtime_path = '/Users/haozigege/Desktop/ctf/softsec/pe_taolism/runtime_test/'
main_path = '/Users/haozigege/Desktop/ctf/softsec/pe_taolism/'


log_file = '/Users/haozigege/Desktop/ctf/softsec/pe_taolism/log.txt'

regex_log_file = '/Users/haozigege/Desktop/ctf/softsec/pe_taolism/regex_log.txt'

html_log_file = '/Users/haozigege/Desktop/ctf/softsec/pe_taolism/out.html'

# str regex rules
str_rules = [r"(\\\\|/)(etc|usr|var|proc|dev|home|root|Program Files|Windows|Microsoft)",
r"(\.bash_history|\.bashrc|\.bash_profile|\.ssh|authorized_keys|rc\.d|cron\.d|\.conf|passwd|\.bat|\.ocx)",
r"\\temp",
r"(( |\"|\'|\/|;)(wget|curl|mail)( |\"|\'))|HTTP/1\.[1|0]",
r"((([0-9]{1,3}\.){3}[0-9]{1,3})|(htons\((\d{2,5}|0x[0-9a-fA-F]{2,4}u?)\)))",
r"((((?:_POST|_GET|_REQUEST|GLOBALS)\[(?:.*?)\]\(\$(?:_POST|_GET|_REQUEST|GLOBALS)))|(((?:exec|base64_decode|edoced_46esab|eval|eval_r|system|proc_open|popen|curl_exec|curl_multi_exec|parse_ini_file|show_source|assert)\s*?\(\$(?:_POST|_GET|_REQUEST|GLOBALS)))|(((?:eval|eval_r|execute|ExecuteGlobal)\s*?\(?request))|((write|exec)\(request\.getParameter)|(((?:eval|eval_r|execute|ExecuteGlobal).*?request))|(SaveAs\(\s*?Server\.MapPath\(\s*?Request))",
r"(disable_dynamic|AddType|x-httpd-php)",
r"(( |\"|\'|\/|\.|;|\|)(chmod|chown|bash|cat|export|useradd)( |\"|\'))",
r"(\{((0x)?[0-9a-fA-F]{1,3},(\s)*){3}((0x)?[0-9a-fA-]{1,3})(\s)*\})",
r"((\\x[0-9a-fA-F]{2}){3})|(\{((0x)?[0-9a-fA-F]{1,3},(\s)*){4,}((0x)?[0-9a-fA-]{1,3})(\s)*\})|(#define(\s)*_[0-9a-fA-F]{32})",
r"(( |\"|\'|\/)evil|( |\"|\'|\/|@)eval|shellcode|\* \* \*|( |\"|\'|\/)grep)"
]

# function regex rules
func_rules = [r"(fopen|fread|fgetc|fgets|CopyFileA)\(.*\)",
r"(fwrite|fputc|fputs|fprintf|fscanf|sprintf|CopyFileA)\(.*\)",
r"(tcgetattr)\(.*\)",
r"(SOCKET|socket|htons|inet_addr|bind|connect|send|recv|listen|accept|InternetConnectA|InternetOpenA|HttpOpenRequestA|HttpSendRequestA|gethostbyname)\(.*\)",
r"(popen|execve|system|exec|execl|execv|execlp|execle|execvp)\(.*\)",
r"(ftruncate|chmod|ioctl|rename|putenv)\(.*\)",
r"(GetEnvironmentVariableA|getenv|GetCurrentDirectoryA|ptrace|opendir|RegOpenKeyExA|RegQueryValueExW|RegSetValueExA|get_nprocs|lstat|getpwent|getuid|getcwd)\(.*\)"]


regex_rules = str_rules + func_rules

html_headers = '''
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Read Text</title>
	<link href="./css/bootstrap.min.css" rel="stylesheet">
	<script src="./js/jquery.min.js"></script>
	<script src="./js/bootstrap.min.js"></script>
	<script src="./js/clipboard.min.js"></script>
	
</head>
<body>
	<script type="text/javascript">
		var clipboard = new ClipboardJS('.btn');
		clipboard.on('success', function(e) {
			console.log(e);
		});
		clipboard.on('error', function(e) {
			console.log(e);
		});
	</script>
	<div class="panel panel-info">

'''




