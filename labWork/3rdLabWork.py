print("Welcome to students Dashboard")

print("""Select an option
1.Add Students
2.Display All Students
3.Update Students information
4.Delete Students
5.Display Subjects Offered
6.Exit""")
selectOption = int(input("Enter a option:"))


listOfStudents = []
tupleofStudentId = ()
tupleOfStudentDob = ()
setOfUniqueSubject = set()

for i in range(0,12):
    if selectOption==1:
    studentId = int(input("Enter student ID:"))
    name = input("Enter the Student Name:")
    age = int(input("Enter the Age"))
    grade = input("Enter the grade")
    dateOfBirth = input("Enter DOB YYYY-MM-DD")
    subject = input("Enter subject by comma Seprated:").split(",")

    #Add studentId By adding new Tuple
    tupleofStudentId = tupleofStudentId + (studentId,)
    tupleOfStudentDob = tupleOfStudentDob + (dateOfBirth,)

    #Add subjects of unique
    setOfUniqueSubject.update(subject)

    # Create dictionary of students details
    dictionaryOfSingleStudent = {
        "studentId":studentId,
        "studentName":name,
        "studentAge":age,
        "studentGrade":grade,
        "dateOfBirth":dateOfBirth,
        "subject":subject
    }
    listOfStudents.append(dictionaryOfSingleStudent)
elif(selectOption == 2):
    for i in listOfStudents:
        print(i)
elif(selectOption == 3):
    print("Here")