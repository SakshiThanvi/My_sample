                                                          #gmail_prototype
from datetime import datetime
import smtplib 
import random
import xlrd
import xlwt


def signup():
    print("\t\t welcome to GMAIL\n")

                                                            #input the details of the new user
    wb=xlwt.Workbook()
    ws=wb.add_sheet("sheet1")
    name=input("\t\nenter your name:-\n")
    ws.write(0,0,name)
    print("\t \t welcome",name)

    age=int(input("enter your age"))
    ws.write(0,1,age)
    username=input("enter your username")
    ws.write(0,2,username)
    password=input("enter your password")
    ws.write(0,3,password)
    altid=input("enter one alternate email ")
    ws.write(0,4,altid)
    contct=int(input("enter your contact number"))
    ws.write(0,5,contct)
    wb.save(".xls")
    otp_send(username)
                                                            #random generation of six digit numbers
    
        
            
def otp_send(uname):
    for i in range(1000000):
        OTP=random.randint(100001,1000001)

                                                             #send a mail via SMTP
    server=smtplib.SMTP('smtp.gmail.com',587)

    server.starttls()

    Id='111sakshi97@gmail.com'
    paswd='Jodhpur@123'

    msg=OTP
    msg=str(msg)

    server.login(Id,paswd)
    server.sendmail(Id,uname,msg)
    server.quit()  

    print(" enter the six digit OTP sent to your email for verification ")

    t=0
    otp=int(input())
    if(OTP==otp):         
        print("YOU ARE NOW A USER OF GMAIL")
    else:
        t=t+1
        if(t>3):
            print("error")
            exit()
        else:
            otp_send(uname)
    
    
        

    

#def signin():
    #uname=input("enter your username")
    #pasword=input("enter your password")

signup()
    
