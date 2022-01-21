from random import choice
def checking_mail(addr,domain="pop.ac.uk"):
  '''Checks the domain of a mail.'''
  if "@" in addr:
    split_mail=addr.split("@")
    if split_mail[1]==domain:
      return True
    else:
      return False
def check(user_input):
  '''Returns the value of specific keyword required for interacting, if it is present in the argument.'''
  key_word=["library","wifi","deadline","hostel","food","sports"]
  for word in key_word:
    if word in user_input:
      return word
print("Welcome to Pop Chat\nOne of our operators will be pleased to help you today.")
bot=["Edrics","Jack","Heimans","Billie","Galot","Nejuko"]#Names for the system which later is used randomly 
noth=["Hmmm", "Oh, yes, I see","Tell me more","Ohh i see","Yes?","What?"]
exit=["bye","end","exit","quit"]
mail=input("Please enter your Poppleton email address:")
rate=[1,1,1,1,1,1,1,1,1,0]# helps to disconnect the server randomly by 10%
fort=checking_mail(mail)
if fort:
  sot=mail.split("@")
  name=sot[0]
  print(f"Hi {name}! Thank you, and Welcome to PopChat!\nMy name is {choice(bot)}, and it will be my pleasure to help you.")
  while True:
    enter=input("--->").lower()
    if choice(rate)==0:
      print("******NETWORK ERROR******")
      print(f"Thanks, {name}, for using PopChat. See you again soon!")
      break
    if enter.lower() in exit:
      print(f"Thanks, {name}, for using PopChat. See you again soon!")
      break
    dic={'library':['The library is closed today.','The library will open today','The library opens at 8 am'],#getting the values from the selected keywords 
      'wifi':['WiFi is excellent across the campus.','Wifi is not down','The Wifi is not available'],
      'deadline':['Your deadline has been extended by two working days.'],
      'hostel':['The food at the hostel is very bad','The hostels fee is $100 per month','2 people are to live in a single room'],
      'food':['The breakfast is served at 7 am ','The food is cooked by our own students.','Food is not ready'],
      'sports':['The students are able to play all sports','Its raining, you cant play any sports','You should first join some clubs']}   
    try:# it tests if there is any error
      print(choice(dic[check(enter)]))
    except:# it handles the error 
      print(choice(noth))
else:
  print("Invalid mail")