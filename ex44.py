# Inheritance

class Parent(object):

    def implicit(self):
        print "Parent implicit()"

    def override(self):
        print "PARENT override()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad  = Parent()
kid = Child()

dad.implicit()
kid.implicit()

dad.override()
kid.override()

dad.altered()
kid.altered()

# Composition

class Other(object):

    def implicit(self):
        print "OTHER implicit()"

    def override(self):
        print "OTHER override()"

    def altered(self):
        print "OTHER altered()"

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD after OTHER altered()"

kid = Child()

kid.implicit()
kid.override()
kid.altered()
