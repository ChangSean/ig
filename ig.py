import json

filenames = ['ig1.json','ig2.json','ig3.json','ig4.json','ig5.json']
data_dict = {}
for filename in filenames:
    file_path = filename
    with open(file_path,"r",encoding='utf-8') as file:
        data = json.load(file)

    data_dict[filename] = data

    print(len(data))

print(data_dict.keys())

print(data_dict['ig3.json'][0]['username'])

usernames = {}
for filename, data in data_dict.items():
    print('正在處理',filename,'的資料')
    for follower in data:
        username = follower['username']
        if username not in usernames:
            usernames[username] = 1
        else:
            usernames[username] += 1

print(len(usernames))

followed_1 = 0
followed_2 = 0
followed_3 = 0
followed_4 = 0
followed_5 = 0

for username, count in usernames.items():
    if count == 1:
        followed_1 += 1
    elif count == 2:
        followed_2 += 1
    elif count == 3:
        followed_3 += 1
    elif count == 4:
        followed_4 += 1
    elif count == 5:
        followed_5 += 1

print('只追蹤一次的人數:', followed_1)
print('只追蹤二次的人數:', followed_2)
print('只追蹤三次的人數:', followed_3)
print('只追蹤四次的人數:', followed_4)
print('只追蹤五次的人數:', followed_5)