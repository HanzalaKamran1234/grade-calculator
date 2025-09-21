#Grade Calculator (input marks → output grade A/B/C/D/F)

marks = float(input("Enter your marks:"))

if marks >= 90 and marks <=100:
    print("You got Grade A")
elif marks >= 80 and marks < 90:
    print("You got Grade B")
elif marks >= 70 and marks < 80:
    print("You got Grade C")
elif marks >= 60 and marks < 70:
    print("You got Grade D")
elif marks >= 50 and marks < 60:
    print("You got Grade E")
elif marks >= 0 and marks < 50:
    print("You have Failed")
else:
    print("Write correct Number")
