# Course-Enrollment-Simulator
This project accepts student and course information from the user and prints the information to a file as well as the console screen.

## Table of Contents
* [Project Info](#project-info)
  * [User Input](#user-input)
  * [Console Output](#console-output)
  * [File Output](#file-output)
* [Installation](#installation)
  * [Linux](#linux) 
  * [Windows](#windows)
  * [Macintosh](#macintosh)
* [Usage](#usage)
* [Contribution](#contribution)
* [License](#license)

---

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
After previous content is erased, the file is ready for new output, which in terms of this project would be the student and course information. After placing the content that's going to be displayed in the file into a file list, the writelines function can now be used to output the information to the file:
```
file_list = ["Some information...", "abc", "def"]
f.writelines(file_list)
```
The file is closed using the close function after it's modifications are complete:
```
f.close()
```

---

## Installation
The following are instructions for installing Python for three different platforms. More information about the setup and installation of Python across different platforms can be accessed from the [Python Setup and Usage](https://docs.python.org/release/3.8.5/using/index.html) section of the [Python website](https://www.python.org).
### Linux
* FreeBSD users add the Python package using the following command:
  ```
  pkg install python3
  ```
* OpenBSD users add the Python package using these commands:
  ```
  pkg_add -r python
  pkg_add ftp://ftp.openbsd.org/pub/OpenBSD/4.2/packages/<insert your architecture here>/python-<version>.tgz
  ```
### Windows
Find a link to install a Python release from the [Python website](https://www.python.org/download/releases/). Python 3.8 is recommended for Windows Vista or newer. Python 3.4 is recommended for Windows XP.
To install Python from Windows:
1. Click a link from the website to start the installer.
2. Select 'Install Now' or 'Customize installation'.

   To silently install a default, system-wide Python installation:
   ```
   python-3.8.0.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
   ```
### Macintosh
Users of Mac OS X 10.8 have Python 2.7 preinstalled. However, the recent version of Python 3 may be installed from the [Python Website](https://www.python.org) if the user wishes to do so. A Python 3.8 folder is provided after installing a newer version of Python. A framework is also provided:
```
/Library/Frameworks/Python.framework
```

## Usage
To clone a repository on Github:
1. Under repository name, click 'Clone or Download'.
2. Copy the clone URL in the 'Clone with HTTPs' section.
3. Open Git Bash and change the current working directory to the location you want it to be in.
4. Type 'git clone' followed by the URL and then press **Enter**:
   ```
   $ git clone https://hostname/USERNAME/REPOSITORY
   ``` 
For more information on cloning for Github, review the website for [Github Docs](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

This project may be run using the IDLE IDE. Other Python IDE's include:
* IDLE
* PyCharm
* Spyder
* PyDev
* Visual Studio for Python

To run this program, click 'run' at the top of the screen:
![Image1](https://user-images.githubusercontent.com/71575315/94645312-22b9c900-02b1-11eb-94be-77894bdd3ca6.jpg)

Click 'Run Module' under 'Run':
![Image2](https://user-images.githubusercontent.com/71575315/94645875-8b557580-02b2-11eb-8f34-d9f62d5c8258.png)

For information on how the project works, refer to the [Project Info](#project-info) section seen earlier in this README.md file.

## Contribution
Pull requests are always welcome!

## License
[![Github license](https://img.shields.io/github/license/jaydenduncan/Course-Enrollment-Simulator)](https://github.com/jaydenduncan/Course-Enrollment-Simulator/blob/master/LICENSE)

Licensed under the [MIT License](https://opensource.org/licenses/MIT)
