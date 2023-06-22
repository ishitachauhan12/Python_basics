import json
import random

# Opening JSON file
f = open('MOCK_DATA.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
# for i in data['student_data']:
#     print(i)
   
marks = dict()

# Find topper list aggregating the marks in respective courses
def topperlist():
        col, row = (2, 20)
        marks = [[ 1 for x in range(col)] for y in range (row)]
        k=0
        for i in data['student_data']:
            sum=0
            count=0
            for j in i['marks']:
                sum += i['marks'][j]
                count +=1
            marks[k][1]= sum/count
            marks[k][0]=i["roll_no"]
            k+=1

        marks.sort(key = lambda x: x[1],reverse=True)
        #print(marks)
        return marks

#or
# for i in data['student_data']:
#     sum=0
#     count=0
#     for j in i['marks']:
#         # print(i['marks'][j])
#         sum += i['marks'][j]
#         count +=1
#     marks[i['roll_no']] = sum/count

# topperDict = dict()

# for i in marks:
#     for j in data['student_data']:
#         if i==j['roll_no']:
#             topperDict[j['first_name'] +" "+ j['last_name']] = marks[i]

# topperlist=sorted(((value, key) for (key,value) in topperDict.items()),reverse=True)
# for i,j in topperlist:
#     print(j,i)

# Elect monitor randomly
def monitor():
    monitor=random.choice(marks)
    print(monitor[0]," you are monitor!")


# Find student available to vote
def student_available_to_vote() :
    available_to_vote = list()
    for i in data['student_data']:
        if i['age'] > 17:
            available_to_vote.append(i['first_name']+i['last_name'])
            print(i['first_name']+" "+i['last_name'])


# Find student with more than 50% in maths
def students_with_marks_more_than_50_in_maths():
    for i in data['student_data']:
        if i['marks'].get('maths')!=None:
            mark = i['marks']['maths']
        if mark > 49:
            print(i['first_name']+" "+i['last_name'])


# Students failed in section B in any subject (<33.3%)
def student_failed():
    failed = list()
    for i in data['student_data']:
        for j in i['marks']:
            if i['marks'][j] < 33.33:
                failed.append(i['first_name']+" "+i['last_name'])
    print(failed)


# Girls with obc quota
def girls_with_obc_quota():
    girls_with_obc = list()
    for i in data['student_data']:
        if i['caste'].lower() == 'obc' and i['gender'].lower()=='f':
            girls_with_obc.append(i['first_name']+i['last_name'])
            print(i['first_name']+" "+i['last_name'])


# Update section of topper students to A if not A
def update_section():
    list = topperlist()
    topper = list[0:3]
    topper2 = list[0:3]

    for i in topper:
        topper2.append(i[0])
        
    # print(topper)
    for i in data["student_data"]:
        if(i['roll_no'] in topper2):
            i['sec']='A'
            print(i['sec'])

# Remove gender column, its inappropiate to ask gender
def delete_gender():
    for i in data["student_data"]:
        del i['gender']
    print(data)

update_section()

updated_data = json.dumps(data)

with open('MOCK_DATA.json','w') as file:
    file.write(updated_data)
# Closing file
f.close()