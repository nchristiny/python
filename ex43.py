from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    quips = [
        "You died. You really suck at this.",
        "Well at least you died young and left a pretty corpse.",
        "Great job. You are dead.  FAIL",
        "I have a small puppy that's better than this.",
        "I had such high hopes for you. SMH"
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips) - 1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(sefl):
        print "The Gothons of Planet Percal #25 have invaded and destroyed"
        print "you entire crew! You are the last surviving member and you last"
        print "mission is to get the neutron destruct bomb from the Weapons Armory,"
        print "put it in the bridge, and blow up the ship up after getting into an"
        print "escape pod."
        print "\n"
        print "You're running down the central corridor to the Weapons Armory when "
        print "a Gothon jumps out with red scaly skin, dark grimy teeth, terrible BO and "
        print "evil yellow dog eyes flowing around it's hate-filled body. Its blocking the door to the"
        print "armory and about to pull a weapon and blast you!"
        print "Shoot!, Dodge!, Tell a joke or something else? "
        action = raw_input(">>> ")

        if action == "Shoot!":
            print "Quick on the draw you yank out your blaster and fire it at the slimy bugger."
            print "His clown costume is flowing and moving around its body, which throws"
            print "off your aim. Your laser hits its costume but misses the alien entirely. This is embarrasing."
            print "It flies into a rage and blasts you repeatedly in the face with their laser until you die."
            print "Then it eats you."
            return 'death'

        elif action == "Dodge!":
            print "Like a world class boxer you dodge, weave and slip n slide right"
            print "as the Gothon's blaster cranks a laser past your head."
            print "IN the middle of your artful dodge your foot slips and you"
            print "bang your head on the metal wall and pass out."
            print "You wake up shortly after only to die as the Gothon curb-stomps you."
            print "Then they eat you. You die."
            return 'death'

        elif action == "Tell a joke":
            print "Lucky for you they made you learn Gothon insults at the Academy."
            print "You tell the best Gothon joke you know:"
            print "Lofd asdf fdwef POPTUPH PHIIFPF"
            print "The Gothon stops, tries not to laugh, then bursts out laughing, rolling incapacitated on the floor."
            print "While the Gothon laughs, you are able to calmly line up and shoot  it in the head."
            print "You then leap through the Weapon Armory door!"
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE!!"
            return 'central_corridor'


class LaserWeaponArmory(Scene):

     def enter(self):
        print "You do a dive roll into the Weapon Armory, crouch and scan the room"
        print "for more Gothons that might be lurking. It's dead quiet, too quiet..."
        print "You stand up and run to the far side of the room and find the"
        print "neutron bomb in its container. There's a keypad lock on the box"
        print  "and you need the code to get the bomb out. If you get the code"
        print "wrong 10 times then the lock closes permanently and you will not be"
        print "Able to get the bomb. The code is 3-digits (real secure)."
        print "You actually have knowledge of one of the digits, being a ranking officer."
        print "The first digit is 9. The second is 4"
        print "You will have to guess the thrid one."
        code = "%d%d%d" % (9, 4, randint(1,9))
        guess = raw_input("[keypad]>>> ")
        guesses = 0

        while guess != code and guesses < 10:
            print "BZZZZZTTTTT!"
            guesses += 1
            guess = raw_input("[keypad]>>> ")

        if guess == code:
            print "The container clicks open and the seal breaks, letting gas whoosh out."
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it in the right spot."
            return 'the_bridge'
        else:
          print "The lock buzzes one last time and then you hear a sickening"
          print "melting sound as the mechanism fuses together."
          print "You decide to sit there and finally the Gothons blow up the ship."
          print "You die."
          return 'death'

class TheBridge(Scene):

    def enter(self):
        print "You burst into the Bridge with the netron destruct bomb"
        print "under your arm.  You surprise 5 Gothons who are trying to "
        print "take control of the ship. Each of them has an even uglier"
        print "clown costume than the last. They haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't want to set it off."
        print "Throw the bomb? Or: Slowly place the bomb'?"

        action = raw_input("> ")

        if action == "Throw the bomb":
            print  "You chunk the bomb at the Gothans really hard."
            print "You leap for the door.  Right as you drop it a"
            print "Gothon shoots you right in the back, tragically killing you."
            print "During your dying breaths, you see another Gothon frantically trying to "
            print "disarm the bomb. You die knowning they will probably blow up when it"
            print "goes off. Oh well."
            print "BOOM"
            return 'death'

        elif action == 'Slowly place the bomb':
            print "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hands up and start to sweat."
            print "You inch backwards to the door, open it and then carefully"
            print "place the bomb on the flloor, all the while pointing your blaster at it."
            print "You then jumpo back throught the door and punch the close button,"
            print "blasting it so the Gothons can't get out."
            print "Now that the bomb is placed you run out to the escape pod to"
            print "get off this doomed tin can."
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return "the_bridge"

class EscapePod(Scene):

    def enter(self):
        print "You rush through the ship desperately trying to make it to"
        print "the escape pod before the whole ship explodes. it seems like"
        print "hardly any Gothons are on the ship, so your run is clear of"
        print "interference. You get to the chamber with the escape pods, and"
        print "now need to pick one to take. Some of them could be damaged"
        print "but you don't have time to look. There's 5 pods, whick one do you take?"

        good_pod = randint(1,5)
        guess = raw_input("[pod #]>>> ")

        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod escapes out into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into jam jelly."
            return 'death'
        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out of the dock and into space, heading"
            print "for the planet below. As it flies to the planet, you look"
            print "back and see your ship implodes then explodes like a"
            print "bright star, taking out the Gothon ship as well. WOO HOO,  way to go."

            return 'finished'

class Finished(Scene):

    def enter(self):
        print "You won, wow. That's actually pretty surprising.  "
        return 'finished'

class Map(object):

    scenes = {
            'central_corridor': CentralCorridor(),
            'laser_weapon_armory': LaserWeaponArmory(),
            'the_bridge': TheBridge(),
            'escape_pod': EscapePod(),
            'death': Death(),
            'finished': Finished()
        }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val =Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
