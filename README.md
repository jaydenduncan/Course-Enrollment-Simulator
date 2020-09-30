# Course-Enrollment-Simulator
This project accepts student and course information from the user and prints the information to a file as well as the console screen.

## Table of Contents
* [Project Info](#project-info)
  * [User Input](#user-input)
  * [Console Output](#console-output)
  * [File Output](#file-output)
* [Usage](#usage)

## Project Info
In this course enrollment simulation, a four-line heading will be printed out to the screen using a class. A function containing a switch statement with a dictionary of the months of the year is provided for use in the Date_Input function. Another function will accept the user's student ID number and store it in a list to be written to a file. A function for accepting the major of the user is also provided, which stores the major in a list to be written to the file along with the student ID. Similar functions are provided to accept the user's name and the name of the advisor, which are also stored in a list and written to the file. More functions are given to accept and store course information input by the user. At the end of the program, all the contents of the file will be read and printed to the console screen.

### User Input
Throughout the program, the user is asked to provide input for various information. 
This information includes: 
* Date
* Student ID Number
* Student's Name
* Major
* Advisor's Name
* Course Information (Title, Credit Hours, etc.)
* Validation Input

In Python, user input is requested using a combination of the print and input functions:
```
print(input("Some prompt for input": ))
```
After the user enters information following an input prompt, that input is checked for validation using if-else and nested if statements.
In if-else statements, the statements within the 'if' block are performed only if the condition is true, or else the statements within the 'else' block are performed:
```
if 'condition':
  do these statements
else:
  do these statements instead
```
In nested if statements or 'elif' statements, a series of if statements are performed until an if statement is found to be true, or else the 'else' statement will be performed:
```
if 'condition':
  do these statements
elif:
  do these statements
...
else:
  do these statements instead
```
After the user's input is validated, the correct information is stored into the first index of a list. The lists in the project are initialized first and the correct information from the user is inserted into the beginning of the list by putting a 0 for the index and the specific element:
```
list = []
list.insert(index, element)
```
All this information is either used to calculate a total or print for output at the end of the program.

### Console Output
The information that was stored in the course information lists contains all of the attempted inputs from the user, but for each list the correct input is placed as the first element in the list. Another list contains all of the course titles, which is counted at the end of the program. The course hours for each course are also summed together and formatted as a floating point number. All course information is printed to the console screen using the print function. 

### File Output
In order to write the contents of the user's input to a file, the information was placed into different file lists. After opening the file using the open function, contents that may have already been in the file are erased using the truncate function:
```
f = open("filename", 'file mode')
f.truncate(0)
```
After previous content is erased, the file is ready for new output, which in terms of this project would be the student and course information. After placing the content that's gonna be displayed in the file into a file list, the writelines function can now be used to output the information to the file:
```
file_list = ["Some information...", "abc", "def"]
f.writelines(file_list)
```
The file is closed using the close function after it's modifications are complete:
```
f.close()
```

## Usage
This course enrollment project can be downloaded and ran using any any IDE compatible with Python. Some Python IDE's include:
* IDLE
* PyCharm
* Spyder
* PyDev
* Visual Studio for Python

To run this program, click 'run' at the top of the screen:
![Run the Program](C:\Users\jayde\OneDrive\Pictures\Screenshots\Github1.jpg)
