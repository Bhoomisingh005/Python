import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='root')
cursor=conn.cursor()
cursor.execute("DROP DATABASE IF EXISTS `ABC Pharmacy`")
cursor.execute("CREATE DATABASE `ABC Pharmacy`")
cursor.execute("USE `ABC Pharmacy`")

s1='''CREATE TABLE employee
      ( UserID int PRIMARY KEY,
        Name varchar(50),
        Password varchar(10),
        Category varchar(10),
        CHECK(Category IN ('E','A')))'''
cursor.execute(s1)
data1=[(1233,'Arpan Banerjee','clock12*','E'),\
       (1234,'Mohini Patel','lmn123%','E'),\
       (1236,'Gauri Sen','singer#1','E'),\
       (1237,'John Watson','bond007$$','E'),\
       (6980,'Lionel Messi','fifa22$','A'),\
       (6981,'Neymar Jr.','copa21?','A')]
insert_stmt1='''INSERT INTO employee VALUES(%s,%s,%s,%s)'''
cursor.executemany(insert_stmt1,data1)

s2='''CREATE TABLE medicine
      ( `Medicine Name` varchar(30) UNIQUE,
        `No. of items` int,
         Rate float,
         CHECK(Rate > 0)) '''
cursor.execute(s2)
insert_stmt2='''INSERT INTO medicine VALUES(%s,%s,%s)'''
med_file=open('med_data.txt','r')
med_list=med_file.readline().rstrip('\n').split(',')
med_nos=med_file.readline().rstrip('\n').split(',')
med_rate=med_file.readline().rstrip('\n').split(',')
med_file.close()
for i in range(len(med_list)):
    cursor.execute(insert_stmt2,(med_list[i],med_nos[i],med_rate[i]))

conn.commit()
conn.close()

