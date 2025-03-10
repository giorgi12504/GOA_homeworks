#მომხმარებელს შემოატანინეთ ნებისმიერი სიტყვა, შემდეგ ამ სიტყვიდან გამოიტანეთ მხოლოდ 'A' ასოები, თუ არ შეიცავს 'A'ს გამოიტანეთ ცარიელი სტრინგ

word = input("Enter a word: ")


a_letters = ""

for char in word:
    if char == 'A' or char == 'a':
        a_letters += char 


print(a_letters)
