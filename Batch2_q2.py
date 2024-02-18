'''  Here is an example dictionary. You may insert more data of choice. 
d-{'name': Ram', 'phone':9434141414','email': "ram@gmail.com }, 
{'name':Laksman','phone':"8434151515","}, 
{'name':*Bharat',' phone':7474161616', "email': 'bharat @gmail.com" }), 
{'name':Satrughna', phone':9478171717", 'email':'satrughna@gmail.com'}] 
(a) All the users whose phone number ends in 5 
Write a program in Python that reads the above dictionary and prints the following: 
(b) All the users that don't have an email address listed 
(c) All the users whose phone number starts with 9 '''

d = [
  {'name': 'Ram', 'phone': '9434141414', 'email': 'ram@gmail.com'},
  {'name': 'Laksman', 'phone': '8434151515'},
  {'name': 'Bharat', 'phone': '7474161616', 'email': 'bharat@gmail.com'},
  {'name': 'Satrughna', 'phone': '9478171717', 'email': 'satrughna@gmail.com'}
]

# (a) All the users whose phone number ends in 5

phone_end_5 =[]
for user in d:
  if user.get('phone','').endswith('5'):
    phone_end_5.append(user['name'])

print("Users whose phoe number ends in 5 :",phone_end_5)

# (b) All the users that don't have an email address listed
no_email =[]
for user in d:
  if 'email' not in user:
    no_email.append(user['name'])
print("Users whose email address is not listed :",no_email)

# (c) All the users whose phone number starts with 9
phone_start_9 =[]
for user in d:
  if user.get('phone','').startswith('9'):
    phone_start_9.append(user['name'])
print("Users whose phone number starts with 9",phone_start_9)