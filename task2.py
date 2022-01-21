print("Swallow Speed Analysis: Version 1.0")
count=0
stat=[]
while True:
  reading=input("Enter the Next Reading:").upper()
  if count==0 and reading=="":#checks if the entered value and number is nothing and the number of times the val
    print("No readings entered. Nothing to do.")
    break
  elif reading=="" and count>=1 :#checks if the input is zero and the number of counts is greateror equal to 1
    max_speed=max(stat)
    avg_speed=sum(stat)/len(stat)
    min_speed=min(stat)
    print("Results Summary")
    print(count,"Reading Analysed")
    print(f"Max speed: {max_speed:.2f} MPH, {max_speed*1.61:.2f} KPH.")
    print(f"Min speed: {min_speed:.2f} MPH, {min_speed*1.61:.2f} KPH.")
    print(f"Avg speed: {avg_speed:.2f} MPH, {avg_speed*1.61:.2f} KPH.")
    break
  else:
    read=reading[1:]
    count+=1
    print("Reading saved")
    if reading[0]=="E":#checks if the first value is U or E
      new=float(read)/1.61
      stat.append(new)
    elif reading[0]=="U":
      new=float(read)
      stat.append(new)
      #print(stat)
    else:
      print("Wrong Reading!!")