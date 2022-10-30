# Description of the project

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

# Description of the command interpreter:
What's a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

[*] Create a new object (ex: a new User or a new Place)
[*] Retrieve an object from a file, a database etc…
[*] Do operations on objects (count, compute stats, etc…)
[*] Update attributes of an object
[*] Destroy an object
## How to start it

hbnb shell works like as shown bellow interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

## How to use it

Below are the examples of the commands that can be used on the hbnb shell:

### Launching the console
```
$ ./console.py
(hbnb) 
```
### Creating a new object
```
(hbnh) create
** class name missing **
(hbnb) create User
796d8678-df45-4a62-ba97-082ff116b4fd
```
### Show an object
```
(hbnb) show User
** instance not found **
(hbnb) show User 796d8678-df45-4a62-ba97-082ff116b4fd
[User] (796d8678-df45-4a62-ba97-082ff116b4fd) {'id': '796d8678-df45-4a62-ba97-082ff116b4fd', 'created_at': datetime.datetime(2022, 7, 1, 13, 36, 48, 407416), 'updated_at': datetime.datetime(2022, 7, 1, 13, 36, 48, 407527)}
```
### Update an object
```
(hbnb) update
** class name missing **
(hbnb) update User
** instance id missing **
(hbnb) update User 796d8678-df45-4a62-ba97-082ff116b4fd
** attribute name missing **
(hbnb) update User 7b8c7a8b-f45a-4484-b6e2-aaed70cdac61 name Javi
(hbnb) all
["[User] (796d8678-df45-4a62-ba97-082ff116b4fd) {'id': '796d8678-df45-4a62-ba97-082ff116b4fd', 'created_at': datetime.datetime(2022, 7, 1, 13, 40, 8, 489607), 'updated_at': datetime.datetime(2022, 7, 1, 13, 40, 8, 489622)}", "[User] (1fa18511-0fea-4a3c-a424-cea1f8ee01cc) {'id': '1fa18511-0fea-4a3c-a424-cea1f8ee01cc', 'created_at': datetime.datetime(2022, 7, 1, 13, 40, 17, 45444), 'updated_at': datetime.datetime(2022, 7, 1, 13, 40, 17, 45560), 'name': 'Javi'}"]
```
### Destroy an object
```
(hbnb) destroy
** class name missing **
(hbnb) destroy User
** instance id missing **
(hbnb) destroy User 796d8678-df45-4a62-ba97-082ff116b4fd
(hbnb)
```

### Exit the console
```
(hbnb) quit
defrancescomartin@LAPTOP-RFLPL88P:~/holbertonschool-AirBnB_clone$
```
