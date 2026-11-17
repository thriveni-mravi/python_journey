def add_student_info(stud):
    while True: 
        try:
            n=int(input("num of students:"))
            subj=int(input("enter num of subjects:"))
            if n>0 and subj>0:
                break
            else:
                print("num of students and subject must be positive integer")
        except ValueError:
            print("num of students and subjects must be integer value")
    print("enter students details")
    while n>0:
        while True:
            usn=input("enter usn:").lower()
            if not usn.isalpha() and not usn.isdigit() and usn.isalnum()==True and len(usn)==5:
                break
            else:
                print("enter correct usn")
        while True:
            name=input("student name:")
            if name.isalpha()==True or " " in name:
                break
            else:
                print("enter string value for name.")

        if usn not in stud:
            stud[usn]={}
            stud[usn]["name"]=name
            stud[usn]["subjects"]={}
            for i in range(subj):
                while True:
                    while True:
                        sub=input("sub:")
                        if sub.isalpha()==True:
                            break
                        else:
                            print("enter string value for sub.")
                    if sub in stud[usn]["subjects"]:
                        print(sub,"is already exist! enter another sub.")
                    else:
                        break
                get_valid_marks(stud,usn,sub)
            n-=1
        else:
            print(usn ,"is already exist! check the student usn again")
        


def display_student_info(stud):
    print("-----students details-----")
    if stud=={}:
        print("student details are not added yet!")
    else:
        for key in stud:
            print("usn   :",key)
            print("name  :",stud[key]["name"])
            for k in stud[key]["subjects"]:
                if stud[key]["subjects"][k]==None:
                    print(k," marks not available")
                else:
                    print(k  ,"-", stud[key]["subjects"][k])

def search_student_details(req_stud,stud):
    if req_stud in stud:
        print("student details found:")
        print("student name:",stud[req_stud]["name"])
        for k in stud[req_stud]["subjects"]:
            if stud[req_stud]["subjects"][k]==None:
                print(k," marks not available")
            else:
                print(k ,"-",stud[req_stud]["subjects"][k])
                
    else:
        print("student details not found")

def class_average(stud):
    if stud=={}:
        print("student details are not added yet!")
    else:
        print("-----class average-----")
        sum_of_marks=0
        num_of_marks=0
        for key in stud:
            for k in stud[key]["subjects"]:
                if stud[key]["subjects"][k]!=None:
                    sum_of_marks+=stud[key]["subjects"][k]
                    num_of_marks+=1
        if num_of_marks>0:
            class_average=sum_of_marks/num_of_marks
            print(class_average)
        else:
            print("no marks avilable")

def get_valid_marks(stud,usn,sub):
        while True:
            marks=input("enter marks: (enter ab if student absent)").lower()
            if marks=="ab":
                stud[usn]["subjects"][sub]=None
                break
            try:
                marks=float(marks)
                if marks>=0 and marks<=100:
                    stud[usn]["subjects"][sub]=marks
                    break
                else:
                    print("marks must greaterthan or equal to zero and lessthan or equal to 100")
            except ValueError:
                print("enter valid marks or if student absent then enter ab !")
            
        
def update_student_details(stud):
    if not stud:
        print("No student details available!")
        return
    usn=input("student usn:").lower()
    search_student_details(usn,stud)
    if usn in stud:
            while True:
                print("which sub marks u want to update:")
                sub=input()
                if sub in stud[usn]["subjects"]:
                    get_valid_marks(stud,usn,sub)
                    break
                else:
                    print("sub not found! ")

    else:
        print("add the student details before trying to update")

def delete_student_detail(stud):
    if not stud:
        print("No student details available!")
        return
    print("enter student usn to delete details:")
    usn=input().lower()
    if usn in stud:
        del stud[usn]
        print(usn," details are deleted successfully")
    else:
        print(usn," not found")

def individual_student_report(stud):
    usn=input("enter student usn:")
    search_student_details(usn,stud)
    if usn in stud:
        total=0
        num_of_sub_absent=0
        num_of_sub_attended=0
        
        num_sub=len(stud[usn]["subjects"])
        for sub in stud[usn]["subjects"]:
            if stud[usn]["subjects"][sub]!=None:
                total+=stud[usn]["subjects"][sub]
                num_of_sub_attended+=1
                
            else:
                num_of_sub_absent+=1

        print("total maximum marks:",num_sub*100)
        print("scored marks:",total)
        percentage=(total/(num_sub*100))*100
        print("percentage:",percentage)  
        print("number of subjects attended for exam:",num_of_sub_attended)
        print("number of subjects not attended for exam:",num_of_sub_absent)

        attended = {key: value for key, value in stud[usn]["subjects"].items() if value!=None}
        if attended:
            highest_scored_sub=max(attended,key=lambda sub:attended[sub])
            lowest_scored_sub=min(attended,key=lambda sub:attended[sub])
            print("highest scored sub is",highest_scored_sub,"marks is",attended[highest_scored_sub])
            print("lowest scored sub is",lowest_scored_sub,"marks is",attended[lowest_scored_sub])
        else:
            print("marks are not available")
        
def student_ranking_list(stud):
    ranking={}
    if not stud:
        print("No student details available!")
        return
    for usn in stud:
        total=0
        for sub in stud[usn]["subjects"]:
            if stud[usn]["subjects"][sub]!=None:
                total+=stud[usn]["subjects"][sub]
        ranking[usn]=total
    order_of_ranking=dict(sorted(ranking.items(), key=lambda item:item[1],reverse=True))
    print("Ranking of students according to the total marks")
    for key in order_of_ranking:
        print(key  ,"--  ",order_of_ranking[key])


print("-------student details-------")
stud={}
print("-----STUDENT MARKS MANAGEMENT-----")
print("1. add student details:")
print("2. display all student details:")
print("3. search for perticular student details:")
print("4. calculate average marks: ")
print("5. update student details")
print("6. delete student details")
print("7. individual student report")
print("8. student ranking list ")
print("9. exit:")
while True:
    try:
        choice=int(input("enter ur choice (1-9):"))
        match (choice):
            case 1:
                add_student_info(stud)
            case 2: 
                display_student_info(stud)
            case 3:
                req_stud=input("enter student usn:").lower()
                search_student_details(req_stud,stud)
            case 4:
                class_average(stud)
            case 5:
                update_student_details(stud)
            case 6:
                delete_student_detail(stud)
            case 7:
                individual_student_report(stud)
            case 8:
                student_ranking_list(stud)
            case 9:
                print("exiting")
                break
            case _:
                print("invalid choice!")
    except ValueError:
        print("value must between 1 and 9:")

print("----Thank you----")




        
        
    
