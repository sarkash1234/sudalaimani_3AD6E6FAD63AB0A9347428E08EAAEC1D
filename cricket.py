class Player: 
  def play(self):
    print("The player is playingcricket.")

class Batsman(Player): 
  def play(self):
    print("The bats man is batting" )

class Bowler(Player): 
  def play(self):
    print("The bowler is bowling" )
# Creating objects of Batsman and Bowler classes
batsman=Batsman() 
bowler=Bowler()
# Calling the play() method for each object
batsman.play()
bowler.play()