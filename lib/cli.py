# lib/cli.py

from helpers import (
    exit_program,
    create_new_job,
    view_all_jobs,
)


def main():#
    # choice = ""
    menu()
    while True:
        
        choice = input("> ")
        if choice == "1":
            exit_program()
        elif choice == "2":
            create_new_job(menu)
        elif choice == "3":
            view_all_jobs(menu)
      
def menu():
    print("Please select an option:")
    print("1. Exit the program")
    print("2. Create a new job posting")
    print("3. Fetch all job postings")
    


if __name__ == "__main__":
    main()
