import os, sys;

testMailPath = 'testmails.conf';

if (not os.path.isfile(testMailPath)):
	print 'Error:\t no testmails found!';
	print 'exec:\t make addTestMail';
	sys.exit(1);

print'echo start tests'

for line in open(testMailPath, 'r'):
	line = line.rstrip();
	print '\t' + line;
	os.system('echo "mail to ' + line + '" | mail -u "Postfix Test" -s "test" ' + line);

