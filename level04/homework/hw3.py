#მომხმარებელს შემოყავს პროექტში მიღებული ქულის შესახებ, თუ ის 90-ზე მეტია შეფასებაა A, თუ 75-ზე მეტია შეფასებაა B, თუ 60-ზე მეტია შეფასებაა C, თუ 50-ზე მეტია შეფასებაა D, თუ 40-ზე E და თუ 30-ზე F,

score = float(input("Please Enter your project points: "))

if score > 90:
    grade = "A"
elif score > 75:
    grade = "B"
elif score > 60:
    grade = "C"
elif score > 50:
    grade = "D"
elif score > 40:
    grade = "E"
else:
    grade = "F"


print("result:" +  grade)
#done