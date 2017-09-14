## Team JE: Eugene Thomas and Joyce Wu 
## SoftDev1 pd7
## HW02 -- NO-body expects the Spanish Inquisition!
## 2017-09-13


import random #You must import the random module to generate a number that will randomly select 
	
def student_picker (x):
    CLASSES = {
        7: [ 'Helen', 'Shakil', 'Eric', 'Jennifer Y', 'Jennifer Z', 'Arif', 'Queenie', 'Jawadul', 'Shaina', 'Vivien', 'Brian', 'Naotaka', 'Bayan', 'Adam', 'Caleb', 'Terry', 'Jason', 'Alessandro', 'Samantha', 'Carol', 'Joyce', 'Shannon', 'Charles', 'Taylor', 'Kelly', 'Leo', 'Khyber', 'Ibnul', 'Eugene', 'Yuyang', 'Karina', 'Tiffany', 'Holden', 'Michael'],
        8: ['Masha', 'Adrian', 'David', 'Eric', 'Josh', 'Jerome', 'Henry', 'Jackie', 'Giorgio', 'Karen', 'Sonal', 'Xavier', 'Bermet', 'Alex', 'Iris', 'Manahal', 'Donia', 'Md', 'Connie', 'Lisa', 'Xing', 'Angelica', 'Angel', 'Augie', 'Dimitriy', 'Yiduo', 'Gordon', 'Tiffany', 'Clive', 'Jonathan', 'Sasha', 'Daniel'],
        9: [ 'Yu Qi', 'Michela', 'Kristin', 'Fabiha', 'Maxim', 'Marcus', 'Ish', 'James', 'Ryan', 'Edward', 'Adeeb', 'Jake', 'Cynthia', 'Kevin', 'Levi', 'Edmond', 'Kyle', 'Andrew', 'Max', 'Jenny', 'Philip', 'Shan', 'Mansour', 'Ray', 'Jake', 'Ida', 'Kerry', 'Stanley', 'Jackie', 'William', 'Tina', 'Michael']
    }
    try: 
        class_list = CLASSES[x] # Gives the list coordinating to the inputted number 
    except:
        return 'Wrong period, no people found.' # If the number is not 7, 8, or 9. 
    student = class_list[random.randint(0,len(class_list)-1)] # In python, randint(a,b) means it chooses a number N such that a <= N <= b (unlike java, both are inclusive).
    return student

repeat = True 
while repeat == True: 
    period = int(raw_input('Pick a Software Development Period (7, 8, or 9) '))
    print student_picker(period)
    confirmationLoop = True
    while confirmationLoop == True: 
        confirmation = int(raw_input('Do you wanna do it again? 0 for no, 1 for yes '))
        if confirmation == 0:
            repeat = False 
            break
        elif confirmation == 1:
            break
            
