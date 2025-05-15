to_do=[]
while True :
  print  ("--- Task Manager ---")
  add=int(input("1. Add task\n2. View tasks\n3. Mark task as done\n4. Delete task\n5. Exit\n Choose an option:" ))
  if add==1:
    task=input("enter the task:")
    to_do.append(task)
    print("task added")
  elif add==2:
    print("tasks:")
    for i in range(len(to_do)):
      print(to_do[i])
  elif add==3:
    task=input("enter the task you want to mark as don ")
    to_do.append(f"*{task} done*")
    print(f"your to do list :\n {to_do}")
    
  elif add==4:
    task=input("enter the task to delete:")
    if task in to_do:
      to_do.remove(task)
      print(f"task deleted \n your to do list is:\n{to_do}")
  elif add==5:
    break
  else:
    print("invield choice ")
print("welcome ")
    