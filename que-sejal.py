from random import choice
import random
import xlrd

i=1
wb = xlrd.open_workbook(r"CurrencyDataFile.xlsx")
sh1 = wb.sheet_by_index(0)
list = []
u=int(input("enter number of question papers u want:"))
for j in range(0,u):
    for i in range(1,3):
        column =2
        x = choice(sh1.col(column)).value
        print(str(i)+". what is the fullform of "+str(x)+" ?"+"\n")
        for row in range(sh1.nrows):
            column = 2
            if(sh1.cell_value(row,column)== x) :
                y = row
        list1 = [1,2,3]
        z = random.choice(list1)
        column = 1
        if( z == 1):
            p = sh1.cell(y,1)
            print('     1. '+p.value+'   2. '+choice(sh1.col(column)).value+'   3. '+choice(sh1.col(column)).value+"\n")    
        elif( z == 2):
            p = sh1.cell(y,1)
            print('     1. '+choice(sh1.col(column)).value+'   2.'+p.value+'   3.'+choice(sh1.col(column)).value+"\n")
        elif(z==3):
            p = sh1.cell(y,1)
            print('     1. '+choice(sh1.col(column)).value+'   2.'+ choice(sh1.col(column)).value+'   3.'+p.value+"\n")
        i+=1
        list.append(p.value)
    i=3
    for i in range(3,5):
        column =1
        x = choice(sh1.col(column)).value
        print(str(i)+ ". what is the shortform of "+x+" ?"+"\n")    
        for row in range(sh1.nrows):
            column = 1
            if(sh1.cell_value(row,column)== x) :
                y = row
        list1 = [1,2,3]
        z = random.choice(list1)
        column = 2
        if( z == 1):
            p = sh1.cell(y,2)
            print('     1. '+p.value+'   2.'+choice(sh1.col(column)).value+'   3.'+choice(sh1.col(column)).value+"\n")        
        elif( z == 2):
            p = sh1.cell(y,2)
            print('     1. '+choice(sh1.col(column)).value+'   2.'+p.value+'   3.'+choice(sh1.col(column)).value+"\n")
        elif(z==3):
            p = sh1.cell(y,2)
            print('     1. '+choice(sh1.col(column)).value+'   2.'+ choice(sh1.col(column)).value+'   3.'+p.value+"\n")
        i+=1
        list.append(p.value)
    i=5
    for i in range(5,7):
        column = 1
        x = choice(sh1.col(column)).value
        print(str(i)+ ". what is the price of "+x+" ?"+"\n")
        for row in range(sh1.nrows):
            column = 1
            if(sh1.cell_value(row,column)== x) :
                y = row
        list1 = [1,2,3]
        z = random.choice(list1)
        column = 3
        if( z == 1):
            p = sh1.cell(y,3)
            print('     1. '+str(p.value)+'   2.'+str(choice(sh1.col(column)).value)+'   3.'+str(choice(sh1.col(column)).value)+"\n")        
        elif( z == 2):
            p = sh1.cell(y,3)
            print('     1. '+str(choice(sh1.col(column)).value)+'   2.'+str(p.value)+'   3.'+str(choice(sh1.col(column)).value)+"\n")
        elif(z==3):
            p = sh1.cell(y,3)
            print('    1.'+str(choice(sh1.col(column)).value)+'  2.'+ str(choice(sh1.col(column)).value)+'  3.'+str(p.value)+"\n")
        i+=1
        list.append(p.value)
    print("\nANSWERS:")
    for i in range(0,6):
        print(str(i+1)+".  "+str(list[i]))
    list.clear()
    print("\n")
