print "You enter a dark room with two doors. How did you get here? Do you take door #1 or door #2?"

door = raw_input(">  ")

if door == "1":
  print "There's a giant bear here eating a cheese cake. What on earth do you do?"
  print "1. Take the cake."
  print "2. Scream at the bear."

  bear = raw_input("> ")

  if bear == "1":
    print "The bear eats your face of like The Revenant.  Good job."
  elif bear == "2":
    print "The bear eats your legs off. Good job."
  else:
    print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
  print "You stare into the endless abyss at Cthulhu's retina."
  print "1. Strawberries."
  print "2. Yellow Jacket clothespins."
  print "3. Understaning revolvers yelling melodies."

  insanity = raw_input("> ")

  if insanity == "1" or insanity == "2":
    print "Your body survives powered by a mind of jello. Great!"
  else:
    print "The insanity rots your eyes into a pool of muck."

else:
  print "You stumble around and fall on a knife and die."
