'''file.manager.io'''

import os
from prompt_toolkit import prompt

def create_new_file():
    
    while True: 
        
        print("Press Enter to go back.")
        file_name = input("Write name of the file: ").strip()
        if file_name == "":
            print("You backed!")
            break
        else:
            if len(file_name) >= 1 and len(file_name) <= 15:
                with open(f"C:\\Users\\pc\\Downloads\\My_Projects\\Python\\07_file_handler\\files\\{file_name}", 'x') as f:
                    
                    print(f"file '{file_name}' created successfully!")
                    print("To go back press Esc + enter")
                    write_content = prompt("Write Content: ", multiline=True)
                    if write_content == "":
                        print("You backed!")
                        break
                    else:
                        while True:
                            print("Do you want to save it?")
                            print("1. yes")
                            print("2. No")
                            choice = input("Enter your choice (1 or 2): ").strip()
                            if choice == "1":
                                f.write(write_content)
                                
                                print(f"file content saved successfully!")
                                break
                            elif choice == "2":
                                print("Content does not saved!")
                                break
                            else:
                                print("Invalid choice!")
            else:
                print("length of files name should be in between 1 to 15!")

def view_files():
    folder_path = "C:\\Users\\pc\\Downloads\\My_Projects\\Python\\07_file_handler\\files"
    items_in_folder = os.listdir(folder_path) # os.listdir gives the list of the names of the files inside that folder whoes path is passed as an argument
    print("YOUR SAVED FILES :)")
    for index, item in enumerate(items_in_folder, start=1):
        print(f"{index}. {item}")
    while True:
        print("Do you want to UPDATE any of these file?")
        print("1. Yes.")
        print("2. No.")
        choice = input("Enter your choice(1 or 2): ").strip()
        if choice == "1":
            file_name_to_update = input("Enter the file name you want to update: ")
            file_path = f"C:\\Users\\pc\\Downloads\\My_Projects\\Python\\07_file_handler\\files\\{file_name_to_update}"
            file_exists = os.path.exists(file_path)
            if file_exists:
                with open(file_path, 'r') as f:
                    content_in_file = f.read()
                    update_content = prompt("Update you existing content: ", default=content_in_file, multiline=True)
                    while True:
                        print("Do you want to save changes?")
                        print("1. Yes.")
                        print("2. No.")
                        choice = input("Enter your choice(1 or 2): ")
                        if choice == "1":
                            with open(file_path, 'w') as f1:
                                f1.write(update_content)
                            print("Changes saved successfully!")
                            break
                        elif choice == "2":
                            print("Changes does not saved!")
                            break
                        else:
                            print("Invalid choice!")
                    
            else:
                print(f"File '{file_name_to_update}' does not exist!")
                
        elif choice == "2":
            print("You backed!")
            break
        else:
            print("Invalid choice!")

def rename_file():
    folder_path = "C:\\Users\\pc\\Downloads\\My_Projects\\Python\\07_file_handler\\files"
    items_in_folder = os.listdir(folder_path) # os.listdir gives the list of the names of the files inside that folder whoes path is passed as an argument
    print("SAVED FILES :)")
    for index, item in enumerate(items_in_folder, start=1):
        print(f"{index}. {item}")
    while True:
        print("Do you want to RENAME any of these file?")
        print("1. Yes.")
        print("2. No.")
        choice = input("Enter your choice(1 or 2 or press Enter to go back): ").strip()
      
        if choice == "1":
            file_name_to_rename = input("Enter the file name you want to rename: ")
            file_path = f"C:\\Users\\pc\\Downloads\\My_Projects\\Python\\07_file_handler\\files\\{file_name_to_rename}"
            file_name_to_rename_exists = os.path.exists(file_path)
            if file_name_to_rename_exists:
                new_file_name = input("Enter the new file name: ").strip()
                if len(new_file_name) >= 1 and len(new_file_name) <= 15:
                    new_file_path = f"C:\\Users\\pc\\Downloads\\My_Projects\\Python\\07_file_handler\\files\\{new_file_name}"
                    os.rename(file_path, new_file_path)
                    print(f"File '{file_name_to_rename}' renamed to '{new_file_name}' successfully!\n")
                else:
                    print("Length of files name should be in between 1 to 15!")
            else:
                print(f"File '{file_name_to_rename}' does not exist!")
        elif choice == "2":
            print("You backed!")
            break
        else:
            print("Invalid choice!")


def delete_files():
    folder_path = "C:\\Users\\pc\\Downloads\\My_Projects\\Python\\07_file_handler\\files"
    items_in_folder = os.listdir(folder_path) # os.listdir gives the list of the names of the files inside that folder whoes path is passed as an argument
    print("SAVED FILES :)")
    for index, item in enumerate(items_in_folder, start=1):
        print(f"{index}. {item}")
    while True:
        print("To go back press Enter")
        file_to_delete = input("Enter the name of file you want to delete: ").strip()
        if file_to_delete == "":
            print("You backed!")
            break
        else:
            file_path = f"C:\\Users\\pc\\Downloads\\My_Projects\\Python\\07_file_handler\\files\\{file_to_delete}"
            file_to_delete_exists = os.path.exists(file_path)
            if file_to_delete_exists:
                while True:
                    print("Are you sure you want to delete this file?")
                    print("1. Yes.")
                    print("2. No.")
                    choice = input("Enter your choice(1 or 2):")
                    if choice == "1":
                        os.remove(file_path)
                        print(f"File '{file_to_delete}' deleted successfully!")
                        break
                    elif choice == "2":
                        print("You backed!")
                        break
                    else:
                        print("Invalid choice!")
            else:
                print(f"File '{file_to_delete}' does not exist!")
                
while True:
    print("WELCOME TO file.manager.io :)")
    print("1. Create a new File.")
    print("2. View Files")
    print("3. Rename file")
    print("4. Delete Files")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        create_new_file()
    elif choice == "2":
        view_files()
    elif choice == "3":
        rename_file()
    elif choice == "4":
        delete_files()
    elif choice == "5":
        print("Thank you for using file.handler :)")
        break
    else:
        print("Invalid choice!") 