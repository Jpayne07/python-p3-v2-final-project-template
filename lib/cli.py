# lib/cli.py

from helpers import (
    exit_program,
    helper_1,
    helper_2,
    helper_3,
    helper_4,
    helper_5,
    helper_6,
    helper_7,
    helper_8,
    # helper_8,
    # helper_9,
    helper_10
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        elif choice == "2":
            helper_2()
        elif choice == "3":
            helper_3()
        elif choice == "4":
            helper_4()
        elif choice == "5":
            helper_5()
        elif choice == "6":
            helper_6()
        elif choice == "7":
            helper_7()
        elif choice == "8":
            helper_8()
        # elif choice == "9":
        #     helper_9()
        elif choice == "10":
            helper_10()
        


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create a new job posting")
    print("2. Fetch all job postings")
    print("3. Fetch job by id: ")
    print("4. Fetch job applicants by job id: ")
    print("5. Delete job by job id: ")
    print("6. Create new application: ")
    print("7. Fetch all applications: ")
    print("8. Fetch application id: ")
    print("9. Fetch applications by job id: ")
    print("10. Delete application: ")


if __name__ == "__main__":
    main()
