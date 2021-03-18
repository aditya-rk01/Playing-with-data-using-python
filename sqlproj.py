import mysql.connector as sqltor
import matplotlib.pyplot as plt
import numpy as np

mycon=sqltor.connect(host="localhost",user="root",passwd="Kayalvizhi@1",database="SQLPROJ")
if mycon.is_connected():
    print("Succesfully connected to database")
cursor=mycon.cursor()

#Taking Data from database
cities=['New York','London','Hampshair','Bangalore','Torento']
cursor.execute("select count(*) from customer where CUST_CITY='%s'"%('New York'))
data=cursor.fetchall()
cursor.execute("select count(*) from customer where CUST_CITY='%s'"%('London'))
data.append(cursor.fetchone())
cursor.execute("select count(*) from customer where CUST_CITY='%s'"%('Hampshair'))
data.append(cursor.fetchone())
cursor.execute("select count(*) from customer where CUST_CITY='%s'"%('Bangalore'))
data.append(cursor.fetchone())
cursor.execute("select count(*) from customer where CUST_CITY='%s'"%('Torento'))
data.append(cursor.fetchone())
count=list()
for i in range(len(data)):
    count.append(data[i][0])

cursor.execute("select avg(OPENING_AMT) from customer where CUST_CITY='%s'"%('New York'))
data1=cursor.fetchall()
cursor.execute("select avg(OPENING_AMT) from customer where CUST_CITY='%s'"%('London'))
data1.append(cursor.fetchone())
cursor.execute("select avg(OPENING_AMT) from customer where CUST_CITY='%s'"%('Hampshair'))
data1.append(cursor.fetchone())
cursor.execute("select avg(OPENING_AMT) from customer where CUST_CITY='%s'"%('Bangalore'))
data1.append(cursor.fetchone())
cursor.execute("select avg(OPENING_AMT) from customer where CUST_CITY='%s'"%('Torento'))
data1.append(cursor.fetchone())
open_amt=list()
for i in range(len(data1)):
    open_amt.append(data1[i][0])

cursor.execute("select max(RECEIVE_AMT) from customer where CUST_CITY='%s'"%('New York'))
data2=cursor.fetchall()
cursor.execute("select max(RECEIVE_AMT) from customer where CUST_CITY='%s'"%('London'))
data2.append(cursor.fetchone())
cursor.execute("select max(RECEIVE_AMT) from customer where CUST_CITY='%s'"%('Hampshair'))
data2.append(cursor.fetchone())
cursor.execute("select max(RECEIVE_AMT) from customer where CUST_CITY='%s'"%('Bangalore'))
data2.append(cursor.fetchone())
cursor.execute("select max(RECEIVE_AMT) from customer where CUST_CITY='%s'"%('Torento'))
data2.append(cursor.fetchone())
receive_amt=list()
for i in range(len(data2)):
    receive_amt.append(data2[i][0])

cursor.execute("select sum(PAYMENT_AMT) from customer where CUST_CITY='%s'"%('New York'))
data3=cursor.fetchall()
cursor.execute("select sum(PAYMENT_AMT) from customer where CUST_CITY='%s'"%('London'))
data3.append(cursor.fetchone())
cursor.execute("select sum(PAYMENT_AMT) from customer where CUST_CITY='%s'"%('Hampshair'))
data3.append(cursor.fetchone())
cursor.execute("select sum(PAYMENT_AMT) from customer where CUST_CITY='%s'"%('Bangalore'))
data3.append(cursor.fetchone())
cursor.execute("select sum(PAYMENT_AMT) from customer where CUST_CITY='%s'"%('Torento'))
data3.append(cursor.fetchone())
pay_amt=list()
for i in range(len(data3)):
    pay_amt.append(data3[i][0])

cursor.execute("select min(OUTSTANDING_AMT) from customer where CUST_CITY='%s'"%('New York'))
data4=cursor.fetchall()
cursor.execute("select min(OUTSTANDING_AMT) from customer where CUST_CITY='%s'"%('London'))
data4.append(cursor.fetchone())
cursor.execute("select min(OUTSTANDING_AMT) from customer where CUST_CITY='%s'"%('Hampshair'))
data4.append(cursor.fetchone())
cursor.execute("select min(OUTSTANDING_AMT) from customer where CUST_CITY='%s'"%('Bangalore'))
data4.append(cursor.fetchone())
cursor.execute("select min(OUTSTANDING_AMT) from customer where CUST_CITY='%s'"%('Torento'))
data4.append(cursor.fetchone())
outstand_amt=list()
for i in range(len(data4)):
    outstand_amt.append(data4[i][0])

#Storing these values in a dictionary
values={}
for i in range(5):
    values[cities[i]]=[open_amt[i],receive_amt[i],pay_amt[i],outstand_amt[i]]
print(values)

#Displaying the database the database
#print("Cities","Opening Amount","Receiving Amount","Payment amount","Outsatnding amount")
#for i in range(5):
#    print(cities[i],avg_open_amt[i],avg_receive_amt[i],avg_pay_amt[i],avg_outstand_amt[i], sep ="\t")

#Bar chart
plt.bar(cities,pay_amt,color=['r','g','b','black','violet'])
plt.xlabel('Payment amount')
plt.ylabel('Cities')
plt.title('Bar Graph showing payment amount details in diffrent cities')
plt.show()

#Multiple Bar Chart
x=np.arange(5)
plt.bar(x+0.00,open_amt,width=0.25,label='Opening amount')
plt.bar(x+0.25,receive_amt,width=0.25,label='Receive amount')
plt.xticks(x,cities)
plt.legend(loc='upper right')
plt.xlabel('Amount')
plt.ylabel('Cities')
plt.title('Bar Graph showing amount details in diffrent cities')
plt.show()

#Pie chart
plt.pie(outstand_amt,labels=cities,explode=[0,0.2,0.15,0.1,0.2])
plt.xlabel('Outstanding amount')
plt.ylabel('Cities')
plt.title('Bar Graph showing Outstanding amount details in diffrent cities')
plt.show()
