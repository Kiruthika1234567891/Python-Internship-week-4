#______-----------BEGINNER LEVEL SMALL REAL - WORLD STYLE PROGRAMS------------_______________

# _____SIMPLE CALCULATOR(FUNCTIONS + LOOPS) → MENU-DRIVEN CALCULATOR WITH +, −, ×, ÷______
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b!= 0:
        return a/b
    else:
        return "Error!Division by ZERO."
print("👋 Welcome to Calculator!🧮")
result = None
while True:
    if result is None:
        try:
            n1= float(input("Enter a number:"))
            n2= float(input("Enter next number:"))
        except ValueError:
            print("Invalid Input!Numbers only.")
            continue
    else:
        n1=result
        try:
            n2=float(input(f"Current Result:{n1}  Enter next number: ")) 
        except ValueError:
            print("Invalid Input!Numbers only.")
            continue
    print("Select operations:➕ , ➖ , ✖️ 2, ➗ or Type 'exit' to Quit.")    
    op=input("Enter operation:")   
    if op.lower() =='exit':
        print("Exiting Calculator!🔚 GOOD BYE. ")
        break
    elif op == '+':
        result = add(n1,n2)
    elif op == '-':
        result = subtract(n1,n2)   
    elif op == '*':
        result = multiply(n1,n2)
    elif op == '/':
        result = divide(n1,n2)
    else:
        print("Invalid Operation!")    
        continue   
    print(f"Result:{result}") 
    choice = input("Press 'enter' to Continue. or  'r' to Reset. or 'exit' Quit." ).lower()   
    if choice == 'r':
        result = None
    elif choice == 'exit':
        print("Exiting Calculator!🔚GOOD BYE. ")
        break
    elif choice == '' :
        continue   

            
# _______NUMBER GUESSING GAME(RANDOM MODULE) → COMPUTER PICKS A NUMBER, USER GUESSES UNTIL CORRECT______
import random
print("Welcome to Number Guessing game!🎲")
secret_number = random.randint(1,100)
attempts = 0
while True:
    try:
        guess = int(input("Enter your Guesss, 1 to 100 ❓ "))
        attempts +=1
    except ValueError:
        print("Invalid! 🤔 Guess 1 to 100 only")    
        continue
    if guess < secret_number:
        print("Your Guess is too low 📉, Try Again ❓ ")
    elif guess > secret_number:
        print("Your Guess is too high 📈 , Try Again ❓ ")   
    else:
        print("\n🎉 Congratulations Your Guess is right ✅ .")  
        print(f"🔢 No.of attempts - {attempts}") 
        break  


# _____WORD COUNTER(STRINGS + DICTIONARY) → COUNT HOW MANY TIMES EACH WORD APPEARS IN A PARAGRAPh________
# _____WORD COUNTER USING DICTIONARY WITH IF - ELSE______
print("Welcome to Word Counter!")
paragraph = input("Enter a Paragraph: ")
words = paragraph.lower().split()
word_count = {}
for word in words:
    word = word.strip(".,!?;:\"'()[]{}")
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("\nWord Frequency:") 
for word,count in word_count.items():
    print(f"{word} : {count}")           
# _________WORD COUNTER USING COUNTER CLASS_________
from collections import Counter
print("Welcome to Word Counter!")
paragraph = input("Enter a Paragraph: ")
words = [word.strip(".,!?;:\"'()[]{}").lower() for word in paragraph.split()]
word_count = Counter(words)
print("\nWord Frequency:") 
for word,count in word_count.most_common():
    print(f"{word} : {count}") 


# ______TO-DO LIST(LIST + FILE HANDLING) → ADD, VIEW, AND REMOVE TASKS, SAVED IN A FILE______
Filename = "tasks.txt"
def load_tasks():
    try:
        with open(Filename,"r")as f:
            tasks = f.read().splitlines()
    except FileNotFoundError:
        tasks = []
    return tasks
def save_tasks(tasks):
    with open(Filename,"w")as f:
        for task in tasks:
            f.write(task + "\n")      
def view_tasks(tasks):
    if not tasks:
        print("No Tasks!")   
    else:
        print("\nYour Tasks:")   
        for i,task in enumerate(tasks,start=1):
            print(f"{i}.{task}")
print("Welcome to TO_DO List App📋")    
tasks = load_tasks()
while True:
    print("\nChoose an option:")
    print("1.Add_task ")
    print("2.View_task ")
    print("3.Remove_task ")
    print("4.Exit.")
    choice = input("\nEnter Your choice : ")
    if choice == "1":
        task = input("Enter Task:")
        tasks.append(task)
        save_tasks(tasks)
        print("Task added.")
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        view_tasks(tasks)
        try:
            n = int(input("Enter task number to remove:"))
            if 1 <= n <= len(tasks):
                removed = tasks.pop(n-1)
                save_tasks(tasks)
                print(f"Task '{removed}' removed.")
            else:
                print("Invalid task number!")    
        except ValueError:
            print("Enter a valid number.")
    elif choice == "4":
        print("Exiting...Your tasks are saved.")
        break
    else:
        print("Invalid choice.Select option 1 - 4 ?")
    

# NOTES APP (FILE HANDLING) → SAVE AND READ NOTES FROM A TEXT FILE.         
Filename ="notes.txt" 
def add_note(note):
    with open(Filename,"a")as f:
        f.write(note + "\n")
        print("Note saved.")
def view_notes():
    try:
        with open(Filename,"r")as f:
            notes = f.readlines()
            if notes:
                print("\nYour notes:")
                for note in notes:
                    print(note.strip())
            else:
                print("Notes not found!")        
    except FileNotFoundError:
        print("Note File not found!")  
print("Welcome to Notes App")
while True:
    print("\n1.Add_Notes.")   
    print("2.View_Notes.")   
    print("3.Exit_Notes.")  
    choice = input("\nEnter your choice: ")   
    if choice == "1":
      note = input("Enter the note:") 
      add_note(note)
    elif choice =="2":
        view_notes()    
    elif choice =="3":
        print("Exiting...bye!")  
        break
    else:
        print("Invalid Choice!")  











                     



        

