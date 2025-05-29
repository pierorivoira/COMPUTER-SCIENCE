"""
get system info
"""

import json, os
from tkinter.simpledialog import askstring
# user = os.getlogin()
# os.chdir('/home/%s/COMPUTER_SCIENCE/AI' % user)
print("Il programma visualizza le seguenti informazioni: <sysname>, <nodename>, <release>, <version> e <machine>")
# question = askstring('Entry', "Inserisci l'informazione desiderata")
info = os.uname()
info = "{0}".format(info)
with open("uname.txt", "w") as text_file:
    text_file.write("%s" % info)
with open('uname.txt') as f:
    newtext = f.read().replace("posix.uname_result(", "{'")
with open('uname.txt', 'w') as f:
    f.write(newtext)
with open('uname.txt') as f:
    newtext = f.read().replace("=", "':")
with open('uname.txt', 'w') as f:
    f.write(newtext)
with open('uname.txt') as f:
    newtext = f.read().replace(", ", ", '")
with open('uname.txt', 'w') as f:
    f.write(newtext)
with open('uname.txt') as f:
    newtext = f.read().replace(")", "}")
with open('uname.txt', 'w') as f:
    f.write(newtext)
with open('uname.txt') as f:
    newtext = f.read().replace("'", '"')
with open('uname.txt', 'w') as f:
    f.write(newtext)
with open('uname.txt', 'r') as file:
    info = file.read()
info = json.loads(info)
# if question == 'sysname':
sysname = info['sysname']
print("Il sistema operativo è <%s>" % sysname)
# elif question == 'nodename':
nodename = info['nodename']
print("Il nome del nodo è <%s>" % nodename)
# elif question == 'release':
release = info['release']
print("Il nome della release è <%s>" % release)
# elif question == 'version':
version = info['version']
print("Il nome della versione è <%s>" % version)
# elif question == 'machine':
machine = info['machine']
print("Il nome della macchina è <%s>" % machine)
