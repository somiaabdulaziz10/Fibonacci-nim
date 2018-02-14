print("***you should be smart to play this game,if you not please get out***")
print("This game is called fibanocci nim..*in this game you have coins you should choose the number of coins,the number of coins which you wanted and donot forget to choose a friend to play with him ;)*")
player1=input("enter your name:")
player2=input("enter your name:")
n=int(input("the number of coins is"))
while (n<0) or (n==0) or (n==1):
    print ("please enter a number bigger than one")
    n=int(input("the number of coins is"))
m=int(input("player1 please choose your number of coins:"))
while(m>=n)or (m<0):
   print("please choose number less than the number of coins,bigger than zero")
   m=int(input("player1 please choose your number of coins:"))
n=n-m  
while(n!=0):
 z=int(input("player2 please choose your number of coins:"))
 while(z>n) or (z>2*m)or(z<0):
  print("**please choose number less the num of coins, less than the double of the player1's number, bigger than zero**")
  z=int(input("player2 please choose another number:"))
 n=n-z
 print("ba2y coins:",n)
 if(n==0):
    print("player2 won :D")
    break
 m=int(input("player1 please choose your number of coins:"))
 while(m>n)or(m<0):
   print("please choose number less than the number of coins")
   m=int(input("player1 please choose your number of coins:"))
 n=n-m
 if(n==0):
    print("player1 won :D)
    break
   

 
