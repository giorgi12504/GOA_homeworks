#მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ for ციკლის გამოყენებით, გამოთვალეთ და გამოიტანეთ მხოლოდ კენტი რიცხვების ჯამი
number = int(input("Enter your number:"))
for i in range(1, number +1,  ):
    if i % number ==0:
        print(i)
