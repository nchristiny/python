# i = 0
# numbers =[]

# while i < 6:
#   print "At the top i is %d" % i
#   numbers.append(i)

#   i = i + 1
#   print "Numbers now: ", numbers

#   print "At the bottom i is %d" % i

# print "The numbers: "

# for num in numbers:
#   print num

# def loopy_loop(max, step):
#   i = 0
#   numbers =[]

#   while i < max:
#     print "At the top i is %d" % i
#     numbers.append(i)

#     i += step
#     print "Numbers now: ", numbers

#     print "At the bottom i is %d" % i

#   print "The numbers: "

#   for num in numbers:
#     print num

def loopy_loop(max, step):
    """
    For-loop over a certain range from zero to maximum at a given step amount.
    Incrementing is no longer needed due to range, a built in type
    that represents an "immutable sequence"  of numbers. Range accepts
    min, max, and third argument step which serves as incremental value.
    """
    numbers = []
    for num in range(0, max, step):
        print "At the top number is %d" % num
        numbers.append(num)
        # num += step  # Not necessary
        print "Numbers now: ", numbers
        print "At the bottom number is %d" % (num + step)
    print "The numbers: "
    for num in numbers:
        print num

loopy_loop(10, 2)
