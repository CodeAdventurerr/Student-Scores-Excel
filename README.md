# 🎓 Student Scores to Excel

## 📌 Description
A simple Python program where the user can input student names and their grades. The program calculates the average grade, determines if the student Passed or Failed based on the average score, and then saves the results into an Excel (.xlsx) file using pandas. This project is suitable for beginner Python learners who want to practice working with user input, basic logic, and data reporting.

## 🚀 Features
- Collect multiple student names and grades via user input.
- Validate that each student receives exactly 4 grades.
- Automatically calculate the average score.
- Determine if the student Passed (75+) or Failed.
- Save the final results into a formatted Excel file (`students.xlsx`).

## 🖥️ Sample Output (Excel File)
    
                Name                  Grades
                Alice                 80.0
                Bob                   72.5



## 🛠️ Technologies Used

- ![Python](https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=python&logoColor=white) Python 3
- ![Pandas](https://img.shields.io/badge/pandas-1.3.3-orange?style=flat-square&logo=pandas&logoColor=white) pandas
- ![Openpyxl](https://img.shields.io/badge/openpyxl-3.0.7-green?style=flat-square&logo=openpyxl&logoColor=white) openpyxl (Excel writer engine for pandas)

## 📂 Project Structure

Student-Scores-Excel/ ├── students_scores.py # Main Python script ├── students.xlsx # Example output Excel file (optional) ├── requirements.txt # List of dependencies └── README.md # Project documentation (this file)


## ⚙️ Installation & Setup

1. **Clone the Repository**:

   ```bash
                  git clone https://github.com/your-username/Student-Scores-Excel.git
                  cd Student-Scores-Excel
   
2. **Install Requirements:**:

   ```bash
                  pip install -r requirements.txt
   
3. **Clone the Repository**:

   ```bash
                   Run the Programl


## 📄 How to Use

Run the program in the terminal.

Input how many students you want to add.

For each student:

Enter the name.

Enter 4 grades separated by commas (e.g., 85,90,78,92).

The program will calculate averages and pass/fail status.

An Excel file students.xlsx will be generated in the project directory.

## 💡 Example Use Case

This small tool can help educators, tutors, or students quickly input and organize grades into a clean Excel file without manual calculations.

## 📌 Notes

The Excel file will overwrite the previous students.xlsx file each time the program is run.

The index in Excel will start from 0 by default. This can be changed if needed.
  
