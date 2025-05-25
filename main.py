library = {
    "The Alchemist": {"author": "Paulo Coelho", "year": 1988},
    "1984": {"author": "George Orwell", "year": 1949}
}
while True:
  print("\n📚 Library Menu")
  print("1. Show all books")
  print("2. Add a book")
  print("3. Delete a book")
  print("4. Search for a book")
  print("5. Show book details")
  print("6. Exit")
  choice = input("Choose an option: ")
  match choice:
     case "1":
       print("\nBooks in the library:")
       for title, author in library.items():
          print(f"{title} by {author}")
     case "2" :
       add=input("enter a name of book ")
       author=input("enter a name of author")
       library[add]= author
       print(f"{add} by {author}")
     case "3" :
       rmov=input("enter the name of a book to remove ")
       del library[rmov]
       print("  beleted successfully of ",rmov)
     case "4":
       research=input("enter a tittle of book you want to research")
       for title , author in library.items():
         if title == research:
           print(f"{title} by {author}")
         else:
           print(f"this a title {research} not found")
     case "5" :
       book=input("enter the title to gave you the details")
       for title , author in library.items():
          if title == book:
            print(f" {author}")
          else:
           print(f"this a title {book} not found")
     case _ :
       print("invalid choice please try again.")
     case "6":
       print("good bye ")
       break 
            
     

  


  