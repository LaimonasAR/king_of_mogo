import app
print("*************")
print("Welcome")
print("*************")

while True:

    choice = input("1 - enter task\n2 - find task\n3 - update task\n4 - delete task\n0 - exit\n")

    match choice:
        case '1':
            task_from_user = input("Plese enter task name: ")
            app.create_task(task_from_user, query = {"name": {task_from_user}})
            
        case '2': 
            find_task = input("Enter task to find: ")
            app.update_task(find_task, query = {"name": {find_task}})
        
        case '3':
            update_task = input("Enter task to update: ") 
            app.delete_task(update_task, query = {"name": {update_task}})

        case '4':
            del_task = input("Enter task to delete: ") 
            app.delete_task(del_task, query = {"name": {del_task}})

        case '0':
            print("Goodbye")
            break

        case other:
            print("Wrong command!!!")