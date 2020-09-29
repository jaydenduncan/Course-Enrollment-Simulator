"""
Title: Course Enrollment Simulation
Author: Jayden Duncan
Created: December 9, 2019
Description: This project will accept information from the user to label an enrollment page and then ask the user to input information for up to six
             different courses, which will be printed to the screen and a file for output.
Code Language: Python

"""




#This class will print the formatted heading to the top of the output screen
class firstPage:
    
    #a method of the firstPage class that has the job of printing the heading
    def print_firstPage(self):
        print("%100s"  %  "Jacksonville State University")#pushes the University name over 100 spaces to center it
        print("%94s" % "Fall Semester 2019")
        print("%88s" % "CS 230")
        print("%91s" % "Jayden Duncan")
        
#Instantiates the firstPage class, creating an object that can call the class's method
p = firstPage()
p.print_firstPage()

#the monthSwitch function performs a switch statement on the passed integer argument, returing the respective month
def monthSwitch(i):
    monthSwitcher = {
        1:'January',
        2:'February',
        3:'March',
        4:'April',
        5:'May',
        6:'June',
        7:'July',
        8:'August',
        9:'September',
        10:'October',
        11:'November',
        12:'December'
        }
    return monthSwitcher.get(i)

#initialized lists that will store a valid month, day, and year
monthList = []
dayList = []
yearList = []

#this function will accept a valid date from the user and store the month, day, and year in their respective list
def Date_Input():
    month = input("Enter number of month in two digts (Example: 01 for January): ")#prompts the user to enter the current month as an integer

    #nested if statements insert the correct month into its list, as the first element of the list
    if month == "01":
        monthList.insert(0,monthSwitch(1))
    elif month == "02":
        monthList.insert(0,monthSwitch(2))
    elif month == "03":
        monthList.insert(0,monthSwitch(3))
    elif month == "04":
        monthList.insert(0,monthSwitch(4))
    elif month == "05":
        monthList.insert(0,monthSwitch(5))
    elif month == "06":
        monthList.insert(0,monthSwitch(6))
    elif month == "07":
        monthList.insert(0,monthSwitch(7))
    elif month == "08":
        monthList.insert(0,monthSwitch(8))
    elif month == "09":
        monthList.insert(0,monthSwitch(9))
    elif month == "10":
        monthList.insert(0,monthSwitch(10))
    elif month == "11":
        monthList.insert(0,monthSwitch(11))
    elif month == "12":
        monthList.insert(0,monthSwitch(12))
    else:
        print("Invalid number of month")
        Date_Input()#recalls the Date_Input function if the entered month value is invalid
    day = input("Enter the day of the month (Example: 1 is the day of the month in the date, January 1, 2019): ")
    if day == "":
        print("Please enter the full date")
        Date_Input()
    year = input("Enter the year (Example: 2019 is the year in the date, January 1, 2019): ")
    if year == "":
        print("Please enter the full date")
        Date_Input()
    print("\nWhat you entered:","Day:",day,"|","Month:",month,"|","Year:",year)

    #Date_Validation makes sure what the user has entered is correct before moving through the rest of the program
    Date_Validation = input('If this is correct, type "Yes". If this is not correct, just type "No" or press the enter key: ')
    if Date_Validation == "Yes":
        dayList.insert(0,day)
        yearList.insert(0,year)
    elif Date_Validation == "yes":
        dayList.insert(0,day)
        yearList.insert(0,year)
    elif Date_Validation == "YES":
        dayList.insert(0,day)
        yearList.insert(0,year)
    elif Date_Validation == "No":
        print("\nRe-enter the date below.")
        Date_Input() #recalls the function if the date entered by the user is incorrect
    elif Date_Validation == "no":
        print("\nRe-enter the date below.")
        Date_Input()
    elif Date_Validation == "NO":
        print("\nRe-enter the date below.")
        Date_Input()
    elif Date_Validation == "":
        print("\nRe-enter the date below.")
        Date_Input()
    else:
        Date_Input()
Date_Input()#initial call to the Date_Input function


studentNumberList = []#stores a valid student id number

#this function accepts a valid student id number from the user to store in its list
def StudentNumber_Input():
        studentNumber = str(input("\nEnter your 9-digit Student Number: "))
        print("\nWhat you entered:",studentNumber)
        if studentNumber == "":
            studentNumber = "N/A" #default content for the student number
        else:
            pass
        SN_Validation = input('If this is correct, type "Yes". If this is not correct, just type "No" or press the enter key: ')
        if SN_Validation == "Yes":
            studentNumberList.insert(0,studentNumber)
        elif SN_Validation == "yes":
            studentNumberList.insert(0,studentNumber)
        elif SN_Validation == "YES":
            studentNumberList.insert(0,studentNumber)
        elif SN_Validation == "No":
            print("\nRe-enter your 9-digit Student Number below.")
            StudentNumber_Input() #recalls the function if the student number entered by the user is incorrect
        elif SN_Validation == "no":
            print("\nRe-enter your 9-digit Student Number below.")
            StudentNumber_Input()
        elif SN_Validation == "NO":
            print("\nRe-enter your 9-digit Student Number below.")
            StudentNumber_Input()
        elif SN_Validation == "":
            print("\nRe-enter your 9-digit Student Number below.")
            StudentNumber_Input()
        else:
            StudentNumber_Input()
StudentNumber_Input()#intial call to the previous function

#fileList1 holds information to be printed to a file
fileList1 = ["%86s\n%80s\n%78s" % ("Jacksonville State University","Fall Semester 2019","Class Schedule"),"\n\nDate:",dayList[0]," ",monthList[0]," ",
             yearList[0],"\n\nStudent Number:",studentNumberList[0]]
storeInfo = open("Student Info.txt", 'w')#opens a file in write mode
storeInfo.truncate(0)#erases the previous contents of the file
storeInfo.writelines(fileList1)#writes the information in the list to the appropriate file


#stores a valid name from the user
nameList = []

#this function accepts a valid first and last name from the user to store in its list
def Name_Input():
    lastName = input("\nEnter your last name: ")
    firstName = input("\nEnter your first name: ")
    print("\nWhat you entered:","\nLast Name-",lastName,"\nFirst Name-",firstName)
    if lastName == "":
        lastName = "N/A" #default content for the user's last name
    else:
        pass
    if firstName == "":
        firstName = "N/A"
    else:
        pass

    #checks for correct name information
    name_Validation = input('If this is correct, type "Yes". If this is not correct, just type "No" or press the enter key: ')
    if name_Validation == "Yes":
        nameList.insert(0,lastName)
        nameList.insert(1,firstName)
    elif name_Validation == "yes":
        nameList.insert(0,lastName)
        nameList.insert(1,firstName)
    elif name_Validation == "YES":
        nameList.insert(0,lastName)
        nameList.insert(1,firstName)
    elif name_Validation == "No":
        print("\nRe-enter your name below.")
        Name_Input() #recalls the function if the name entered by the user is incorrect
    elif name_Validation == "no":
        print("\nRe-enter your name below.")
        Name_Input()
    elif name_Validation == "NO":
        print("\nRe-enter your name below.")
        Name_Input()
    elif name_Validation == "":
        print("\nRe-enter your name below.")
        Name_Input()
    else:
        Name_Input()
Name_Input() #initial call to the Name_Input function

fileList2 = ["\n\nName:",nameList[1]," ",nameList[0]]
storeInfo.writelines(fileList2) #prints the name of the user to the file

#prints a list of valid majors for the user to enter
print("\nOptions for major: \nArt \nAccounting \nApplied Electronics Engineering \nApplied Manufacturing Engineering \nBiology \nBusiness Administration"
      "\nChemistry \nCommunication \nComputer Information Systems \nComputer Science \nComputer Systems and Software Design \nCounselor Education"
      "\nCriminal Justice \nDrama \nEarly Childhood Education \nEconomics \nGeneral Education \nElementary Education \nEmergency Management \nEnglish"
      "\nExercise Science & Wellness \nFamily & Consumer Sciences \nFinance \nForeign Languages \nGeography \nHistory \nIndustrial Leadership"
      "\nInstructional Leadership \nInstructional Technology \nIntegrated Studies \nLiberal Studies \nLibrary Media \nManagement \nMarketing \nMathematics"
      "\nMusic \nNursing \nManufacturing Systems Technology \nOccupational Safety & Health Management \nPhysical Education \nPolitical Science"
      "\nPsychology \nPublic Administration \nReading Specialist \nRespiratory Therapy \nSecondary Education \nSocial Work \nSociology \nSpecial Education"
      "\nSport Management \nSport Management & Recreation Studies \nTeacher Leader")

#stores a valid major from the user
majorList = []

#this function accepts a valid major from the user to store into its list
def Major_Input():
    major = input("Enter one of the majors above: ")
    print("\nWhat you entered:",major)
    if major == "":
        major = "N/A"
    else:
        pass

    #makes sure that the major the user entered is correct
    major_Validation = input('If this is correct, type "Yes". If this is not correct, just type "No" or press the enter key: ')
    if major_Validation == "Yes":
        majorList.insert(0,major)
    elif major_Validation == "yes":
        majorList.insert(0,major)
    elif major_Validation == "YES":
        majorList.insert(0,major)
    elif major_Validation == "No":
        print("\nRe-enter your major below.")
        Major_Input() #recalls the function if the major entered by the user is incorrect
    elif major_Validation == "no":
        print("\nRe-enter your major below.")
        Major_Input()
    elif major_Validation == "NO":
        print("\nRe-enter your major below.")
        Major_Input()
    elif major_Validation == "":
        print("\nRe-enter your major below.")
        Major_Input()
    else:
        Major_Input()
Major_Input() #initial call to the Major_Input function


#stores the first and last name of the advisor into its respective list
advisorLastNameList = []
advisorFirstNameList = []

#this while loop loops through the statements until the user enters the first and last name of their advisor
while True:
    advisorFirstName = input("\nEnter the first name of the advisor for your major. (If you do not know who your advisor is, enter 'N/A' for now.): ")
    advisorFirstNameList.insert(0,advisorFirstName)
    advisorLastName = input("\nEnter the last name of the advisor for your major. (If you do not know who your advisor is, enter 'N/A' for now.): ")
    if advisorLastName == "": #checks if the user enters nothing for the last name
        print("Please enter the full name or enter 'N/A'.")
        pass
    else:
        advisorLastNameList.insert(0,advisorLastName)
        break

fileList3 = ["\n\nMajor:",majorList[0],"\n\nAdvisor:",advisorFirstNameList[0]," ",advisorLastNameList[0]]
storeInfo.writelines(fileList3) #prints the major and advisor name of the user to the screen

print("\nEnter 6 courses. If you have less than 6 courses and are done, press the enter key for other entries and enter '0' for the course hours.")
totalCourseList = [] #list to store all of the user's courses in

#stores the course 1 string data and number of course hours in their respective list
course1List = []
course1_hoursList = []

#this function accepts information about course number 1
def Course1_Input():
    print("\nCourse 1")
    course1_abbr = input("Enter course abbreviation (Example- MS is the abbreviation for MS 125): ")                                                                                                                                                
    if course1_abbr == "":
        course1_abbr = "N/A"
        course1List.insert(0,course1_abbr)
    else:
        course1List.insert(0,course1_abbr)
    course1_courseNumber = input("Enter the course number (Example- 125 is the course number for MS 125): ")
    if course1_courseNumber == "":
        course1_courseNumber = "N/A"
        course1List.insert(1,course1_courseNumber)
    else:
        course1List.insert(1,course1_courseNumber)
    course1_Section = input("Enter the course section (Example- 004 is the section number for MS 125 004): ")
    if course1_Section == "":
        course1_Section = "N/A"
        course1List.insert(2,course1_Section)
    else:
        course1List.insert(2,course1_Section)
    course1_hours = input("Enter the number of course hours: ")
    if course1_hours == "":
        print("You have to enter a number of hours. Please try again. Hint: If you are done entering courses please enter '0' for this entry.")
        Course1_Input()
    else:
        course1_hoursList.insert(0,course1_hours)
    course1_Title = input("Enter the course title: ")
    if course1_Title == "":
        course1_Title = "N/A"
        course1List.insert(3,course1_Title)
    else:
        course1List.insert(3,course1_Title)
    print("\nWhat you entered:",course1_abbr,"|",course1_courseNumber,"|",course1_Section,"|",float(course1_hours),"Hours","|",course1_Title)
    course1_Validation = input('If this is correct, type "Yes". If this is not correct, just type "No" or press the enter key: ')
    if course1_Validation == "Yes":
        if course1_Title == "N/A":
            pass
        else:
            totalCourseList.append(course1_Title)
            pass
    elif course1_Validation == "yes":
        if course1_Title == "N/A":
            pass
        else:
            totalCourseList.append(course1_Title)
            pass
    elif course1_Validation == "YES":
        if course1_Title == "N/A":
            pass
        else:
            totalCourseList.append(course1_Title)
            pass
    elif course1_Validation == "No":
        print("\nRe-enter Course 1 below.")
        Course1_Input()
    elif course1_Validation == "no":
        print("\nRe-enter Course 1 below.")
        Course1_Input()
    elif course1_Validation == "NO":
        print("\nRe-enter Course 1 below.")
        Course1_Input()
    elif course1_Validation == "":
        print("\nRe-enter Course 1 below.")
        Course1_Input()
    else:
        Course1_Input()
Course1_Input() #initial call to the Course1_Input function


#stores the course 2 string data and number of course hours in their respective list
course2List = []
course2_hoursList = []

#accepts information about course number 2
def Course2_Input():
    print("\nCourse 2")
    course2_abbr = input("Enter course abbreviation (Example- MS is the abbreviation for MS 125): ")                                                                                                                                                
    if course2_abbr == "":
        course2_abbr = "N/A"
        course2List.insert(0,course2_abbr)
    else:
        course2List.insert(0,course2_abbr)
    course2_courseNumber = input("Enter the course number (Example- 125 is the course number for MS 125): ")
    if course2_courseNumber == "":
        course2_courseNumber = "N/A"
        course2List.insert(1,course2_courseNumber)
    else:
        course2List.insert(1,course2_courseNumber)
    course2_Section = input("Enter the course section (Example- 004 is the section number for MS 125 004): ")
    if course2_Section == "":
        course2_Section = "N/A"
        course2List.insert(2,course2_Section)
    else:
        course2List.insert(2,course2_Section)
    course2_hours = input("Enter the course hours: ")
    if course2_hours == "":
        print("You have to enter a number of hours. Please try again. Hint: If you are done entering courses please enter '0' for this entry.")
        Course2_Input()
    else:
        course2_hoursList.insert(0,course2_hours)
    course2_Title = input("Enter the course title: ")
    if course2_Title == "":
        course2_Title = "N/A"
        course2List.insert(3,course2_Title)
    else:
        course2List.insert(3,course2_Title)
    print("\nWhat you entered:",course2_abbr,"|",course2_courseNumber,"|",course2_Section,"|",float(course2_hours),"Hours","|",course2_Title)
    course2_Validation = input('If this is correct, type "Yes". If this is not correct, just type "No" or press the enter key: ')
    if course2_Validation == "Yes":
        if course2_Title == "N/A":
            pass
        else:
            totalCourseList.append(course2_Title)
            pass
    elif course2_Validation == "yes":
        if course2_Title == "N/A":
            pass
        else:
            totalCourseList.append(course2_Title)
            pass
    elif course2_Validation == "YES":
        if course2_Title == "N/A":
            pass
        else:
            totalCourseList.append(course2_Title)
            pass
    elif course2_Validation == "No":
        print("\nRe-enter Course 2 below.")
        Course2_Input()
    elif course2_Validation == "no":
        print("\nRe-enter Course 2 below.")
        Course2_Input()
    elif course2_Validation == "NO":
        print("\nRe-enter Course 2 below.")
        Course2_Input()
    elif course2_Validation == "":
        print("\nRe-enter Course 2 below.")
        Course2_Input()
    else:
        Course2_Input()
Course2_Input() #initial call to the Course2_Input function


#stores the course 3 string data and number of course hours in their respective list
course3List = []
course3_hoursList = []

#accepts information about course number 3
def Course3_Input():
    print("\nCourse 3")
    course3_abbr = input("Enter course abbreviation (Example- MS is the abbreviation for MS 125): ")                                                                                                                                                
    if course3_abbr == "":
        course3_abbr = "N/A"
        course3List.insert(0,course3_abbr)
    else:
        course3List.insert(0,course3_abbr)
    course3_courseNumber = input("Enter the course number (Example- 125 is the course number for MS 125): ")
    if course3_courseNumber == "":
        course3_courseNumber = "N/A"
        course3List.insert(1,course3_courseNumber)
    else:
        course3List.insert(1,course3_courseNumber)
    course3_Section = input("Enter the course section (Example- 004 is the section number for MS 125 004): ")
    if course3_Section == "":
        course3_Section = "N/A"
        course3List.insert(2,course3_Section)
    else:
        course3List.insert(2,course3_Section)
    course3_hours = input("Enter the course hours: ")
    if course3_hours == "":
        print("You have to enter a number of hours. Please try again. Hint: If you are done entering courses please enter '0' for this entry.")
        Course3_Input()
    else:
        course3_hoursList.insert(0,course3_hours)
    course3_Title = input("Enter the course title: ")
    if course3_Title == "":
        course3_Title = "N/A"
        course3List.insert(3,course3_Title)
    else:
        course3List.insert(3,course3_Title)
    print("\nWhat you entered:",course3_abbr,"|",course3_courseNumber,"|",course3_Section,"|",float(course3_hours),"Hours","|",course3_Title)
    course3_Validation = input('If this is correct, type "Yes". If this is not correct, just type "No" or press the enter key: ')
    if course3_Validation == "Yes":
        if course3_Title == "N/A":
            pass
        else:
            totalCourseList.append(course3_Title)
            pass
    elif course3_Validation == "yes":
        if course3_Title == "N/A":
            pass
        else:
            totalCourseList.append(course3_Title)
            pass
    elif course3_Validation == "YES":
        if course3_Title == "N/A":
            pass
        else:
            totalCourseList.append(course3_Title)
            pass
    elif course3_Validation == "No":
        print("\nRe-enter Course 3 below.")
        Course3_Input()
    elif course3_Validation == "no":
        print("\nRe-enter Course 3 below.")
        Course3_Input()
    elif course3_Validation == "NO":
        print("\nRe-enter Course 3 below.")
        Course3_Input()
    elif course3_Validation == "":
        print("\nRe-enter Course 3 below.")
        Course3_Input()
    else:
        Course3_Input()
Course3_Input() #initial call to the Course3_Input function


#stores the course 4 string data and number of course hours in their respective list
course4List = []
course4_hoursList = []

#accepts information about course number 4
def Course4_Input():
    print("\nCourse 4")
    course4_abbr = input("Enter course abbreviation (Example- MS is the abbreviation for MS 125): ")                                                                                                                                                
    if course4_abbr == "":
        course4_abbr = "N/A"
        course4List.insert(0,course4_abbr)
    else:
        course4List.insert(0,course4_abbr)
    course4_courseNumber = input("Enter the course number (Example- 125 is the course number for MS 125): ")
    if course4_courseNumber == "":
        course4_courseNumber = "N/A"
        course4List.insert(1,course4_courseNumber)
    else:
        course4List.insert(1,course4_courseNumber)
    course4_Section = input("Enter the course section (Example- 004 is the section number for MS 125 004): ")
    if course4_Section == "":
        course4_Section = "N/A"
        course4List.insert(2,course4_Section)
    else:
        course4List.insert(2,course4_Section)
    course4_hours = input("Enter the course hours: ")
    if course4_hours == "":
        print("You have to enter a number of hours. Please try again. Hint: If you are done entering courses please enter '0' for this entry.")
        Course4_Input()
    else:
        course4_hoursList.insert(0,course4_hours)
    course4_Title = input("Enter the course title: ")
    if course4_Title == "":
        course4_Title = "N/A"
        course4List.insert(3,course4_Title)
    else:
        course4List.insert(3,course4_Title)
    print("\nWhat you entered:",course4_abbr,"|",course4_courseNumber,"|",course4_Section,"|",float(course4_hours),"Hours","|",course4_Title)
    course4_Validation = input('If this is correct, type "Yes". If this is not correct, just type "No" or press the enter key: ')
    if course4_Validation == "Yes":
        if course4_Title == "N/A":
            pass
        else:
            totalCourseList.append(course4_Title)
            pass
    elif course4_Validation == "yes":
        if course4_Title == "N/A":
            pass
        else:
            totalCourseList.append(course4_Title)
            pass
    elif course4_Validation == "YES":
        if course4_Title == "N/A":
            pass
        else:
            totalCourseList.append(course4_Title)
            pass
    elif course4_Validation == "No":
        print("\nRe-enter Course 4 below.")
        Course4_Input()
    elif course4_Validation == "no":
        print("\nRe-enter Course 4 below.")
        Course4_Input()
    elif course4_Validation == "NO":
        print("\nRe-enter Course 4 below.")
        Course4_Input()
    elif course4_Validation == "":
        print("\nRe-enter Course 4 below.")
        Course4_Input()
    else:
        Course4_Input()
Course4_Input() #initial call to the Course4_Input function


#stores the course 5 string data and number of course hours in their respective list
course5List = []
course5_hoursList = []

#accepts information about course number 5
def Course5_Input():
    print("\nCourse 5")
    course5_abbr = input("Enter course abbreviation (Example- MS is the abbreviation for MS 125): ")                                                                                                                                                
    if course5_abbr == "":
        course5_abbr = "N/A"
        course5List.insert(0,course5_abbr)
    else:
        course5List.insert(0,course5_abbr)
    course5_courseNumber = input("Enter the course number (Example- 125 is the course number for MS 125): ")
    if course5_courseNumber == "":
        course5_courseNumber = "N/A"
        course5List.insert(1,course5_courseNumber)
    else:
        course5List.insert(1,course5_courseNumber)
    course5_Section = input("Enter the course section (Example- 004 is the section number for MS 125 004): ")
    if course5_Section == "":
        course5_Section = "N/A"
        course5List.insert(2,course5_Section)
    else:
        course5List.insert(2,course5_Section)
    course5_hours = input("Enter the course hours: ")
    if course5_hours == "":
        print("You have to enter a number of hours. Please try again. Hint: If you are done entering courses please enter '0' for this entry.")
        Course5_Input()
    else:
        course5_hoursList.insert(0,course5_hours)
    course5_Title = input("Enter the course title: ")
    if course5_Title == "":
        course5_Title = "N/A"
        course5List.insert(3,course5_Title)
    else:
        course5List.insert(3,course5_Title)
    print("\nWhat you entered:",course5_abbr,"|",course5_courseNumber,"|",course5_Section,"|",float(course5_hours),"Hours","|",course5_Title)
    course5_Validation = input('If this is correct, type "Yes". If this is not correct, just type "No" or press the enter key: ')
    if course5_Validation == "Yes":
        if course5_Title == "N/A":
            pass
        else:
            totalCourseList.append(course5_Title)
            pass
    elif course5_Validation == "yes":
        if course5_Title == "N/A":
            pass
        else:
            totalCourseList.append(course5_Title)
            pass
    elif course5_Validation == "YES":
        if course5_Title == "N/A":
            pass
        else:
            totalCourseList.append(course5_Title)
            pass
    elif course5_Validation == "No":
        print("\nRe-enter Course 5 below.")
        Course5_Input()
    elif course5_Validation == "no":
        print("\nRe-enter Course 5 below.")
        Course5_Input()
    elif course5_Validation == "NO":
        print("\nRe-enter Course 5 below.")
        Course5_Input()
    elif course5_Validation == "":
        print("\nRe-enter Course 5 below.")
        Course5_Input()
    else:
        Course5_Input()
Course5_Input() #initial call to the Course5_Input function


#stores the course 6 string data and number of course hours in their respective list
course6List = []
course6_hoursList = []

#accepts information about course number 5
def Course6_Input():
    print("\nCourse 6")
    course6_abbr = input("Enter course abbreviation (Example- MS is the abbreviation for MS 125): ")                                                                                                                                                
    if course6_abbr == "":
        course6_abbr = "N/A"
        course6List.insert(0,course6_abbr)
    else:
        course6List.insert(0,course6_abbr)
    course6_courseNumber = input("Enter the course number (Example- 125 is the course number for MS 125): ")
    if course6_courseNumber == "":
        course6_courseNumber = "N/A"
        course6List.insert(1,course6_courseNumber)
    else:
        course6List.insert(1,course6_courseNumber)
    course6_Section = input("Enter the course section (Example- 004 is the section number for MS 125 004): ")
    if course6_Section == "":
        course6_Section = "N/A"
        course6List.insert(2,course6_Section)
    else:
        course6List.insert(2,course6_Section)
    course6_hours = input("Enter the course hours: ")
    if course6_hours == "":
        print("You must enter a number of hours. Please try again. Hint: If you are done entering courses please enter '0' for this entry.")
        Course6_Input()
    else:
        course6_hoursList.insert(0,course6_hours)
    course6_Title = input("Enter the course title: ")
    if course6_Title == "":
        course6_Title = "N/A"
        course6List.insert(3,course6_Title)
    else:
        course6List.insert(3,course6_Title)
    print("\nWhat you entered:",course6_abbr,"|",course6_courseNumber,"|",course6_Section,"|",float(course6_hours),"Hours","|",course6_Title)
    course6_Validation = input('If this is correct, type "Yes". If this is not correct, just type "No" or press the enter key: ')
    if course6_Validation == "Yes":
        if course6_Title == "N/A":
            pass
        else:
            totalCourseList.append(course6_Title)
            pass
    elif course6_Validation == "yes":
        if course6_Title == "N/A":
            pass
        else:
            totalCourseList.append(course6_Title)
            pass
    elif course6_Validation == "YES":
        if course6_Title == "N/A":
            pass
        else:
            totalCourseList.append(course6_Title)
            pass
    elif course6_Validation == "No":
        print("\nRe-enter Course 6 below.")
        Course6_Input()
    elif course6_Validation == "no":
        print("\nRe-enter Course 6 below.")
        Course6_Input()
    elif course6_Validation == "NO":
        print("\nRe-enter Course 6 below.")
        Course6_Input()
    elif course6_Validation == "":
        print("\nRe-enter Course 6 below.")
        Course6_Input()
    else:
        Course6_Input()
Course6_Input() #initial call to the Course6_Input function

#intializes a count variable to 0 and loops through the totalCourseList to count the number of courses the user entered
count = 0
for courses in totalCourseList:
    count += 1

#prints the all the information the user entered, using the valid content that was stored in the previous lists
print("\nSTUDENT INFORMATION")
print("\nDate: ",dayList[0],monthList[0],yearList[0])
print("\nStudent Number: " , studentNumberList[0])
print("\nName: " ,nameList[0], ",", nameList[1])
print("\nMajor: " + majorList[0])
print("\nHere are your",count,"courses:")

print("\nCourse 1:",course1List[0],course1List[1],course1List[2],course1List[3])
print("\nCourse 2:",course2List[0],course2List[1],course2List[2],course2List[3])
print("\nCourse 3:",course3List[0],course3List[1],course3List[2],course3List[3])
print("\nCourse 4:",course4List[0],course4List[1],course4List[2],course4List[3])
print("\nCourse 5:",course5List[0],course5List[1],course5List[2],course5List[3])
print("\nCourse 6:",course6List[0],course6List[1],course6List[2],course6List[3])


#conversion of the course data to a string for output
course1Abb = str(course1List[0])
course1CrsNum = str(course1List[1])
course1Section = str(course1List[2])
course1Title = str(course1List[3])
course2Abb = str(course2List[0])
course2CrsNum = str(course2List[1])
course2Section = str(course2List[2])
course2Title = str(course2List[3])
course3Abb = str(course3List[0])
course3CrsNum = str(course3List[1])
course3Section = str(course3List[2])
course3Title = str(course3List[3])
course4Abb = str(course4List[0])
course4CrsNum = str(course4List[1])
course4Section = str(course4List[2])
course4Title = str(course4List[3])
course5Abb = str(course5List[0])
course5CrsNum = str(course5List[1])
course5Section = str(course5List[2])
course5Title = str(course5List[3])
course6Abb = str(course6List[0])
course6CrsNum = str(course6List[1])
course6Section = str(course6List[2])
course6Title = str(course6List[3])

#adds the total number of course hours that were stored in a list
totalCourseHours = int(int(course1_hoursList[0]) + int(course2_hoursList[0]) + int(course3_hoursList[0]) + int(course4_hoursList[0]) +
                       int(course5_hoursList[0]) + int(course6_hoursList[0]))
formatedCourseHours = float("%0.2f" % (totalCourseHours)) #formats the course hours to 2 decimal places
print("\nTotal Hours:",formatedCourseHours)
fileCourseHours = str(formatedCourseHours) #converts the course hours to a string for file output


#stores formatted course information into a list for file output (formatted for spacing purposes)
fileList4 = ["\n\n%-10s%-4s%-4s%-4s%-70s" % ("Course 1:",course1Abb,course1CrsNum,course1Section,course1Title),"%-10s%-4s%-4s%-4s%-40s" % ("Course 2:",
             course2Abb,course2CrsNum,course2Section,course2Title),
             "\n\n%-10s%-4s%-4s%-4s%-70s" % ("Course 3:",course3Abb,course3CrsNum,course3Section,course3Title),"%-10s%-4s%-4s%-4s%-40s" % ("Course 4:",
             course4Abb,course4CrsNum,course4Section,course4Title),
             "\n\n%-10s%-4s%-4s%-4s%-70s" % ("Course 5:",course5Abb,course5CrsNum,course5Section,course5Title),"%-10s%-4s%-4s%-4s%-40s" % ("Course 6:",
             course6Abb,course6CrsNum,course6Section,course6Title),"\n\n%75s" % "Total Hours:",fileCourseHours]
storeInfo.writelines(fileList4) #writes the course contents to the file
storeInfo.close() #closes the file

printInfo = open("Student Info.txt", 'r') #opens the same file in read mode
schoolInformation = printInfo.read() #reads the contents of the file
print(schoolInformation) #prints all the contents of the file to the console screen

printInfo.close() #closes the file again

"""SUMMARY: The class, firstPage, will print out the four-line heading for this application. The function, monthSwitch, contains a switch statement that
    contains a dictionary of the months of the year for when they need to be called from the Date_Input function. The StudentNumber_Input function
    will accept the student's student number and store it in a list and output file. The Major_Input function will accept the student's major and store it in
    a list and output file as well, followed by the while loop which will accept the advisor name and store it. The course input functions will accept
    the student's course information and also validate those courses before storing the information in their respective lists and writing it to the output
    file called 'Student Info'. At the end of the application, the 'Student Info' file will be read and the contents on the file will be printed."""

end_program = input("Thanks for using the Course Enrollment Simulator! Press the enter key to end the program: ")
#waits for the user to press the enter key to end the program
    
