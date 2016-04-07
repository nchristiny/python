class Song(object):

  def __init__(self, lyrics):
    self.lyrics = lyrics

  def sing_me_a_song(self):
    for line in self.lyrics:
      print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally round the family",
                        "With a pocket full of sunshine!"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

sad_n_stuff = ["Yeah, yeah,",
         "Yeah, yeah",
         "Let me make your stasis",
         "My, my, my, my serpentine",
         "I got a breathalyzer",
         "And a bad ass dream",
         "Yeah, yeah",
         "Yeah, yeah",
         "Yeah, yeah, yeah, yeah",
         "Yeah"]

we_are_sex_bbbomb = Song(sad_n_stuff)

we_are_sex_bbbomb.sing_me_a_song()
