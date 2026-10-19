
print("==============================")
print("   STUDENT MARKS CALCULATOR")
print("==============================")

name = input("Enter student name: ")

subjects = ["English", "Maths", "Science", "Computer", "Hindi"]
total = 0
all_passed = True

for subject in subjects:
    while True:
        try:
            marks = float(input(f"Enter marks in {subject} (0-100): "))
            if 0 <= marks <= 100:
                break
            print("Enter marks between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

    total += marks

    if marks < 33:
        all_passed = False

percentage = total / len(subjects)

print("\n========== RESULT ==========")
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print(f"Percentage: {percentage:.2f}%")

if not all_passed:
    print("Grade: F")
    print("Result: Fail")
elif percentage >= 90:
    print("Grade: A+")
    print("Result: Excellent!")
elif percentage >= 80:
    print("Grade: A")
    print("Result: Very good!")
elif percentage >= 60:
    print("Grade: B")
    print("Result: Good!")
else:
    print("Grade: C")
    print("Result: Pass")

print("============================")
