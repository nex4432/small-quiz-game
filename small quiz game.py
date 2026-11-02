score = 0


while True:
 answer1 = str(input("What is the name of the final boss in Terraria?" ))


 if answer1.lower() == "moon lord":
    print("Correct")
    score = score + 1

 elif answer1.strip() == "":
    print("you can't just leave a blank")
    continue
    

 
 else:
    print("Wrong, the answer was mood lord")
    
 break
    

while True:
  answer2 = str(input("What is the main character's name in Hollow Knight?" ))

 
  if answer2.lower() == "the knight":
    print("Correct")
    score = score + 1
  elif answer2.strip() == "":
    print("you can't just leave a blank")
    continue

    
  else:
   print("Wrong, the answer was the knight")
   
  break


while True:
  answer3 = str(input("What game features the character Kratos?" ))



  if answer3.lower() == "god of war":
    print("Correct")
    score = score + 1
  elif answer3.strip() == "":
    print("you can't just leave a blank")
    continue
    
  else:
    print("Wrong, the answer god of war")
    

  break 
    

print("your score is:", score)