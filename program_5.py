# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.
courses = {}

def enter_course_info():
    while True:
        courses[input("Course ID ")] = input("Course Name ")

        if not input("Enter y if you would like to add another course") == "y":
            break

    requested = input("Enter Course ID")

    for i, key in enumerate(courses):
        if key == requested:
            print(key)

    print(courses[requested])





enter_course_info()