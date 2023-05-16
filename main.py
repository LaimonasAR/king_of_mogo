import app


user_name = input("Plese enter user name: ")
print("*************")
print(f"Welcome {user_name}")
print("*************")

while True:

    choice = input("1 - enter task\n2 - find task\n3 - update task\n4 - delete task\n0 - exit\n")

    match choice:
        case '1':
            task_title = input("Plese enter task title: ")
            task_description = input("Plese enter task desription: ")
            task_status = input("Plese enter task status: ")
            app.create_task({"name": user_name, "task_title": task_title, "task_desription": task_description, "task_status": task_status})
            
        case '2': 
            find_task = input("Enter task to find: ")
            app.update_task(query = {"name": user_name, "task_title": find_task})
        
        case '3':
            update_task = input("Enter task to update: ") 
            app.delete_task(query = {"task_title": update_task})

        case '4':
            del_task = input("Enter task to delete: ") 
            app.delete_task(query = {"name": del_task})

        case '0':
            print("Goodbye")
            break

        case other:
            print("Wrong command!!!")