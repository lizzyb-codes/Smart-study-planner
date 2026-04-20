# Smart-study-planner


#PROGRAM DESCRIPTION: 

The Smart Study Planner is a Python-based program that helps students allocate study time across their courses based on their current progress and the difficulty level of each course.

In simple terms, the program acts as a flexible study planner that helps students decide what to study and for how long, depending on how difficult a course is and how much progress has been made. 

#FEATURES
- Accepts multiple courses as input
- Collects:
  • course name
  • difficulty level (1-3)
  • progress (0-10)
- Calculates the priority for each course using the difficulty level and progress
- Allocates study time based on calculated priority
- Ensures a minimum if 1 subject snd maximum of 3 subjects is studied per session for optimal productivity
- Prevents invalid inputs using error handling
- Displays a structured study plan

#HOW IT WORKS
1. User enters the number of courses being offered
2. User inputs details for each course
3. User inputs total available study time
4. The program:
   - calculates priority
   - sorts courses based on priority
   - distributes time proportionally
5. Outputs a recommended study plan

#TECH USED
- Python 3
- Google colab

#HOW TO RUN THIS PROJECT

*Option 1: Run on Google colab (Recommended)
1. Go to this GitHub repo
2. Click on the project file (Smart_Study_Planner.ipynb)
3. At the top in the preview section, there's a button: "Open in Colab" —> click it
4. Colab opens the notebook
5. From the options menu at the top left corner, click runtime and then click run all
6. Enter inputs when prompted
7. The program displays a structured study plan

*Option 2: Running the Project Locally
1. Install Python
   - Go to: https://www.python.org/downloads/
   - Download and Install Python 3
   - During installation, make sure to check "Add Python to PATH"
2. Download the project
   - Go to this GitHub repository
   - Click the green Code button
   - Select Download ZIP
   - Extract(unzip) the downloaded file
   - Open the extracted folder
3. Locate the Python File
   - Inside the folder, find the file named "smart_study_planner.py"
4. Open the Command Prompt/Terminal
   - On Windows: Press Windows + R, type cmd, and press Enter
5. Navigate to the Project Folder
   - In the terminal, type:
     cd Downloads
   - Then,
     cd Smart-study-planner
6. Run the program
   - Type "python smart_study_planner.py"
   - Press Enter
7. Follow the prompts
   - Enter your course details when asked
   - Input your available study time
   - The program will generate your study plan

#EXAMPLE USAGE:

**Input
- Number of Courses: 4
- Courses:
  - Maths (Difficulty: 1, Progress: 8)
  - English (Difficulty: 1, Progress: 8)
  - Chemistry (Difficulty: 2, Progress: 6)
  - Physics (Difficulty: 2, Progress: 7)
- Available study time: 3 hours

**Output
1. Chemistry = 2 hr
2. Physics = 1 hr
3. Maths = 0 hr 

#⚠️NOTE
   The program limits the recommended number of courses to 3 per session to promote effective learning and reduce burnout. 
   While it is possible to study more, focusing on fewer subjects allows for deeper understanding and better retention.
   If you can handle more than that consistently, you might just have superpowers😆.

#AUTHOR:

lizzyb-codes
