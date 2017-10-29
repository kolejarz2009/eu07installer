#
#
from sys import argv
script, filename=argv
'''
#EU07Home="/home/m/MaSzyna/17.07"

txt=open(filename)
print("here's your file %r:" % filename
print(txt.read())

print("I'll also ask you to name it")
file_again=input()
txt_again=open(file_again)
print(txt_again.read())
'''
#This should work:
txt = open(filename, 'r')
print('Here\'s your file %r: ' % filename)
print(txt.read())
txt.close()

print('I\'ll also ask you to type it again: ')
file_again = input()
txt_again = open(file_again, 'r')
print(txt_again.read())
txt_again.close()


