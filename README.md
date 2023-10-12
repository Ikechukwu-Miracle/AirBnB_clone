# 0x00. AirBnB clone - The console

This team project is part of the (Alx) Holberton School Software Engineering program.
It represents the first step towards building a full web application.

The Airbnb Clone project is a web application that aims to replicate the core functionalities of the Airbnb platform. It provides a platform for users to search, book, and list accommodations.

## The Console
In the project a custom CLI was used as console. This console serve as a way for the user to engage with the program.
The console is a sub class that inherits from the standard Python module Cmd.

**Usage:**
The CLI can be use in interactive or non-interactive modes by either call a command as follows:
<command> <argument1> <argument2> ...
Or typing: <class>.<command>()

Example:
(hbnb) create BaseModel
f35becf1-31be-4014-8cd1-60783ba4f8aa
(hbnb) all
["[BaseModel] (6c26dfea-23e1-4340-b567-14b70f4bfa0c) {'id': '6c26dfea-23e1-4340-b567-14b70f4bfa0c', 'created_at': datetime.datetime(2023, 10, 12, 11, 40, 35, 764246), 'updated_at': datetime.datetime(2023, 10, 12, 11, 40, 35, 764254), 'email': 'qrs@mail.com', 'int_no': '234'}", "[BaseModel] (8db07ea9-bf7d-49a8-8594-075cfbbff904) {'id': '8db07ea9-bf7d-49a8-8594-075cfbbff904', 'created_at': datetime.datetime(2023, 10, 12, 13, 4, 15, 834420), 'updated_at': datetime.datetime(2023, 10, 12, 13, 4, 15, 834426)}", "[User] (6d435786-a118-4e50-ad0c-86a734ae8f4d) {'id': '6d435786-a118-4e50-ad0c-86a734ae8f4d', 'created_at': datetime.datetime(2023, 10, 12, 20, 34, 55, 343710), 'updated_at': datetime.datetime(2023, 10, 12, 20, 34, 55, 343751), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", "[User] (9dd3a2be-0261-48f4-b502-9c8daaaf7b74) {'id': '9dd3a2be-0261-48f4-b502-9c8daaaf7b74', 'created_at': datetime.datetime(2023, 10, 12, 20, 34, 55, 345920), 'updated_at': datetime.datetime(2023, 10, 12, 20, 34, 55, 345976), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}", "[Review] (01edff60-2a44-462f-acc4-671ee1ac0c13) {'id': '01edff60-2a44-462f-acc4-671ee1ac0c13', 'created_at': datetime.datetime(2023, 10, 12, 20, 15, 20, 288438), 'updated_at': datetime.datetime(2023, 10, 12, 20, 15, 20, 288445), 'text': 'Beautiful'}", "[BaseModel] (f35becf1-31be-4014-8cd1-60783ba4f8aa) {'id': 'f35becf1-31be-4014-8cd1-60783ba4f8aa', 'created_at': datetime.datetime(2023, 10, 12, 20, 32, 7, 68940), 'updated_at': datetime.datetime(2023, 10, 12, 20, 32, 7, 68946)}"]
(hbnb) show Review 01edff60-2a44-462f-acc4-671ee1ac0c13
[Review] (01edff60-2a44-462f-acc4-671ee1ac0c13) {'id': '01edff60-2a44-462f-acc4-671ee1ac0c13', 'created_at': datetime.datetime(2023, 10, 12, 20, 15, 20, 288438), 'updated_at': datetime.datetime(2023, 10, 12, 20, 15, 20, 288445), 'text': 'Beautiful'}
(hbnb)
(hbnb) quit:
