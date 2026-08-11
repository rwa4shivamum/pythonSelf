def factorial(num):
    if(num == 1):
        return 1
    return num*factorial(num-1)

filterData = lambda lst, thresoldValue: [ i for i in lst if i > thresoldValue]
              
              
def sortFunction(lst,choice):
    if choice==1:
        lst.sort()
    else:
        lst.sort(reverse=True)
    return lst


print("Welcome to Data Analyzer and Transformer Program")
while True:
    print('''
          Main Menu:
          1.Input Data
          2.Display Data Summary (Built-in Functions)
          3.Calculate Factorial (Recusrion)
          4.Filter Data by Threshold (Lambda Function)
          5.Sort Data
          6.Display Dataset Statistics (return Multiple Values)
          7.Exit Program
          ''')
    choiceOfInput = int(input("Enter your Chice: "))
    match choiceOfInput:
        case 1:
            global inputOfNum
            inputOfNum = input("Enter data for 1D array separate by spaces").split(" ")
            inputOfNum = [int(i) for i in inputOfNum] 
            print("Data has been stored successfully!")
        case 2:
            print(f'''Data Summary
                  - Total element: {len(inputOfNum)}
                  - Minimum Value: {min(inputOfNum)}
                  - Maximum Value: {max(inputOfNum)}
                  - Sum of all Values: {sum(inputOfNum)}
                  - Average of all Value: {sum(inputOfNum)/len(inputOfNum)}''')
        case 3:
            inputNumOfFact = int(input("Enter the num of Factorial: "))
            factofNumb = factorial(inputNumOfFact)
            print(f'Factorial of {inputNumOfFact} is: {factofNumb}')
        case 4:
            thresoldValue = int(input("Enter a Thresold value"))
            thresoldOp = filterData(inputOfNum,thresoldValue)
            print(f"Filter Data (values >= {thresoldValue}): {thresoldOp}")
        case 5:
            print('''
                  Choose Sortign Option:
                  1.Ascending
                  2.Descending''')
            inputOfChice = int(input("Enter your Choice: "))
            sortFunction(inputOfNum,inputOfChice)
            print(f"Sorted Data in {"Ascending" if inputOfChice == 1 else "Descending"} Order: {inputOfNum}")
        case 6:
            print(f'''
                  Dataset Statistics:
                  - Minimum value: {min(inputOfNum)}
                  - Maximum value: {max(inputOfNum)}
                  - Sum of All values: {sum(inputOfNum)}
                  - Average of Value: {sum(inputOfNum)/len(inputOfNum)}
                  ''')
        case 7:
            print("Thank you for using Data Analyzer and Transformer Program. Goodby!")
            break