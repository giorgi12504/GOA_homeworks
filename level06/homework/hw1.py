#მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ for ციკლის გამოყენებით, გამოთვალეთ და გამოიტანეთ მხოლოდ კენტი რიცხვების ჯამი
number = int(input("Enter your number:"))
sum = 0
for i in range(1,number +1):

    if i %2 ==1:
        sum += i
        print(sum)


    