tasks=[]
finish=[]

def view_list():
    print ()
    if tasks:
        for i in tasks:
            print (i)
    else:
        print("No tasks available")
    
def add_task():
    print ()
    task = input("Enter a task: ")
    tasks.append(task)
    print (f"Task {tasks[-1]} added successfully")

def remove_task():
    print ()
    view_list()
    print ()
    remove=input("Enter the task you want to delete: ")
    if remove in tasks:
        tasks.remove(remove)
        print (f"Task {remove} deleted successfully")
    else:
        print (f"Task {remove} not found")

def finish_task():
    print ()
    if finish:
        for i in finish:
            print (i)
    else:
        print("No tasks finished")

def update_task():
    view_list()
    print ()
    update=input("Enter the task you finished: ")
    if update in tasks:
        finish.append(update)
    else:
        print (f"Task {update} not found")
    tasks.remove(update)

def edit_task():
    view_list()
    print ()
    edit=input("Enter the task you want to edit: ")
    if edit in tasks:
        edit_task=input("Enter the new task: ")
        tasks.remove(edit)
        tasks.append(edit_task)
    else:
        print (f"Task {edit} not found")
    print (f"Task {edit} edited successfully")


def main():
    n=1
    while n:
        print ()
        print("1. View task")
        print ("2. Add task")
        print("3. Remove task")
        print ("4. Update task")
        print("5. Finished task")
        print ("6. Edit task")
        print ("7. Exit")
        print ()
        n=int(input("Enter the choice"))
        if n==1:
            view_list()
        elif n==2:
            add_task()
        elif n==3:
            remove_task()
        elif n==4:
            update_task()
        elif n==5:
            finish_task()
        elif n==6:
            edit_task()
        elif n==7:
            print()
            print("Exiting the program")
            break
        else:
            print("Invalid choice")

main()      