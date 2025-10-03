#Todo List Menu:
#1. View Tasks
#2. Add a Task
#3. Remove a Task
#4. Exit
#Enter Your choice:2
#Enter a new task: Buy Groceries
list = []
while True:
 a = input("enter a new task :")
 b = input("do you want to remove task :")
 d = input("do you want to stop:")
 if b == "yes":
   c = input("enter task to remove :")
   list.remove(c)
 list.append(a)
 [print(x) for x in list]
 if d == "yes":
  break

