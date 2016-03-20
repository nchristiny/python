def print_two(*args):
  arg1, arg2 = args
  print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
  print "arg1: %r, arg2: %r" % (arg1,arg2)

def print_one(arg1):
  print "arg1: %r" % arg1

def print_none():
  print "Got nothin'."

print_two("ZOMG", "ILUVU")
print_two_again("ZOMG","ILYSM")
print_one("Hola")
print_none()
