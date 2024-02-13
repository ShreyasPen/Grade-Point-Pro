import tkinter as tk
from tkinter import ttk, messagebox


class CGPACalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GradePoint Pro")
        self.root.geometry("1000x650")
        self.create_widgets()
        self.style = ttk.Style()
        self.style.configure(
            "Blue.TButton",
            foreground="white",
            background="blue",
            font=("Helvetica", 10, "bold"),
        )

    def create_widgets(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        self.instructions_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.instructions_frame, text="Instructions")
        self.create_instructions_widgets()

        self.unweighted_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.unweighted_frame, text="Unweighted GPA Calculator")

        self.weighted_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.weighted_frame, text="Weighted GPA Calculator")

        self.faq_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.faq_frame, text="FAQ")
        self.create_faq_widgets()

        self.create_unweighted_widgets()
        self.create_weighted_widgets()

    def create_instructions_widgets(self):
        instructions_text = """
        To run the application, open the file in your preferred IDE (recommended through vscode) and run the program.

        To receive your exact GPA, follow these steps:

        1. Choose whether you want to calculate your Unweighted or Weighted GPA.
        2. After selecting the correct calculator:
           - For your unweighted GPA, input the course name, number of credits, and your current grade in the class.
           - For the weighted calculator, select the course type (Regular, Honors, AP, AICE, or Dual Enrollment), add the course name, include the number of credits, and your current grade.
        3. Click on the '+' button to add the course. You can remove a course by clicking the '-' button.
        4. Repeat step 2 until you have all your desired courses added.
        5. Click on 'Calculate GPA' to view your GPA based on the added courses. You can also add any class that you plan to take in the future.
        """

        instructions_label = tk.Label(
            self.instructions_frame,
            text=instructions_text,
            font=("Arial", 20),
            justify="left",
            padx=20,
            pady=20,
            wraplength=800,
        )
        instructions_label.pack(fill="both", expand=True)

    def create_faq_widgets(self):
        faq_questions = [
            "How do I add a course?",
            "Can I remove a course after adding it?",
            "How do I calculate my GPA?",
            "Can I calculate both unweighted and weighted GPA?",
            "What do I do if I encounter an error?",
        ]

        for idx, question in enumerate(faq_questions):
            question_frame = ttk.Frame(self.faq_frame)
            question_frame.pack(fill="x")
            question_label = tk.Label(
                question_frame,
                text=f"{idx + 1}. {question}",
                font=("Arial", 12, "bold"),
                padx=20,
                pady=10,
                cursor="hand2",
            )
            question_label.pack(anchor="w", fill="x")
            question_label.bind(
                "<Button-1>",
                lambda event, idx=idx, frame=question_frame: self.toggle_answer_visibility(
                    idx, frame
                ),
            )

            
    
    def faq_toggle(self):
        faq_answers = [
            "To add a course, click on the '+' button.",
            "Yes, you can remove a course by clicking on the '-' button next to it.",
            "After adding all your courses, click on the 'Calculate GPA' button.",
            "Yes, you can switch between unweighted and weighted GPA calculators using the tabs.",
            "If you encounter an error, please double-check your inputs and try again. If the issue persists, contact support.",
        ]

        for idx, question in enumerate(faq_answers):
            question_frame = ttk.Frame(self.faq_frame)
            question_frame.pack(fill="x")
            question_label = tk.Label(
                question_frame,
                text=f"{idx + 1}. {question}",
                font=("Arial", 12, "bold"),
                padx=20,
                pady=10,
                cursor="hand2",
            )
            question_label.pack(anchor="w", fill="x")
            question_label.bind(
                "<Button-1>",
                lambda event, idx=idx, frame=question_frame: self.toggle_answer_visibility(
                    idx, frame
                ),
            )

            answer_label = tk.Label(
                question_frame,
                text=faq_answers[idx],
                font=("Arial", 11),
                justify="left",
                padx=40,
                pady=5,
                wraplength=800,
            )
            answer_label.pack(anchor="w", fill="x", padx=20)



    def create_unweighted_widgets(self):
        self.unweighted_calculator_frame = ttk.Frame(self.unweighted_frame)
        self.unweighted_calculator_frame.pack(padx=20, pady=20)

        ttk.Label(
            self.unweighted_calculator_frame,
            text="GPA CALCULATOR",
            font=("Helvetica", 20, "bold"),
        ).grid(row=0, column=0, columnspan=3, pady=10)

        # Labels for course name, credits, and grade
        ttk.Label(self.unweighted_calculator_frame, text="Course Name").grid(
            row=1, column=0, padx=5, pady=5
        )
        ttk.Label(self.unweighted_calculator_frame, text="Credits").grid(
            row=1, column=1, padx=5, pady=5
        )
        ttk.Label(self.unweighted_calculator_frame, text="Grade").grid(
            row=1, column=2, padx=5, pady=5
        )

        self.unweighted_course_wrapper = ttk.Frame(self.unweighted_calculator_frame)
        self.unweighted_course_wrapper.grid(row=2, column=0, columnspan=3)

        self.add_unweighted_course()

        self.unweighted_buttons_frame = ttk.Frame(self.unweighted_calculator_frame)
        self.unweighted_buttons_frame.grid(row=3, column=0, columnspan=3, pady=10)

        ttk.Button(
            self.unweighted_buttons_frame,
            text="+ Add Course",
            command=self.add_unweighted_course,
        ).grid(row=0, column=0, padx=5)
        ttk.Button(
            self.unweighted_buttons_frame,
            text="- Remove Course",
            command=self.remove_unweighted_course,
        ).grid(row=0, column=1, padx=5)
        ttk.Button(
            self.unweighted_buttons_frame,
            text="Calculate CGPA",
            command=self.calculate_cgpa,
        ).grid(row=0, column=2, padx=5)

        self.cgpa_label = ttk.Label(
            self.unweighted_calculator_frame,
            text="Your Unweighted GPA is: ",
            font=("Helvetica", 14),
        )
        self.cgpa_label.grid(row=4, column=0, columnspan=3, pady=(10, 0))

    def create_weighted_widgets(self):
        self.weighted_calculator_frame = ttk.Frame(self.weighted_frame)
        self.weighted_calculator_frame.pack(padx=20, pady=20)

        ttk.Label(
            self.weighted_calculator_frame,
            text="Weighted GPA CALCULATOR",
            font=("Helvetica", 20, "bold"),
        ).grid(row=0, column=0, columnspan=4, pady=10)

        # Labels for course type, course name, credits, and grade
        ttk.Label(self.weighted_calculator_frame, text="Course Type").grid(
            row=1, column=0, padx=5, pady=5
        )
        ttk.Label(self.weighted_calculator_frame, text="Course Name").grid(
            row=1, column=1, padx=5, pady=5
        )
        ttk.Label(self.weighted_calculator_frame, text="Credits").grid(
            row=1, column=2, padx=5, pady=5
        )
        ttk.Label(self.weighted_calculator_frame, text="Grade").grid(
            row=1, column=3, padx=5, pady=5
        )

        self.weighted_course_wrapper = ttk.Frame(self.weighted_calculator_frame)
        self.weighted_course_wrapper.grid(row=2, column=0, columnspan=4)

        self.add_weighted_course()

        self.weighted_buttons_frame = ttk.Frame(self.weighted_calculator_frame)
        self.weighted_buttons_frame.grid(row=3, column=0, columnspan=4, pady=10)

        ttk.Button(
            self.weighted_buttons_frame,
            text="+ Add Course",
            command=self.add_weighted_course,
        ).grid(row=0, column=0, padx=5)
        ttk.Button(
            self.weighted_buttons_frame,
            text="- Remove Course",
            command=self.remove_weighted_course,
        ).grid(row=0, column=1, padx=5)
        ttk.Button(
            self.weighted_buttons_frame,
            text="Calculate CGPA",
            command=self.calculate_weighted_cgpa,
        ).grid(row=0, column=2, padx=5)

        self.weighted_cgpa_label = ttk.Label(
            self.weighted_calculator_frame,
            text="",
            font=("Helvetica", 14),
        )
        self.weighted_cgpa_label.grid(row=4, column=0, columnspan=4, pady=(10, 0))

    def add_unweighted_course(self):
        course_frame = ttk.Frame(self.unweighted_course_wrapper)
        course_frame.pack(pady=5)

        ttk.Entry(course_frame).grid(row=0, column=0, padx=5)
        ttk.Entry(course_frame).grid(row=0, column=1, padx=5)
        ttk.Combobox(course_frame, values=["A", "B", "C", "D", "F"]).grid(
            row=0, column=2, padx=5
        )
    # Define our switch function

    def remove_unweighted_course(self):
        children = self.unweighted_course_wrapper.winfo_children()
        if children:
            children[-1].destroy()

    def add_weighted_course(self):
        course_frame = ttk.Frame(self.weighted_course_wrapper)
        course_frame.pack(pady=5)

        ttk.Combobox(
            course_frame, values=["AP", "AICE", "DE", "Honors", "Regular"]
        ).grid(row=0, column=0, padx=5)
        ttk.Entry(course_frame).grid(row=0, column=1, padx=5)
        ttk.Entry(course_frame).grid(row=0, column=2, padx=5)
        ttk.Combobox(course_frame, values=["A", "B", "C", "D", "F"]).grid(
            row=0, column=3, padx=5
        )

    def remove_weighted_course(self):
        children = self.weighted_course_wrapper.winfo_children()
        if children:
            children[-1].destroy()

    def calculate_cgpa(self):
        children = self.unweighted_course_wrapper.winfo_children()
        total_grade_points = 0
        total_credit_units = 0

        for child in children:
            entries = child.winfo_children()
            course_code = entries[0].get()
            credit_units = entries[1].get()
            grade = entries[2].get()

            if course_code and credit_units and grade:
                grade_points = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
                total_grade_points += grade_points[grade] * float(credit_units)
                total_credit_units += float(credit_units)

        if total_credit_units == 0:
            messagebox.showwarning(
                "Warning", "Please add at least one course with credit units."
            )
        else:
            cgpa = total_grade_points / total_credit_units
            self.cgpa_label.config(text=f"Your Unweighted GPA is: {cgpa:.2f}")

    def calculate_weighted_cgpa(self):
        children = self.weighted_course_wrapper.winfo_children()
        total_grade_points = 0
        total_credit_units = 0

        for child in children:
            entries = child.winfo_children()
            course_type = entries[0].get()
            course_code = entries[1].get()
            credit_units = entries[2].get()
            grade = entries[3].get()

            if course_code and credit_units and grade:
                grade_points = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
                unweighted_grade_points = grade_points[grade] * float(credit_units)

                # Calculate the weighted GPA according to the specified rules
                if course_type in ["AP", "AICE", "DE"] and grade in ["A", "B", "C"]:
                    unweighted_grade_points += 0.08 * float(credit_units)
                elif course_type == "Honors" and grade in ["A", "B", "C"]:
                    unweighted_grade_points += 0.04 * float(credit_units)

                total_grade_points += unweighted_grade_points
                total_credit_units += float(credit_units)

        if total_credit_units == 0:
            messagebox.showwarning(
                "Warning", "Please add at least one course with credit units."
            )
        else:
            # Calculate the weighted GPA
            weighted_cgpa = total_grade_points / total_credit_units
            self.weighted_cgpa_label.config(
                text=f"Your Weighted CGPA is: {weighted_cgpa:.2f}"
            )


root = tk.Tk()
app = CGPACalculatorApp(root)
root.mainloop()
