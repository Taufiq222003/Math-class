import random #imports random library from python


def main():

    print("Welcome to Maths Class.") #welcome statement
    print("This program helps you study math by mastering the skills of addition, subtraction and multiplication.")
    print("**You must get 3 in a row correct in order to go to the next step.**")
    print("***BEST OF LUCK***")

    addition_1()

    subtraction_2()

    print("Do you want to continue and do Multiplications? \n\nIf yes, please enter '1', else enter '2'." )
    input_user = int(input())
    
    if input_user == 1:
        multiply_3()
    else:
        print("Ok, bye. Hope to see you soon.")

    

def addition_1(): #this function is the code for addition part
     streak = 0
     num_correct = 3
     while streak < num_correct: #used to run the program untill user does 3 additions correct in row

        x = random.randint(1,100) #generates random number between 1-100, num 1
        y = random.randint(1,100) #generates random number between 1-100, num 2
        sum = x + y #summation of two integers
    
        print("What is " + str(x) + " + " + str(y) + " ?") #prints "What is the sum of 'x' + 'y'?"
    
        input_user = int(input("Your answer: ")) #takes user input
        
        if input_user == sum:
            streak += 1 #increments by one when user corrects one addition
            print("Correct! ") 
            print("You've gotten " + str(streak) + " correct in a row.")
   
        else:
            print("Incorrect. ")
            streak = 0
            print("The expected answer is " + str(sum))

        if streak == num_correct:
            print("Congratulations! You mastered addition.")
            print("")
            print("Now it's turn for Subtraction. ")

def subtraction_2(): #this function is the code for subtraction part
     streak = 0
     num_correct = 3
     while streak < num_correct: 

        x = random.randint(1,100) 
        y = random.randint(1,100)
        subtraction = x - y #subtraction of two integers
    
        print("What is " + str(x) + " - " + str(y) + " ?") #prints "What is the subtraction of 'x' - 'y'?"
    
        input_user = int(input("Your answer: ")) 
        
        if input_user == subtraction:
            streak += 1 #increments by one when user corrects one subtraction
            print("Correct! ") 
            print("You've gotten " + str(streak) + " correct in a row.")
   
        else:
            print("Incorrect. ")
            streak = 0
            print("The expected answer is " + str(subtraction))

        if streak == num_correct:
            print("Congratulations! You mastered subtraction too.")
            
def multiply_3(): #this function is the code for multiplication part
     streak = 0
     num_correct = 3
     while streak < num_correct: 

        x = random.randint(1,12) 
        y = random.randint(1,12)
        multiplication = x * y #multiplication of two integers
    
        print("What is " + str(x) + " x " + str(y) + " ?") #prints "What is the multiplication of 'x' x 'y'?"
    
        input_user = int(input("Your answer: ")) 
        
        if input_user == multiplication:
            streak += 1 #increments by one when user corrects one multiplication
            print("Correct! ") 
            print("You've gotten " + str(streak) + " correct in a row.")
   
        else:
            print("Incorrect. ")
            streak = 0
            print("The expected answer is " + str(multiplication))

        if streak == num_correct:
            print("So proud of you. Best of luck for your future. ")

    
if __name__ == '__main__':
    main()