# Simple Grade Calculator

def grade_calculator():
    print("=" * 40)
    print("     SIMPLE GRADE CALCULATOR")
    print("=" * 40)
    
    # Get number of subjects
    n = int(input("\nEnter number of subjects: "))
    
    total = 0
    
    # Get grades for each subject
    for i in range(n):
        grade = float(input(f"Enter grade for subject {i+1}: "))
        total += grade
    
    # Calculate average
    average = total / n
    
    # Determine letter grade
    if average >= 90:
        letter_grade = 'A'
    elif average >= 80:
        letter_grade = 'B'
    elif average >= 70:
        letter_grade = 'C'
    elif average >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    
    # Display results
    print("\n" + "=" * 40)
    print("Average Score: {:.2f}".format(average))
    print("Letter Grade: {}".format(letter_grade))
    print("=" * 40)

# Run the calculator
grade_calculator()
