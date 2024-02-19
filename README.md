# GradePoint Pro - GPA Calculator
GradePoint Pro is a simple GPA calculator application built using the Tkinter library in Python. It allows users to calculate both unweighted and weighted GPAs based on their course grades and credit units.
# Prerequisites
- Download the latest version of python through (https://www.python.org/downloads/) for Windows or MacOS depending on the system being used. You also need an IDE (recommended VScode) to download that use (https://code.visualstudio.com/)
- Before you run the program, you must type the command "pip install python-docx" or for mac "pip3 install python-docx"
# Features
- Calculate both unweighted and weighted GPAs.
- Add any amount of courses and remove them if needed
- Clear Instruction provided for easy use
- FAQ section to address common questions
- Ability to transfer your GPA chart to a Microsoft Word document
- Stores your classes and all of the information in a database
# Instructions
1. Running the Application:
- Open the Python file in your preferred IDE and run the program to launch the GPA calculator.
2. Choosing Calculator Type:
- The application presents tabs for Unweighted GPA Calculator and Weighted GPA Calculator. - Choose the appropriate tab based on which GPA you want.
3. Adding Courses:
- Input course details such as name, credits, and grade. - Click on the '+' button to add a course and click on the '-' button to remove them
4. Calculating GPA:
- Once all desired courses are added, click on the 'Calculate GPA' button. - The application will display your GPA based on the added courses.
5. Switching Calculator Type:
- Use the tabs to switch between unweighted and weighted GPA calculators.
6. Print Button:
 -The print button will allow you to transfer your gpa chart into a word document, click print the save the document as you wish.
7. FAQ:
- The FAQ tab provides answers to common questions about using the application.
8. Opening the database:
- To open the database, if you are using vscode we reccomend downloading the extension sqlite-viewer, if not we reccomend using DB Browser (https://sqlitebrowser.org/dl/), or you can use any other alternative to open a sqlite3 database.
# How The Calculator Works
The unweighted GPA is calculated by summing up the total grade points 
earned in all courses and dividing it by the total number of credit units. 
Each course grade is converted to a numerical value (A=4, B=3, C=2, D=1, F=0) 
and multiplied by the number of credits for the course. The resulting 
grade points for all courses are then added together and divided by the 
total number of credits to obtain the unweighted GPA.


The weighted GPA is calculated similarly to the unweighted GPA, with 
additional weight given to certain courses. In addition to summing up 
the total grade points earned in all courses and dividing it by the 
total number of credit units, extra points are added for honors, AP, 
AICE, or Dual Enrollment courses. Honors courses receive an additional 
0.04 points, while AP, AICE, or Dual Enrollment courses receive an 
additional 0.08 points. These additional points are added to the 
unweighted GPA to obtain the weighted GPA.

