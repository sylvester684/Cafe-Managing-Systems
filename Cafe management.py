Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import mysql.connector
db=mysql.connector.connect(user="root" ,password="stilton" ,
                           host="localhost" ,database="cafe")
mycur=db.cursor()
print("1.Show all tables\n"
      "2.Read data from specific tables\n"
      "3.Write data into tables \n"
      "4.Delete data from tables")
mono= int(input ("What do you want to execute"))


#1.Show complete tables.

if mono ==1:
    print("1.Bill\n" "2.Menu\n"  "3.Storage" )
    h=int(input("Enter the no. of the table you want to see :"))
    if h ==1:
        s="Select * from bill"
        mycur.execute(s)
        dataa=mycur.fetchall()
        
        for row in dataa:
            print()
            print('Bill no',row[0])
            print('bill date',row[1])
            print('item',row[2])
            print('quantity',row[3])
            print('price',row[4])
            
    elif h==2:
        s="Select * from menu"
        mycur.execute(s)
        dataa=mycur.fetchall()
        for row in dataa:
            print()
            print('item name :',row[0])
            print('Price :',row[1])


    elif h == 3:
        s="Select * from storage"
        mycur.execute(s)
        dataa=mycur.fetchall()
        for row in dataa:
            print()
            print('Item :',row[0])
            print('Quantity :',row[1])
            print('Ordered :',row[2])
            print('Delivery date :',row[3])
    else:
        print("Data not found. ")


#2.Read data from tables
        
if mono==2:
    print("1.Bill\n" "2.Menu\n" "3.Storage" )
    n=int(input("Enter the no. of the table you want to see :"))


    #Read data from table 'bill'
    if n == 1:
        print("1.Show complete Table\n""2.Show table using Bill_no\n"
              "3.Show table using Bill Date\n"
              "4.Show  table using item\n""5.Show table using Price\n"
              "6.Show table using Quantity\n")
        o=int(input("Which function do you want to perform ? "))
        if o == 1:
            bs= "select * from bill"
            mycur.execute(bs)
        elif o ==2:
            bf="select * from bill where bill_no =  "
            j=input("enter bill no. :")
            w=(bf + j)
            mycur.execute(w)
            
        elif o ==3:
            bg="select * from bill where bill_date = "
            k=input("enter bill_date(in single quotations) :")
            q=(bg + k)
            mycur.execute(q)
        elif o== 4:
            bge="select * from bill where item = "
            ko=input("enter item name  :")
            qp=(bge +ko)
            mycur.execute(qp)
           
        elif o ==5:
            bgt="select * from bill where price "
            kop=input("enter symbol :")
            kopl=input ("enter price :")
            qplk=(bgt + kop+kopl)
            mycur.execute(qplk)
            
        elif o ==6:
            bgt="select * from bill where quantity "
            kop=input("enter symbol :")
            kopl=input ("enter quantity :")
            qplk=(bgt + kop+kopl)
            mycur.execute(qplk)
    dataa=mycur.fetchall()
    for row in dataa:
        print()
        print('Bill No. :',row[0])
        print('Bill Date :',row[1])
        print('Item :',row[2])
        print('Quantity :',row[3])
        print('Price :',row[4])
    

    #Read data from table 'Menu'
    if n== 2:
        print("1.Show complete Table\n""2.Show table using item\n""3.Show table using Price")
        y=int(input("which function do you want to perform "))
        if y == 1:
            by= "select * from menu"
            mycur.execute(by)
            
        elif y ==2:
            byu="select item from menu "
            mycur.execute(byu)
           
        elif y ==3:
            byui="select * from menu where price "
            krt=input("enter symbol :")
            kyuio=input ("enter price :")
            qyui=(bgt + krt+kyuio)
            mycur.execute(qyui)
    dataa=mycur.fetchall()
    for row in dataa:
        print()
        print('Item :',row[0])
        print('Price :',row[1])


    #Read data from table 'storage'        
    if n==3:
        print("1.Show complete Table\n""2.Show table using Item\n"
              "3.Show table using Ordered Column\n"
              "2.Show  table using Delivery Date\n")
        z=int(input("which function do you want to perform "))
        if z==1:
            nu= "select * from storage"
            mycur.execute(nu)
            

        elif z ==2:
            nuy="select item from storage "
            mycur.execute(nuy)
            
        elif z==3:
            noui="select * from storage where ordered ="
            nqt=input("YES or NO :")
            if nqt.lower=="yes":
                nkyui=(noui + nqt+nkuio)
                mycur.execute(nkyui)
            elif nqt.lower=="no":
                nkyui=(noui + nqt+nkuio)
                mycur.execute(nkyui)
            else:
                print("invalid response")
            
        elif z==4:
            npui="select * from storage where delv_date  "
            npt=input("enter date :")
            npyui=(npui + npt)
            mycur.execute(npyui)
    dataa=mycur.fetchall()
    for row in dataa:
        print()
        print('Item :',row[0])
        print('Quantity :',row[1])
        print('Ordered :',row[2])
        print('Delivery date :',row[3])




#3.Insert data into tables.
        
if mono ==3:
    print("1.Bill\n" "2.Menu\n"  "3.Storage" )
    h=int(input("Enter the no. of the table you want to insert data into :"))

    # Insert Values into table 'Bill'
    if h==1:
        Blno=int(input("Enter the Bill_No. :"))
        Bldt=input("Enter  the date in (YYYY-MM-DD) form : ")
        Item=input("enter the item name :")
        Qnt=int(input("Enter the quantity :"))
        Prc=int(input("Enter the price : "))
        mycur.execute("insert into bill values('" + str(Blno) + "','" + Bldt + "','" + Item + "','" +str(Qnt) + "','"+str(Prc)+"')")
        print('Entry sucessful')
        db.commit()

    if h==2:
        Item=input("Enter the item name :")
        Qnt=int(input("Enter the quantity :"))
        
        mycur.execute("insert into menu values('" + Item + "','" +str(Qnt) + "')")
        print('Entry sucessful ')
        db.commit()

    if h==3:
        
        Item=input("Enter the item name :")
        Qnt=int(input("Enter the quantity :"))
        ordr=input("Enter YES or NO")
        dlvdt=input("Enter  the date in (YYYY-MM-DD) form : ")
        mycur.execute("insert into bill values('" +Item+"','"+str(Qnt)+"','"+ordr+"','"+dlvdt+"')")
        print('Entry sucessful')
        db.commit()
         

# 4.Deleting Data.

if mono ==4 :
    print("1.Bill\n" "2.Menu\n"  "3.Storage" )
...     n= int(input("Enter a no."))
...     
...     # for table 'bill'
...     if n==1 :
...         e=input("Enter Bill No. to delete : ")
...         qu="delete from bill where billno= "
...         query=(qu+e)
...         mycur.execute(query)
...         db.commit()
...         if mycur.rowcount>0:
...             print("deletion successfull...")
...         else:
...             print("Bill_no not found")
...     #for table 'menu'
...     if n==2 :
...         e=input("Enter Item to delete : ")
...         qu="delete from menu where item = "
...         query=(qu+e)
...         mycur.execute(query)
...         db.commit()
...         if mycur.rowcount>0:
...             print("deletion successfull...")
...         else:
...             print("Item not found")
...     #for table 'storage'
...     if n==3 :
...         e=input("Enter Item to delete : ")
...         qu="delete from storage where item = "
...         query=(qu+e)
...         mycur.execute(query)cha
...         db.commit()
...         if mycur.rowcount>0:
...             print("deletion successfull...")
...         else:
...             print("Item not found")
... 
... 
... 
... 
