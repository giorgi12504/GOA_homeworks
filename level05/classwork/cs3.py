#შექმენით correct_password ცვლადი სადაც შეინახავთ რაიმე პაროლს, შემდეგ მომხმარებელს inputით შემოატანინეთ რაიმე პაროლი, სანამ ეს მომხმარებლის შემოტანილი პაროლი არ უდრის correct_passwordს თავიდან შემოატანინეთ მომხმარებელს პაროლი
correct_password = ("blah123")
user_input = input("please enter your password:")
while user_input != correct_password:
    print("please try again:")
    user_input = input("please enter your password:")
    

    print("logged in succsesfully")


    
   



