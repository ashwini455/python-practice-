marks=int(input('enter your marks: '))
match marks:
    case marks if marks >= 90:
        print('A+')
    case marks if marks >= 80:
        print('A')
    case marks if marks >= 70:
        print('B')
    case marks if marks >= 60:
        print('C')
    case marks if marks >= 50:
            print('D')
    case marks if marks >= 40: 
        print('E')
    case marks if marks < 40:
        print('Fail') 
    case _:
        print('Invalid marks')


quater=int(input('enter your quater:'))
match quater:
     case quater if quater == 1:
         print('january to march')
     case quater if quater == 2:
         print('april to june')
     case quater if quater == 3:
         print('july to september')
     case quater if quater == 4:
          print('october to december')
     case _:
         print('Invalid quater') 

a=int(input('enter your number:'))
b=int(input("enter your number:"))
c=input('enter your operation:')
match c:
    case c if c == '+':
        print('result:',a+b)
    case c if c == '-':
        print('result:',a-b)
    case c if c == '*':
        print('result:',a*b)
    case c if c == '/'  :
        print('result:',a/b)
    case c if c == '%'  :
        print('result:',a%b)
    case c if c == '//'  :
        print('result:',a//b)
    case c if c == '**':
        print('result:',a**b)
    case _:
        print('Invalid operation')


day = int(input("Enter day (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")



n = int(input("Enter number: "))

match n % 2:
    case 0:
        print("Even")
    case 1:
        print("Odd")



light = input("Enter light colour: ").lower()

match light:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid colour") 


ch = input("Enter a letter: ").lower()

match ch:
    case "a" | "e" | "i" | "o" | "u":
        print("Vowel")
    case _:
        print("Consonant")


choice = int(input("1. Tea\n2. Coffee\n3. Juice\nEnter choice: "))

match choice:
    case 1:
        print("Tea")
    case 2:
        print("Coffee")
    case 3:
        print("Juice")
    case _:
        print("Invalid choice") 




month = int(input("Enter month number (1-12): "))

match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid month")



n = int(input("Enter number (1-5): "))

match n:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case 5:
        print("Five")
    case _:
        print("Invalid number")  



username = input("Enter username: ")

match username:
    case "admin":
        print("Welcome Admin")
    case "student":
        print("Welcome Student")
    case "teacher":
        print("Welcome Teacher")
    case _:
        print("User not found")

                                                                    
                
