from story2 import *
#import HTML_output
storyname =('The Emperor\'s Authority')
filename=(storyname+'.html')

output_file = open(filename,'w')
file_header = '''<!DOCTYPE html>
	<html lang='en'>
		<head>
			<title>'''+storyname+'''</title>
			<link rel="stylesheet" type='text/css' href='roster.css'>
		</head>
		<body>'''
output_file.write(file_header)
def Paragraphs(c):
    #output_file.write('<p>'+c+'</p>')
    output_file.write('<p>'+c)
def document_write(c):
    output_file.write(c)
def close_Paragraphs():
    output_file.write('</p>')
def close():
        output_file.write('</body></html>')
        output_file.close()
        print('Story compiled')

training = 0
print(S00001)
c = S00001
Paragraphs(c)
#print('S00001')
#SM_01.StatTest('Weapon Skill' ,30, True)
#SM_01.StatTest('Weapon Skill' ,30, False)
if SM_01.StatTest('Weapon Skill',30,False):
    print(S00002a)
    c = S00002a
    document_write(c)
    training = training+1
    #print(DoS)
    if SM_01.StatTest('Agility' ,30, False)[0]:
        #print(DoS)
        print(S00003a)
        c = S00003a
        training = training+1
        document_write(c)
        SM_01.StatTest('Weapon Skill' ,50, False)
    else:
        print(S00003b)
        #print(DoS)
        c = S00003b
        training = training+1
        document_write(c)
        #print(training)
else:
        print(S00002b)
        #print(DoS)
        c = S00002b
        document_write(c)
        close_Paragraphs()
        #print('S00002b')
        training = -1
        print(training)
close()
