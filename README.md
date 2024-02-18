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
- To open the database, if you are using vscode we reccomend downloading the extension sqlite-viewer, if not we reccomend using DB Browser (https://sqlitebrowser.org/dl/), or you can use any toher alternative to open a sqlite3 database.
# How The Calculator Works
- The calculator uses the Middleton High School and the Hillsborough County Public Schools GPA scale
- The scale goes as follows
- For Regular, there is not any added credits
- For Honors, 0.04 is added per class
- For AICE, AP, DE, 0.08 is added per class
- Using this scale the calulator takes your grade in the class and uses it to give you your accurate GPA
- Note: This scale is used to calculate your weighted GPA which contains all of the credits you recieve from your classes
- No credits are added on for your unweighted GPA

