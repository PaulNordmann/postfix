import os, re;

testMailPath = 'testmails.conf';
email = raw_input('email: ').lower();

#check if it is a correct email!
if not re.match("[^@]+@[^@]+\.[^@]+", email):
	print 'Error: ' + email + ' is not an email';
	exit(1);

#check if the email is almost added
if os.path.isfile(testMailPath):
	for line in open(testMailPath, 'r'):
		if line.rstrip() == email: 
			print 'Error: ' + email + ' almost added';
			exit(1);


#add email;
conf = open(testMailPath, 'a');
conf.write(email + '\n');
conf.close();
print email + ' added';


