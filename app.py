# Program Topic: Todo List CLI Application

# Importing Required Libraries

import pymongo
from datetime import datetime

# ========================================

# PyMongo Configuration

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["TodoListCLIApp"]
collection = db["Todos"]

# ========================================

# Making Required Functions

def addTodo(title, description, date_time):
    ''' Function to add a todo '''

    try:
        record = {
            "todo": "todo",
            "title": title,
            "description": description,
            "date_time": date_time
        }
        collection.insert_one(record)
        print("Todo Inserted Successfully!")
    except Exception as error:
        print(f"An error occurred:\n{error}")

def updateTodo(oldTitle, newtitle, newdescription):
    ''' Function to update a todo '''

    try:
        old = {
            "title": oldTitle
        }
        new = {
            "$set": {
                "title": newtitle,
                "description": newdescription
            }
        }
        collection.update_one(old, new)
        print("Todo Updated Successfully!")
    except Exception as error:
        print(f"An error occurred:\n{error}")
        

def deleteTodo(title):
    ''' Function to delete a todo '''

    try:
        toDel = {
            "title": title
        }
        collection.delete_one(toDel)
        print("Todo has been deleted successfully!")
    except Exception as error:
        print(f"An error occurred:\n{error}")

def viewTodos():
    ''' Function to view all the todos '''
    
    try:
        todos = collection.find(
            {
                "todo": "todo"
            },
            {
                "_id": 0,
                "title": 1,
                "description": 1
            }
        )
        print("App Todos are printed below:")
        for todo in todos:
            print(todo)
    except Exception as error:
        print(f"An error occurred:\n{error}")

# ========================================

# Main Logic for Todo List Application

if __name__ == '__main__':
    while True:
        try:
            task = int(input('''Enter the task number which you want to perform:\n1. Add a Todo\n2. Update a Todo\n3. Delete a Todo\n4. View All Todos\n5. Exit Application\n'''))
            if task == 1:
                title = input("Enter the title for your Todo: ")
                description = input("Enter the description for your todo: ")
                date_time = datetime.now().strftime("%d\n%B, %Y\n%H:%M\n%p")
                addTodo(title, description, date_time)
            elif task == 2:
                oldTitle = input("Enter the title of the todo which you want to update: ")
                newTitle = input("Enter the new title of your todo: ")
                newDescription = input("Enter the new description of your todo: ")
                updateTodo(oldTitle, newTitle, newDescription)
            elif task == 3:
                title = input("Enter the title of the todo which you want to delete: ")
                deleteTodo(title)
            elif task == 4:
                viewTodos()
            elif task == 5:
                print("Thank You for using Todo List CLI App")
                break
            else:
                print("Error: Task Not Found!")
        except Exception as error:
            print(f"An error occurred:\n{error}")

# ========================================