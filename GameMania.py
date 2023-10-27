print('----------------------------------------------------WELCOME TO GAME MANIA---------------------------------------------------------\n \n \n')
import random   #global variable

#HANGMAN

def hangman():
 print("    WELCOME TO HANGMAN")
 print(" ---------------------------")
 print()
 name=input('enter your name: ')
 print('Hello ',name," Best of luck!!")
 words=["pizza", "nandos", "hongkong", "computer", "cheetos", "perfume", "jacket", "headphones", "hallway", "cookies"]
 word=random.choice(words)    #the random module chooses a random word from the above list and stores it in the variable 'word'.
 tries=6
 guessmade=""       #the 'guessmade' variable is used to store the letters that have already been guessed by the player.

 while len(word) and tries>=0:
     m_word=""
     for letter in word:
         if letter in guessmade:
             m_word= m_word+letter    
         else:
              m_word= m_word+"_"    
     if  m_word==word:
         print( m_word)
         print("you have won")
         break
     if tries==0:
         print("you have lost the game")
         print("the correct word is ",word)
         break
    
        
     print("guess the word", m_word)
     guess=input().lower()
     if guess in guessmade:        #check if the letters are printed more than once 
         guessmade=guessmade
         print("you have guessed the same letter more than once enter guess again")
         guess=input("try again").lower()
         guessmade=guessmade+guess  
         
    
     elif guess in 'abcdefghijklmnopqrstuvwxyz' or guess in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
         guessmade=guessmade+guess  
        
     else:
         print("enter valid character")
         guess=input("try entering a character again").lower()    

     if guess not in word:
         tries-=1   
         print("you have ",tries,"left")
     if tries==5:
                print("   ___ \n"
                   "  |      \n"
                   "  |      \n"
                   "  |      \n"
                   "  |      \n"
                   "  |      \n"
                   "  |      \n"
                    " _|_\n")
     elif tries==4:
                print("   ___ \n"
                   "  |     | \n"
                   "  |     |\n"
                   "  |      \n"
                   "  |      \n"
                   "  |      \n"
                   "  |      \n"
                    " _|_\n")
     elif tries==3:
               print("   ___ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                   " _|_\n")
     elif tries==2:
                print("   ___ \n"
                   "  |     | \n"
                   "  |     |\n"
                   "  |     | \n"
                   "  |     O \n"
                   "  |      \n"
                   "  |      \n"
                    " _|_\n")
     elif tries==1:
                print("   ___ \n"
                   "  |     | \n"
                   "  |     |\n"
                   "  |     | \n"
                   "  |     O \n"
                   "  |    /|\ \n"
                   "  |    / \ \n"
                    " _|_\n")


#TIC TAC TOE

def tictactoe():
    #Two player game tic tac toe
 
 print("Welcome to Tic Tac Toe")
 n1,n2,n3,n4,n5,n6,n7,n8,n9=1,2,3,4,5,6,7,8,9
 print(n1 , "|" , n2 , "|" , n3)
 print("-", "|", "-", "|", "-")
 print(n4 , "|" , n5 , "|" , n6)
 print("-" ,"|" , "-" ,"|" , "-")
 print(n7 , "|" , n8 , "|" , n9)
 player1=input("Enter name of player1: ")
 player2=input("Enter name of player2: ")
 print(player1 ,"your symbol is X: ")
 print(player2 ,"your symbol is O: ")
 count=1
 toss=random.randint(0,1)
 coin=["Heads","Tales"]
 if toss==0:
    selection=input("Player1 select Heads or Tales :")
 elif toss==1:    
    selection=input("Player2 select Heads or Tales :")
 Toss=random.choice(coin)
 if Toss==selection :
    print(player1," wins the toss")
    while count<=9:
     tries=count%2
     if tries==1:
         move1=int(input("player1 make the move enter number between 1-9"))
         if move1==1 :
           n1="x"
         elif move1==2 :
            n2="x"  
         elif move1==3 :
            n3="x"   
         elif move1==4 :
            n4="x"
         elif move1==5  :
            n5="x"    
         elif move1==6 :
            n6="x"
         elif move1==7 :
            n7="x" 
         elif move1==8 :
           n8="x"
         elif move1==9 :
          n9="x"
         print(n1 , "|" , n2 , "|" , n3)
         print("-", "|", "-", "|", "-")
         print(n4 , "|" , n5 , "|" , n6)
         print("-" ,"|" , "-" , "|" , "-")
         print(n7 , "|" , n8 , "|" , n9)    
         if tries==0:        
              move2=int(input("player2 enter number between 1-9"))
              if move2==1:
                  n1="o"
              elif move2==2:
                  n2="o"
              elif move2==3:
                  n3="o"
              elif move2==4:
                  n4="o"
              elif move2==5:
                  n5="o"     
              elif move2==6:
                  n6="o"
              elif move2==7:
                  n7="o"
              elif move2==8 :
                  n8="o"
              elif move2==9:
                  n9="o"       
              print(n1 , "|" , n2 , "|" , n3)
              print("-", "|", "-", "|", "-")
              print(n4 , "|" , n5 , "|" , n6)
              print("-" ,"|" , "-" , "|" , "-")
              print(n7 , "|" , n8 , "|" , n9)
         if count==3:
              if n1==n2==n3=="x" or n4==n5==n6=="x" or n7==n8==n9=="x" or n1==n4==n7=="x" or n2==n5==n8=="x" or n3==n6==n9=="x" or n7==n5==n3=="x" or n9==n5==n1=="x":
                  print(player1,"wins the match")
              elif n1==n2==n3=="o" or n4==n5==n6=="o" or n7==n8==n9=="o" or n1==n4==n7=="o" or n2==n5==n8=="o" or n3==n6==n9=="o" or n7==n5==n3=="o" or n9==n5==n1=="o":                         
                  print(player2,"wins the match") 
                  quit()
         if count==4:
              if n1==n2==n3=="x" or n4==n5==n6=="x" or n7==n8==n9=="x" or n1==n4==n7=="x" or n2==n5==n8=="x" or n3==n6==n9=="x" or n7==n5==n3=="x" or n9==n5==n1=="x":
                  print(player1,"wins the match")
              elif n1==n2==n3=="o" or n4==n5==n6=="o" or n7==n8==n9=="o" or n1==n4==n7=="o" or n2==n5==n8=="o" or n3==n6==n9=="o" or n7==n5==n3=="o" or n9==n5==n1=="o":                         
                  print(player2,"wins the match") 
                  quit()  
              elif count==9:
                  print("Its a draw")              
         count+=1        
 if Toss!=selection :
      print(player2 ,"wins the toss")        
      while count<=9 :
          tries=count%2
          if tries==1:
              move2=int(input("player2 make the move enter a number between 1 - 9 "))
              if move2==1:
                  n1="o"
              elif move2==2:
                  n2="o"
              elif move2==3:
                  n3="o"
              elif move2==4:
                  n4="o"
              elif move2==5:
                  n5="o"     
              elif move2==6:
                 n6="o"
              elif move2==7:
                  n7="o"
              elif move2==8 :
                  n8="o"
              elif move2==9:
                  n9="o"       
              print(n1 , "|" , n2 , "|" , n3)
              print("-", "|", "-", "|", "-")
              print(n4 , "|" , n5 , "|" , n6)
              print("-" , "|" , "-" , "|" , "-")
              print(n7 , "|" , n8 , "|" , n9)     
          if tries==0:    
              move1=int(input("player1 enter number between 1-9"))
              if move1==1  :
                  n1="x"
              elif move1==2 :
                  n2="x"  
              elif move1==3 :
                  n3="x"   
              elif move1==4 :
                  n4="x"
              elif move1==5  :
                  n5="x"    
              elif move1==6 :
                  n6="x"
              elif move1==7 :
                  n7="x" 
              elif move1==8 :
                  n8="x"
              elif move1==9 :
                  n9="x"
              print(n1 , "|" , n2 , "|" , n3)
              print("-", "|", "-", "|", "-")
              print(n4 , "|" , n5 , "|" , n6)
              print("-" , "|" , "-" , "|" , "-")
              print(n7 , "|" , n8 , "|" , n9)
          if n1==n2==n3=="x" or n4==n5==n6=="x" or n7==n8==n9=="x" or n1==n4==n7=="x" or n2==n5==n8=="x" or n3==n6==n9=="x" or n7==n5==n3=="x" or n9==n5==n1=="x":
              print(player1,"wins the match")
              break
          elif n1==n2==n3=="o" or n4==n5==n6=="o" or n7==n8==n9=="o" or n1==n4==n7=="o" or n2==n5==n8=="o" or n3==n6==n9=="o" or n7==n5==n3=="o" or n9==n5==n1=="o":                         
              print(player2,"wins the match") 
              break
          elif count==9:
              print("Its a draw")                   
          count+=1
def main():
    game = input("Would you like to play Hangman or Tic Tac Toe? Enter 'Hangman' or 'TicTacToe': ").lower()

  # Start the chosen game
    if game == "hangman":
      hangman()
    elif game== "tictactoe":
      tictactoe()
    else:
      print("Invalid choice")

main()

