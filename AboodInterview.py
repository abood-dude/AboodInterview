import json

#Author: Abdel Hammad
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

# mysql.connect()
# mysql.createTable("active_user_table")
# mysql.createColumn(date)
# mysql.createColumn(active_user_count)
uniqueDates = []
for d in usersThreeSeconds:
    if d["event_date"] not in uniqueDates:
        uniqueDates.append(d["event_date"])

for date in uniqueDates:
    count = 0
    for d in usersThreeSeconds:
        if d["event_date"] == date:
            count+=1
    print(date)
    print(count)
    # mysql.addValueToDate(date)
    # mysql.addCounttoUserCount(count)

