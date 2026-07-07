print("Hello, Welcome to-do-List App!")
tasks=[]
def view_tasks():
    for index, task in enumerate(tasks, start=1):
        print(f"{index}.{task}")

while True:
    print("TO-DO LIST MENU")
    menu = input(" choose a number- \n 1.Add \n 2.View\n 3.Delete\n 4. Exit \n")
    if menu=='1':
        add=str(input(" 1. Add a task \n"))
        tasks.append(add)
        print("List has been Added \n")
    elif menu=='2':
         view=input(" To view a list \n 'Hit Enter' ")
         view_tasks()
    elif menu=='3':
         if tasks==[]:
             print("Nothing to delete!")
         else:
             view_tasks()
             delete = int(input("Enter the number you wanted to delete from the list \n "))
             index=int(delete)-1
             if 1<= delete <= len(tasks):
                 tasks.pop(index)
                 print(f"List got deleted")
                 view_tasks()
             else:
                 print("invalid,Go to back Menu!")

    elif menu=='4':
        print("4. Exit")
        break
    else:
        print("In-Valid Try to choose again from the Menu")
