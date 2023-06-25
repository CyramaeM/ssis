import csv

courses = []
students = []
fields = [' student id',' name','course',' gender',' year level']
course_fields =['course id','course name']
database = 'student_list.csv'
course_data = 'course_list.csv'


class Course:

    def add_course(self):
        global course_fields
        global course_data
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('add course')
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        for field in course_fields:
            add = input("enter "+ field + ': ')
            courses.append(add)
            
        with open(course_data,'a',encoding= 'utf-8', newline= '') as a:
            writer = csv.writer(a)
            writer.writerows([courses])
        
        print("course added successfully")
        input("press any key to return to main")
    
    def list_course(self):
        global course_fields
        global course_data
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('course list')
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        with open (course_data,'r', encoding= "utf-8") as lst:
            reader = csv.reader(lst)
            for row in reader:
                    if len(row) > 0:
                        print("course ID: ",row[0])
                        print("course name: ",row[1])
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")        
        input("press any key to continue")
    
    def delete_course(self):
        global course_data
        global course_fields
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('delete course')
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        course_id = input("enter course id to delete: ")
        course_found = False
        update_course = []
        student_found =False
        update_student =[]
        with open(course_data,'r', encoding='utf-8')as dlt:
            reader = csv.reader(dlt)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if course_id != row[0]:
                        update_course.append(row)
                        
                    else:
                        counter +=1
                        course_found = True

        if course_found is True:
                with open ( course_data, "w",encoding= "utf-8") as ups:
                    writer = csv.writer(ups)
                    writer.writerows(update_course)

                with open(database,'r',newline='') as file:
                    reader = csv.reader(file)
                    data = list(reader)
                    count = 0
                
                with open(database,'w',newline='') as sdlt:
                        writer = csv.writer(sdlt)
                        writer.writerows(update_student)
                        for rows in update_student:
                            if rows[2] == course_data[1]:
                                rows[2] = ''

                            writer.writerow(rows)

                print("course Id: ", course_id,"deleted successfully")
        else:
            print("course ID not found in our database")

        
        
        input("press any key to return to menu ")

    def edit_course(self):
        global course_fields
        global course_data
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("update course")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        course_id = input('enter course ID no.')
        index_course = None 
        update_course = []
        with open(course_data,'r',encoding="utf-8",newline='') as ups:
            reader =csv.reader(ups)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if course_id == row[0]:
                        index_course = counter
                        print("student found: at index ", index_course)
                        course_data = []
                        for field in course_fields:
                            revision = input("enter" + field + ": ")
                            course_data.append(revision)
                        update_course.append(course_data)
                    else:
                        update_course.append(row)
                    counter += 1

        if index_course is not None:
            with open (course_data,"w",encoding= 'utf-8',newline='') as ups:
                writer = csv.writer(ups)
                writer.writerows(update_course)
                print('course information updated')
        else:
            print('course ID no. not found in database')
            
class Student:

    def add_student(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('add student information')
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        global fields
        global database
        for field in fields:
            new = input("\n enter: "+ field + ':')
            students.append(new)

        with open(database,'a', encoding= "utf-8", newline='') as sdt:
            writer = csv.writer(sdt)
            writer.writerows([students])

        print('data saves successfully')
        input("press any key to return to menu")


    def delete_student(self):
        global fields
        global database
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('delete student')
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        student_id = input('enter student id no. to delete: ')
        student_found = False
        temp_data = []
        with open (database,'r', encoding='utf-8') as dlt:
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

        input('press any key to return to menu')


    def edit_student(self):
        global fields
        global database

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("update student")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        student_id = input('enter student ID no.')
        index_student = None 
        update_student = []
        with open(database,'r',encoding="utf-8",newline='') as ups:
            reader =csv.reader(ups)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if student_id == row[0]:
                        index_student = counter
                        print("student found: at index ", index_student)
                        students_data = []
                        for field in fields:
                            revision = input("enter" + field + ": ")
                            students_data.append(revision)
                        update_student.append(students_data)
                    else:
                        update_student.append(row)
                    counter += 1

        if index_student is not None:
            with open (database,"w",encoding= 'utf-8',newline='') as ups:
                writer = csv.writer(ups)
                writer.writerows(update_student)
                print('student information updated')
        else:
            print('Student ID no. not found in database')
            
        input("press any key to return to  menu")


    def search_students(self):
        global fields
        global database
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("search student records")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        idnumber =input("enter student Id no: ")
        with  open (database,"r",encoding="utf-8", newline='')as find:
            reader = csv.reader(find)
            for row in reader:
                if len(row) > 0:
                    if idnumber == row[0]:
                        print("~~~~~~~ student found ~~~~~~~~")
                        print("Student Id: ", row[0])
                        print("name: ", row[1])
                        print("course: ",row[2])
                        print("sex: ",row[3])
                        print("year level: ",row[4])
                        break
                
        input("press any key to return to menu")


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
                    print("course:",row[2])
                    print("sex: ",row[3])
                    print("year level: ",row[4])
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        input("press any key to return to menu")

    
def select_menu():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" 1 : add  student/course")
    print(" 2 : delete student/course")
    print(" 3 : edit student/course")
    print(" 4 : view list student/course")
    print(" 5 : search student")
    print(" 6 : quit")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def add_menu():
    print("what do you want to do?:")
    print("a: add student")
    print("b: add course")
    print("c: back")
    answer = input()
    while answer != 'c':
        if answer == 'a':
            s.add_student()
            return
        elif answer == 'b':
            c.add_course()
            return
        else:
            print('error: command not found')
            add_menu()
            answer = input()
    return


def delete_menu():
    print("what do you want to do?:")
    print("a: delete student")
    print("b: delete course")
    print("c: back")
    answer = input()
    while answer != 'c':
        if answer == 'a':
            s.delete_student()
            return
        elif answer == 'b':
            c.delete_course()  
            return
        else:
            print('error: command not found')
            delete_menu()
            answer = input()
    return


def edit_menu():
    print("what do you want to do?:")
    print("a: edit student")
    print("b: edit course")
    print("c: back")
    answer = input()
    while answer !='c':
        if answer == 'a':
            s.edit_student()
            return
        elif answer == 'b':
            c.edit_course()
            return
        else:
            print('error: command not found')
            edit_menu()
            answer = input()
    return


def view_menu():
    print("what do you want to do?:")
    print("a: view student")
    print("b: view course")
    print("c: back")
    answer = input()
    while answer != 'c':
        if answer == 'a':
            s.list_student()
            return
        elif answer == 'b':
            c.list_course()
            return
        else:
            print('error: command not found')
            view_menu()
            answer = input()
    return


c= Course()
s = Student()

select_menu()
answer = input("\n what do you want to do?: ")
while answer != '6':
    if answer == "1":
        add_menu()
        select_menu()
        answer = input("\n what to do you want to do?: ")
    elif answer == "2":
        delete_menu()
        select_menu()
        answer = input("\n what to do you want to do?: ")
    elif answer == "3":
        edit_menu()
        select_menu()
        answer = input("\n what to do you want to do?: ")
    elif answer == "4":
        view_menu()
        select_menu()
        answer = input("\n what to do you want to do?: ")
    elif answer == '5':
        s.search_students()
        select_menu()
        answer = input("\n what to do you want to do?: ")
        break
    else:
        print("error: command invalid")
        select_menu()
        answer = input("\n what to do you want to do?: ")
        
print(" Thank you for using our system")        

