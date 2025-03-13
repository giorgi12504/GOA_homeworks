#მომხარებელს შემოატანინეთ რაიმე რიცხვი, შემდეგ for ციკლის გამოყენებით შეამოწმეთ, არის თუ არა ეს რიცხვი მარტივი, თუ არის დაპრინტეთ "your number is a prime" თუ არ არის დაპრინტეთ "your number is not a prime" 

number = int(input("Enter your number please:"))
aris_martivi_ricxvi = True

for i in range(2, number):
         if number%i==0:
              aris_martivi_ricxvi =False
              break
if aris_martivi_ricxvi and number > 1:
     print("your  number is a prime")
else:
     print("your number is not a prime")
     #Done 
                   

         
         


    
    




                                              
            
                

                        
                       
                 



                 

        
        




   

    

 
    



