# შექმენით პროგრამა რომელშიც შემოაყვანინებთ მომხმარებელს რაიმე სიყვას და თუ ეს სიტყვა იწყება "_"-ით მაშინ გამოიტანეთ True - თუ არა False

word = input("შეიყვანეთ სიტყვა: ").strip()  

if word and word[0] == "_":  
    print(True)  
else:  
    print(False)
