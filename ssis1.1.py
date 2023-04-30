import csv

courses = []
students = []
fields = [' student id',' name',' course',' gender',' year level']
database = 'studentlist.csv'
""""
class Course:

    def add_course(self):
            add = input("\n enter course: ")
            #courses.append(add)
    
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
"""
def select_menu():
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(" 1 : add  student")
        print(" 2 : delete student")
        print(" 3 : edit student ")
        print(" 4 : view list student")
        print(" 5 : quit")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


class Student:

    def add_student(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('add student information')
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        global fields
        global database
        for field in fields:
            new = input("\n add student: "+ field + ':')
            students.append(new)

        with open(database,'a', encoding= "utf-8") as sdt:
            writer = csv.writer(sdt)
            writer.writerows([students])

        print('data saves successfully')
        input("press any key to continue")
        return

    def delete_student(self):
        global fields
        global database
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('delete student')
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        student_id = input('enter student id no. to delete: ')
        student_found = False
        temp_data = []
        with open (database,'r', encoding='utf - 8') as dlt:
            reader = csv.reader(dlt)
            counter = 0
            for row in reader:
                if len(row)> 0:
                    if student_id != row[0]:
                        temp_data.append(row)
                        counter += 1
            else:
                student_found = True
        if student_found is True:
            with open(database,'w',encoding='utf-8') as dlt:
                writer = csv.writer(dlt)
                writer.writerows(temp_data)
                print('student ID no.', student_id,'deleted sucessfully')
        else:
            print('student ID no. not found in our database')

        input('press any key to continue')


    def edit_student(self):
        global fields
        global database
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("update student")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        student_id = input('enter student ID no.')
        index = None
        update_student = []
        with open(database,'r',encoding="utf-8") as ups:
            reader =csv.reader(ups)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if student_id == row[0]:
                        students_data = []
                        for field in fields:
                            revision = input("enter" + field + ": ")
                            students_data.append(revision)
                        update_student.append(students_data)

                    else:
                        update_student.append(row)
                    counter += 1
            else:
                index is not None
        if index is not None:
            with open (database,'w',encoding= 'utf-8') as ups:
                writer = csv.writer(ups)
                writer.writerow(update_student)
        else:
            print('Student ID no. not found in database')
            
        input("press any key to continue")

    def list_student(self):
        global fields
        global database
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("student records")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        with open (database,'r',encoding='utf-8') as list:
            reader = csv.reader(list)
            for row in reader:
                if len(row)>0:
                    print("student id: ",row[0])
                    print("name: ",row[1])
                    print("course: ",row[2])
                    print("gender: ",row[3])
                    print("year level: ",row[4])
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    
#c= Course()
s = Student()

def display():
    select_menu()
    answer = input( "\n what do you want to do?: ")
    while answer != '5':
        if answer == "add course":
           #c.add_course()
           select_menu()
           answer = input( "\n what do you want to do?: ")
        elif answer == "delete course":
            #c.delete_course()
            select_menu()
            answer = input("\n what to do you want to do?: ")
        elif answer == "edit course":
           # c.edit_course()
            select_menu()
            answer = input("\n what to do you want to do?: ")

        elif answer == "view list course":
           # c.list_course()
            select_menu()
            answer = input("\n what to do you want to do?: ")
        elif answer == "1":
            s.add_student()
            select_menu()
            answer = input("\n what to do you want to do?: ")
        elif answer == "2":
            s.delete_student()
            select_menu()
            answer = input("\n what to do you want to do?: ")
        elif answer == "3":
            s.edit_student()
            select_menu()
            answer = input("\n what to do you want to do?: ")
        elif answer == "4":
            s.list_student()
            select_menu()
            answer = input("\n what to do you want to do?: ")
        

display()

