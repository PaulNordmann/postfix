import os, sys;

configfile = "/etc/postfix/main.cf";
def virtualAliasMaps( path ):
	for l in open(path, 'r'):
		e = l.split(' ');
		if (len(e) != 2): continue;
		e[0] = e[0].strip();
		e[1] = e[1].strip();
		print e[0] + ' -> ' + e[1];

for line in open(configfile, 'r'):
	line = line.rstrip();
	if (line.startswith('#')): continue;
	t = line.split('=');
	if (len(t) != 2): continue;
	t[0] = t[0].strip();
	t[1] = t[1].strip();
	if (t[0] == 'virtual_alias_maps'):
		virtualAliasMaps(t[1][5:] if t[1].startswith('hash:') else t[1])
		break;
