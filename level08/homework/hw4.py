#შექმენით პატარა თამაში, სადაც თქვენ შექმნით რაიმე რიცხვების თანმიმდევრობას (ოთხნიშნა integer-რიცხვი), და მომხმარებელმა კი უნდა გამოიცნოს ეს თანმიმდევრობა (გამოიყენეთ While loop)
number1 = int(input("Enter sequences:"))
number = 345
while number1 != number:
    number1 = int(input("Enter sequences:"))
    
if number1 == number:
    print("you have logged in sucssfully")
    
#For loop-ის დახმარებით შექმენით პროგრამა, სადაც მომხმარებელი შემოიტანს რიცხვს (50-ის ჩათვლით, თუ არა დაუპრინტეთ, რომ თავიდან შეიყვანოს), და თქვენ გამოიტანეთ ამ რიცხვის ჯერადები 100-ის ჩათვლით.

number = int(input("enter your number"))
if number <= 50:
    for i in range(number, 101, number):
        print(i)
else:
    print("please enter number that is bellow 50")
