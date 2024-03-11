

# welcome message and display status 
print("Welcom to Number scrabble.")
print("Each player takes turns picking a number from 1 to 9.") 
print("Once a number has been picked, it cannot be picked again.")
print("If a player has picked three numbers that add up to 15, that player wins the game.")
print("if all the numbers are used and no player gets exactly 15, the game is a draw.")

Num= [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
numbers_for_player_1=[]
numbers_for_player_2=[]

# function finds probabilities
def win(Num):
    sum = 0
    for i in range(0, len(Num)):
        for j in range(i+1, len(Num)):
            for k in range(j+1, len(Num)):
                summation = Num[i] + Num[j] + Num[k]
                if summation == 15 :
                    return True
    return False            
        
# game playing 
while True :              # player 1's turn 
    
   
    
    print("Available numbers are :" , Num , "\n")   
    global num1
    while True :  
        try : 
            num1=int(input("Player one, pick a number: "))      #take the number that player one choose 
            while num1 not in  Num :                          #  loop for mistakes 
                print("Please select a valid number ")
                num1=int(input("Player one, pick a number: "))
            break      
        except ValueError :
            print("please choose a number")        
            
    
    numbers_for_player_1.append(num1)        # make the list for player one  
    print("player one: ", numbers_for_player_1)
    if win(numbers_for_player_1) :             # function checks if he won or not
        print("player one is the winner")
        break
    
    Num.remove(num1)                       # remove the number choosen from the list 
    print("Available numbers are : " , Num , "\n" )
    if len(Num) == 0 :
        print("the game is a draw.")
        break
     # player 2's turn 
    global num2 
    while True :
        try :
            
            num2=int(input("Player two, pick a number: "))        #take the number that player two  choose
        
            
            while num2 not in  Num :                                #  loop for mistakes 
                print("Please select a valid number ")
                num2=int(input("Player two, pick a number: ")) 
            break        
        except ValueError : 
             print("please choose a number")        
            
               
    numbers_for_player_2.append(num2)                    # make the list for player one  
    print("player two: " , numbers_for_player_2 )
    if win(numbers_for_player_2) :                       # function checks if he won or not
        print("player two is the winner")
        break
    
    Num.remove(num2)    
    
        
        
    

