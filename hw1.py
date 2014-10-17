# crypto - hw1.problem7
import binascii
import struct

old_cipher  = 0x6c73d5240a948c86981bc294814d
old_message = long("attack at dawn".encode("hex"),16)
old_key = old_cipher ^ old_message

new_message = long("attack at dusk".encode("hex"),16)
new_cipher = new_message ^ old_key

print "old cipher  = %x" % (old_cipher)
print "old message = %x" % (old_message) 
print "old key     = %x" % (old_key)

print "new message = %x" % (new_message) 
print "new cipher  = %x" % (new_cipher)


#