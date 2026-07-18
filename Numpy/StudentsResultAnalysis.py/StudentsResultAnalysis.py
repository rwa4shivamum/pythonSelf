import numpy as np

marks = np.array([45, 67, 89, 32, 76, 50, 91, 38, 60, 72])

#Basic Analysis
totalMarks = np.sum(marks)
averageMarks = np.average(marks)
highestMarks = np.max(marks)
lowestMarks = np.min(marks)
print("Baisc Analtsis------------>",totalMarks,averageMarks,lowestMarks, highestMarks)


#filtering
passedStudents = marks[marks > 50]
failedStudent = marks[marks < 50]
print("filtering students------------->>",passedStudents,failedStudent)

#grading System


#sorting
sortAscending = np.sort(marks)
sortDesceinding = np.sort(marks)[::-1]
print("sotging -------------->>",sortAscending,sortDesceinding)

#step 6: statistics
meanOfStudents = np.mean(marks)
medianOfStudents = np.median(marks)
standardDeviation = np.std(marks)

print("statistics----------------------->>",meanOfStudents,medianOfStudents,standardDeviation)

