import os, subprocess, time

# stop the service
time.sleep(5)
args = ['sc', 'stop', 'Spooler']
result = subprocess.run(args)

# erase the files 
path = "C:\Windows\System32\spool\PRINTERS"
dir = path
time.sleep(5)
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))

""" print("El archivo ha sido eliminado") """

# start the service
time.sleep(5)
args = ['sc', 'start', 'Spooler']
result = subprocess.run(args)
