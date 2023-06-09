import csv

fields = ['student id','name','course','gender','year level']
course_fields =['course id','course name']
database = 'studentlist.csv'
course_data = 'courselist.csv'


class Course:

    def add_course(self):
        global course_fields
        global course_data
       
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('add course')
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        courses = []

        for field in course_fields:
            add = input("enter "+ field + ': ')
            courses.append(add.upper())

        with open(course_data,'r',newline='') as file:
            reader = csv.reader(file,delimiter=',')
            exist = list(reader)
        
            for row in exist:
                if courses[0] == row[0]:
                    print("course id already exist!")
                    return
            
        with open(course_data,'a',newline='') as a:
            writer = csv.writer(a,delimiter=',')
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
        global database
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('delete course')
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        course_id = input("Enter course ID to delete: ")
        course_found = False
        updated_courses = []
        updated_students = []
        student_found = False

        with open(course_data, 'r', newline='') as dlt:
            reader = csv.reader(dlt, delimiter=',')
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if course_id.upper() != row[0]:
                        updated_courses.append(row)
                        counter += 1
                    else:
                        course_found = True

        if course_found is True:
            with open(database, 'r', newline='') as sdlt:
                sreader = csv.DictReader(sdlt,fieldnames=fields,delimiter=',')
                for row in sreader:
                    if row['course'] != course_id.upper():
                        updated_students.append(row)
                    else:
                        student_found = True

            with open(course_data, 'w', newline='') as up:
                writer = csv.writer(up, delimiter=',')
                writer.writerows(updated_courses)

            with open(database, 'w', newline='') as sdlt:
                fieldnames = ['student id', 'name', 'course', 'gender', 'year level']
                writer = csv.DictWriter(sdlt, fieldnames=fieldnames)
                #writer.writeheader()
                writer.writerows(updated_students)

            print("Course ID:", course_id, "deleted successfully")
        else:
            print("Course ID not found in our database")

        input("Press any key to return to the menu")


    def edit_course(self):
        global course_fields
        global course_data
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("update course")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        course_id = input('enter course ID no.')
        index_course = None 
        update_course = []
        with open(course_data,'r',newline='') as ups:
            reader =csv.reader(ups,delimiter=',')
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if course_id.upper() == row[0]:
                        index_course = counter
                        print("student found: at index ", index_course)
                        course_datas = []
                        for field in course_fields:
                            revision = input("enter " + field + ": ")
                            course_datas.append(revision.upper())
                        update_course.append(course_datas)
                    else:
                        update_course.append(row)
                    counter += 1

        if index_course is not None:
            with open (course_data,'w',newline='') as ups:
                writer = csv.writer(ups,delimiter=',')
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
        global course_data

        students = []

        for field in fields:
            new = input("enter " + field + ': ')
            students.append(new.upper())

        with open(database, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            exist = list(reader)

        for row in exist:
            if students[0] == row[0]:
                print("student id already exists!")
                return
            if students[2] not in self.get_course_list():
                print("course not found in the course list!")
                return

        with open(database, 'a', newline='') as sdt:
            writer = csv.writer(sdt, delimiter=',')
            writer.writerows([students])

        print('data saved successfully')
        input("press any key to return to menu")

    def get_course_list(self):
        course_list = []
        with open(course_data, 'r', encoding="utf-8") as lst:
            reader = csv.reader(lst)
            for row in reader:
                if len(row) > 0:
                    course_list.append(row[0])
        return course_list



    def delete_student(self):
        global fields
        global database
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('delete student')
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        student_id = input('enter student id no. to delete: ')
        student_found = False
        temp_data = []
        with open (database,'r') as dlt:
            reader = csv.reader(dlt,delimiter=',')
            counter = 0
            for row in reader:
                if len(row)> 0:
                    if student_id != row[0]:
                        temp_data.append(row)
                        counter += 1
            else:
                student_found = True
        if student_found is True:
            with open(database,'w',newline='') as dlt:
                writer = csv.writer(dlt,delimiter=',')
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
        with open(database,'r') as ups:
            reader =csv.reader(ups,delimiter=',')
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if student_id == row[0]:
                        index_student = counter
                        print("student found: at index ", index_student)
                        students_data = []
                        for field in fields:
                            revision = input("enter " + field + ": ")
                            students_data.append(revision.upper())
                        update_student.append(students_data)
                    else:
                        update_student.append(row)
                    counter += 1

        if index_student is not None:
            with open (database,"w",newline='') as ups:
                writer = csv.writer(ups,delimiter=',')
                writer.writerows(update_student)
                print('student information updated')
        else:
            print('Student ID no. not found in database')
            
        input("press any key to return to  menu")


    def search_students(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("search student records")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        idnumber = input("Enter Student ID or name: ")
        with open(database,'r') as fnd:
            sreader= csv.DictReader(fnd,fieldnames=fields,delimiter=',')
            found = False
            next(sreader)
            for row in sreader:
                if idnumber.lower() in str(row["student id"]).lower() or idnumber.lower() in str(row["name"]).lower():
                    found = True
                    print("ID number", row["student id"])
                    print("Name: ",row["name"])
                    print("Course: ",row["course"])
                    print("Gender: ",row["gender"])
                    print("Year level: ",row["year level"])
            if not found:
                print("Student not Found. ")
        input("Press enter to return to menu ")


    def list_student(self):
        global fields
        global database
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("student records")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        with open (database,'r',newline='') as list:
            reader = csv.reader(list,delimiter=',')
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

