

"""
  A Simple Smart Study Planner
---------------------------------
It is a simple smart study planner that allocates time to each subject/course based on difficulty level and current progress
"""


#Input stage

courses = []

#Asks users how many courses they want to study
#This helps to determine how many times we loop over the course input

while True:
    try:
       num_courses = int(input("How many courses are you offering?: "))
       if num_courses > 0:
            break
       else:
            print("Number must be greater than 0.")
    except ValueError:
       print("Please input an integer value")


#Collect information from each course
#This includes name, difficulty level and progress
#The while loop and try-except block are also uses for exception handling

for i in range(num_courses):
   print("Course ", i+1)

   while True:
        name = input("What's the name of the course?: ")
        if name.replace(" ", "").isalnum():
           break
        print("Only letters and numbers are allowed.")

   while True:
        difficulty_level = int(input("How hard is it? 1=simple, 2=medium, 3=hard: "))
        if difficulty_level not in [1, 2, 3]:
           print("Please choose 1, 2 or 3 only")
        else:
           break

   while True:
        try:
           progress = int(input("What's your current standing in the course on a scale of 0 to 10?: "))
           if 0 <= progress <= 10:
              break

           else:
              print("Please enter a number between 0 and 10.")
        except ValueError:
           print("Please enter a valid number. No letters allowed.")


#A dictionary is created to store input
   course = {
         "Name": name,
         "Difficulty": difficulty_level,
         "Progress": progress
   }
   courses.append(course)


#Calculate priority based on difficulty and progress
#Higher priority = more study time allocation

   priority = difficulty_level * (10 - progress)
   course["Priority"] = priority

   courses.sort(key=lambda course: course["Priority"], reverse=True)

top_courses = courses[:3]


#Users input the total time available to study

while True:
     try:
        total_time = int(input("How long do you intend to study?: "))
        if total_time > 0:
           break
        else:
           print("Time must be greater than 0.")

     except ValueError:
        print("Please enter a whole number")
if total_time >= 8:
   print("\n😳 Wow,that's a lot of time...no excuses oh!!")
elif total_time >= 4:
   print("\n😌 Nice and solid study time. Stay focused!")
else:
   print("\n😅 Not much time we got here, but let's make it count.")



#Split total time based on course priority

total_priority = 0
for course in top_courses:
    total_priority += course["Priority"]

allocated_time = []
for course in top_courses:
    time_allocated = round((course["Priority"] / total_priority) * total_time, 1)
    allocated_time.append(time_allocated)

int_time = [round(t) for t in allocated_time]
remaining_time = total_time - sum(int_time)


for i in range(remaining_time):
    allocated_time[i] += 1

for i, course in enumerate(top_courses):
       course["Time"] = int_time[i]


#Display final recommended study plan inorder of priority
print("\n📅 Study Plan:")
print("-" * 30)

for i, course in enumerate(top_courses):
    print(f"{i+1}. {course['Name']} → {course["Time"]} hr(s)")


#Inform user about recommended number of courses per session
print("\n⚠️ Disclaimer:")
print("For optimal focus and retention, it is recommended to study a minimum of 1 subject and maximum of 3 subjects per session.")
