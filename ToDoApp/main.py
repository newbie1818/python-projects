import json
import os
PATH ="task/task.json"
list_of_tasks = []

def load_tasks():
    os.makedirs("task", exist_ok=True)
    if not os.path.exists(PATH):
        return list_of_tasks
    else:
        with open (PATH, "r") as f:
            content = json.load(f)
            return content
def show_task():
    for i in list_of_tasks:
        if i['progress']:
            print(f"{i['id']}, {i['title']}, [X]")
        else:
            print(f"{i['id']}, {i['title']}, []")
def save_tasks(list_of_tasks):
    with open(PATH,"w") as f:
        json.dump(list_of_tasks, f, indent=2)

def add_task():
    task = input("Write down a task: ")
    task_id = len(list_of_tasks)+1
    dic = {"id":task_id, "title":task, "progress": False}
    list_of_tasks.append(dic)
    save_tasks(list_of_tasks)

def delete_task():
    # show tasks
    show_task()
    id_to_delete = input("Enter a number of the task you want to delete")
    # ask id. if id is not int throw error
    try:
        id_to_delete = int(id_to_delete)
    except ValueError:
        print("This is not a number. Enter a number: ")

    # get task with the required id
    for i in list_of_tasks:
        if i["id"] == id_to_delete:
            list_of_tasks.remove(i)
    # save the updated list
    save_tasks(list_of_tasks)


















