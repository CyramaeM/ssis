
courses = []
students = []

class Course:

    def add_course(self):
           # assert courses == 0
            add = input("\n enter course: ")
            courses.append(add)
    
    def list_course(self):
        if len(courses) == 0:
            print("list is empty! ")
        else:
            print(courses)
        
    def delete_course(self):
        if len(courses) == 0:
            print("course doesn't exist in our system! ")
        else:
            remove = input("which course you want to delete?: ")
            if remove in courses:
                courses.remove(remove)
                print(courses)
            
    def edit_course(self):
        if len(courses) == 0:
            print("no courses to edit ")
        else:
            edited = input("what course do you want to edit?: ")
            print(courses)
            if edited in courses:
                newEdit = input("\n ")
                courses.remove(edited)
                courses.append(newEdit)
                print(courses)

    def select_menu(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(" 1 : add course or student")
        print(" 2 : delete course or student")
        print(" 3 : edit course or student ")
        print(" 4 : view list course or student")
        print(" 5 : quit")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


class Student:

    def add_student(self):
        #assert students == 0
        new = input("\n add student: ")
        students.append(new)

    def delete_student(self):
        if len(students)== 0:
            print("no student to delete ")
        else:
            expel = input(" enter the name of the student you want to delete ")
            if expel in students:
                students.remove(expel)
                print(students)


    def edit_student(self):
        if len(students) == 0:
            print("no students to edit")
        else:
            revision = input("which student you want to edit ")
            print(students)
            if revision in students:
                update = input(" ")
                students.remove(revision)
                students.append(update)
                print(students)

    def list_student(self):
        if len(students) == 0:
            print("the list is empty! ")
        else:
            print(students)


c= Course()
s = Student()

def display():
    c.select_menu()
    answer = input( "\n what do you want to do?: ")
    while answer != 'quit':
        if answer == "add course":
           c.add_course()
           c.select_menu()
           answer = input( "\n what do you want to do?: ")
        elif answer == "delete course":
            c.delete_course()
            c.select_menu()
            answer = input("\n what to do you want to do?: ")
        elif answer == "edit course":
            c.edit_course()
            c.select_menu()
            answer = input("\n what to do you want to do?: ")
        elif answer == "view list course":
            c.list_course()
            c.select_menu()
            answer = input("\n what to do you want to do?: ")
        elif answer == "add student":
            s.add_student()
            c.select_menu()
            answer = input("\n what to do you want to do?: ")
        elif answer == "delete student":
            s.delete_student()
            c.select_menu()
            answer = input("\n what to do you want to do?: ")
        elif answer == "edit student":
            s.edit_student()
            c.select_menu()
            answer = input("\n what to do you want to do?: ")
        elif answer == "view list student":
            s.list_student()
            c.select_menu()
            answer = input("\n what to do you want to do?: ")
        

display()

