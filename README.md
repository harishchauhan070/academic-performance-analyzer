#  Academic Performance Analyzer

A simple Python project to **analyze and visualize student performance** using data analysis and visualization techniques.  
This project demonstrates the use of **Pandas** for data handling and **Matplotlib** for generating insights through charts.  

---

##  Features
- Reads student marks from a CSV file (`students.csv`)
- Calculates subject-wise averages
- Identifies the **top performer** in the class
- Generates **bar charts** for performance visualization

---

##  Repository Structure
academic-performance-analyzer/
│
├── analyzer.py # Script to compute statistics and print report
├── visualizer.py # Script to generate performance charts
├── students.csv # Sample dataset with student marks
├── requirements.txt # Python dependencies
└── README.md # Documentation



---

##  Installation
Clone this repository and install required dependencies:

```bash
git clone https://github.com/harishchauhan070/academic-performance-analyzer.git
cd academic-performance-analyzer
pip install -r requirements.txt
 Usage
1. Analyze student performance
bash
Copy code
python analyzer.py
Example Output:

===== Academic Performance Report =====
Total Students: 5

Subject-wise Averages:
Math: 80.00
Science: 83.40
English: 85.20

Topper:
Ananya with total 276 marks
2. Generate performance charts
bash
Copy code
python visualizer.py
This will create PNG charts:

Math_performance.png

Science_performance.png

English_performance.png

Example Dataset (students.csv)
Name,Math,Science,English
Harish,85,78,90
Ravi,70,88,76
Ananya,92,95,89
Priya,65,72,80
Amit,88,84,91
Tech Stack
Python 3

Pandas → data analysis

Matplotlib → visualization

👨‍💻 Author
Harish Chauhan
📧 haishcha456@gmail.com
🔗 LinkedIn www.linkedin.com/in/harish-chauhan-717175338
💻 GitHub harishchauhan070
