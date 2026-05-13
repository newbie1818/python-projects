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
            return json.load(f)

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

def main():
#downloading tasks
    global list_of_tasks
    list_of_tasks = load_tasks()
    while True:
        print("1. ADD TASK")
        print ("2. SHOW TASK")
        print ("3. DELETE TASK")
        print ("4. EXIT")

        choice = input("Choose an option ")

        if choice == "1":
            add_task()
            print("The task has been added")
        elif choice == "2":
            show_task()
        elif choice == "3":
            delete_task()
            print("Your task has been deleted")
        elif choice == "4":
            break

if __name__ == "__main__":
    main()




















