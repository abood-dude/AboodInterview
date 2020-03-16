#Author: Abdel Hammad
import json
import mysql.connector

#Connect to database with already existing user database
mydb =  mysql.connector.connect (host="localhost",user="root",passwd="passwordabood",database="userdb")

mycursor = mydb.cursor()

#MySQL Query goes here to create table

mycursor.execute("CREATE TABLE userevents (date DATE, count INTEGER(10))")

#load json file
data = [json.loads(line) for line in open('data.json', 'r')]
modifiedData=[]
for d in data:
    if d["event_name"] == "user_engagement":
        modifiedData.append(d)

usersThreeSeconds = []
usersLessThreeSeconds = []
for d in modifiedData:
    for thing in d["event_params"]:
        if thing["key"] == "engagement_time_msec":
            if int(thing["value"]["int_value"]) >=3000:
                usersThreeSeconds.append(d)
            else:
                usersLessThreeSeconds.append(d)

#Get Unique Dates
uniqueDates = []
for d in usersThreeSeconds:
    if d["event_date"] not in uniqueDates:
        uniqueDates.append(d["event_date"])

for date in uniqueDates:
    count = 0
    for d in usersThreeSeconds:
        if d["event_date"] == date:
            count+=1
    
    query = ("INSERT INTO userdb.userevents (date, count) VALUES ("+date+","+str(count)+")")
    mycursor.execute(query)
    mydb.commit()

#Close Connection
mydb.close()

