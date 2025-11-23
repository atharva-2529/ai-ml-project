import random

print(" domestic/international")
dist=(input())



def domestic():
 if dist=="domestic":
  print("Enter Starting Point:")
  start=input()
  print("Enter destination")
  dest=input()
  print("enter ticket/seat preference:")
  print("Economy")
  print("Premium Economy")
  print("Business")
  pref=input()
  print("Enter trip preference")
  print("one way / round trip")
  trip=input()
  print("Enter Date")
  date=input()
  print("----------------------------------------------------")

  print("Your ticket is successfully booked. ")

  print("-----------------------------------------------------")
  print("From:" + " " + start + " " + "To:" +" " + dest) 
  print("Date")
  print(date)
  print("Seat number:")
  print(random.randint(1,100))
  print("Seat type:")
  print(pref)
  print("Price:INR")
  print(random.randint(3000,10000))
  print(trip)



domestic()



def international():
 if dist=="international":
  print("Enter Starting Point:")
  start=input()
  print("Enter destination:")
  dest=input()
  print("enter ticket/seat preference:")
  print("Economy")
  print("Premium Economy")
  print("Business")
  pref=input()
  print("Enter trip preference:" )
  print("one way / round trip")
  trip=input()
  print("Enter Date:")
  date=input()
  print("----------------------------------------------------")

  print(" Your ticket is successfully booked. ")

  print("-----------------------------------------------------")
  print("From:" + " " + start + " " + "To:" + " "+ dest) 
  print("Date:")
  print(date)
  print("Seat number:")
  print(random.randint(1,100))
  print("Seat type:")
  print(pref)
  print("Price:INR")
  print(random.randint(70000,100000))
  print(trip)


international()





print("---------------------------------------")








