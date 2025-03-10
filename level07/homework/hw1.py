#1 შექმენით პროგრამა, რომელშიც მომხმარებელი შემოიტანს რიცხვს, თქვენ უნდა გამოიტანოთ ამ რიცხვის ყველა გამყოფი (ის რიცხვები რომლებზეც გაყოფისას მომხმარებლის მიერ შემოტანილ რიცხვზე ნაშთი 0-ია)# Take input from the user

number = int(input("Please enter a number: "))


გამყოფი = []

for i in range(1, number + 1):
    if number % i == 0: 
     გამყოფი.append(i)

print("The გამყოფი of", number, "are:",გამყოფი )
