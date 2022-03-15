#Jayvee N Mapote
#Midterm
#A11
def ending():
    exit()
def InputNum():
    
    num = [int(input('Enter a Number: ')) for i in range(10)]
    a = sorted(num)                                     
    b = sorted(num, reverse=True)
    c = sum(num)/len(num)
    d = max(num)
    e = min(num)
    print('\nInput Order: %s\nAscending Order: %s\nDescending Order: %s\nAverage: %s\nHighest: %s\nLowest: %s' 
    %(str(num),str(a),str(b),str(c),str(d),str(e)))

def InputWord():
    
    a = [str(input('Enter a String: ')) for i in range(5)]
    b = sorted(a)                                     
    c = sorted(a, reverse=True)
    print('\nInput Order: %s\nAlphabetical order: %s\nReverse order: %s' %(str(a),str(b),str(c)))

def Grading_System():

    Course_code = []
    Course_grade = []
    Course_unit = []
    i = 0
    x = 0
    z=0
    Name = str(input("Enter your name: "))
    Student_number = str(input("Enter your Student Number: "))
    Program = str(input("Enter your Program: "))
    Units = int(input("Enter your Units enrolled: "))
    if Units >= 12 and Units <=18:
        print()
    else:
        print("Wrong Input!")
        Grading_System()
    while i <= 0:
        Course_code.append(str(input("Enter your Course Code: ")))
        Course_grade.append(float(input("Enter your Course Grade: ")))
        Course_unit.append(int(input("Enter your Units: ")))
        if Course_unit[z] >5:
            print("Wrong Input")
            Grading_System()
            z+1
        i = int(input("Enter 1 if you're done else type 0: "))
        y = len(Course_grade)
        z = 0
    while z < y:
        x += (Course_grade[z]*Course_unit[z])
        z+=1
    z=0
    for loop in range(y):
        if Course_grade[z] < 5:
            a = 1
        else:
            a = 0
        z+=1
    Course_unit = ['%.2f' % elem for elem in Course_unit]
    Course_grade = ['%.2f' % elem for elem in Course_grade]
    gwa = x/Units
    print("\n\n\nStudent Name: " + Name)
    print("Student Number: " + Student_number)
    print("Program: " + Program)
    print("\n")
    z=0
    print("CourseCode\tUnits\tGrades")
    for k in range(y):
        print(str(Course_code[z])+"\t\t",str(Course_unit[z])+"\t",str(Course_grade[z]))
        z+=1
    print("\n")
    print("Total Units: " + str(Units))
    if gwa <= 1.50 and a == 1:
        print("General Weighted Average: " + str(gwa))
        print("Lister Status: President’s Lister")
    elif gwa <= 1.75 and a == 1:
        print("General Weighted Average: " + str(gwa))
        print("Lister Status: Dean’s Lister")
    elif gwa > 1.75 and a == 1:
        print("General Weighted Average: " + str(gwa))
        print("Lister Status: Parent’s Lister")
    else:
        print("N/A")
    
#A loop for the program to keep running
while True:
    print(
          "1. Input_Number\n" +
          "2. Input_Word\n" +
          "3. Grading System\n" +
          "Type [End] to quit\n")

    selection = input("Enter Selection: ")
    
    print()
#The selection from the program
    {"1":InputNum,
     "2":InputWord,
     "3":Grading_System,
     "End":ending
    }[selection]()
    
    print()