import app


user_name = input("Plese enter user name: ")
print("*************")
print(f"Welcome {user_name}")
print("*************")

while True:

    choice = input("1 - enter task\n2 - find task\n3 - update by task title\n4 - delete task by name\n0 - exit\n")

    match choice:
        case '1':
            task_title = input("Plese enter task title: ")
            task_description = input("Plese enter task desription: ")
            task_status = input("Plese enter task status: ")
            app.create_task({"name": user_name, "task_title": task_title, "task_desription": task_description, "task_status": task_status})
            
        case '2': 
            find_task = input("Enter task to find: ")
            tasks_list = app.find_task(query = {"name": user_name, "task_title": find_task})
            for task in tasks_list:
                print(task)


        case '3':
            print("Your tasks: ")
            tasks = app.find_task(querry= {"name": user_name})
            for task in tasks:
                print(task)

            update_task = input("Enter task title to update: ")
            print("Selected task: ")
            print(app.find_task(querry={"name": user_name, "task_title": update_task}))
            update_name = input("What do you want to update: ")
            update_value = input("enter new value: ")
            updates = app.update_task(query = {"task_title": update_task}, update= {update_name: update_value})
            print(updates)
            

        case '4':
            del_task = input("Enter task name to delete: ") 
            print(deleted_task = app.delete_task(query = {"name": del_task}))
            

        case '0':
            print("Goodbye")
            break

        case other:
            print("Wrong command!!!")