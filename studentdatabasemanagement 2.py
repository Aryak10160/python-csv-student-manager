import csv
import os

L=[]

def load():
    if os.path.exists("student_data.csv"):
        with open("student_data.csv","r") as f:
            reader=csv.reader(f)
            for row in reader:
                L.append(row)


def save():
    with open("student_data.csv","w",newline="") as f:
        writer=csv.writer(f)
        writer.writerows(L)

def insert():
    stu_id=input('enter student ID: ')
    Reg=input('enter student registration no.: ')
    name=input('enter student name: ')
    gen=input('enter gender of student: ')
    br=input('enter branch of student: ')
    yr=input('enter year of student: ')
    L1=[stu_id, Reg, name, gen, br, yr]
    L.append(L1)
    save()
    print("record inserted!")

def delete():
    n=input('enter student id to delete: ')
    for i in L:
        if i[0]==n:
            L.remove(i)
            save()
            print("record deleted!")
            return
    print("student id not found")

def upd():
    n=input('enter student ID: ')
    b=input('updated value of year: ')
    for i in L:
        if i[0]==n:
            i[5]=b
            save()
            print("updated!")
            return
    print("student id not found")

def dis():
    n=input('enter student ID: ')
    for i in L:
        if i[0]==n:
            print(i)
            return
    print("student id not found")

load()   
while True:
    print('====Menu====')
    print('1. insert data')
    print('2. display data')
    print('3. delete data')
    print('4. update year')
    print('5. display all')
    print('6. exit')
    n = int(input('enter your choice: '))
    if n==1:
        insert()
    elif n==2:
        dis()
    elif n==3:
        delete()
    elif n==4:
        upd()
    elif n==5:
        print(L)
    elif n==6:
        save()
        break