print("Stop! Who would cross the Bridge of Death\nMust answer me these questions three, 'ere the other side he see.'\n")
name=input("What is your name?").lower()
if name=="arthur":
  print("My liege! You may pass!")
else:
  what_u_seek=input("Name what you seek!")
  if "grail" in what_u_seek:#checks if the word grail is in the answer
    fav_colour=input("What is your favourite colour:").lower()
    if name[0]==fav_colour[0]:#checks to see if the first letter of name and color is equal
      print("You may pass!")
    else:
      print("Incorrect! You must now face the Gorge of Eternal Peril.")
  else:
    print("Only those who seek the Grail may pass.")