# lib/helpers.py
from models.job import Job
from models.applicants import Applicants
def back(menu):
    while True:
        prompt = input("\n--- Press B to return to main menu, 0 to exit: ").upper()
        if prompt == 'B':
            menu()
            return
        elif prompt == '0':
            exit()
        else:
            print("Invalid input. Please try again.")

def print_job_list():
    i=1
    for job in Job.get_all():
        
        print(f"{i}. {job.title}")
        i += 1

def view_all_jobs(menu): #getting all jobs
    print("---\nRetrieving jobs. . .\n")
    print_job_list()
    view_applicants(menu, current_job=None)    
        
def view_applicants(menu, current_job=None):
    while True:
        try:
            # Get user input for job number and ensure it's a valid integer
            id = int(input("---\n\nEnter the job # you wish to see more information on\n"))
        except ValueError:
            # Handle case where input is not an integer
            print("Invalid input. Please enter a valid job #.")
            back(menu)
            return

        jobs = Job.get_all()

        # Adjust for 1-based indexing: Check if the job number is within valid range
        if 1 <= id <= len(jobs):
            # Find the job (adjust index to 0-based by subtracting 1)
            current_job = jobs[id - 1]
            print(f"---\nWhat information would you like to know about position {current_job.title}?")
            print(f"\n1. View Applicants: ")
            print(f"\n2. Create Application: ")
            print(f"\n3. Delete Job: ")
            
            try:
                # Get user input for the choice (1, 2, or 3)
                choice = int(input("---\nEnter Choice: "))
            except ValueError:
                # Handle invalid input for the choice
                print("Invalid input. Please enter a number.")
                back(menu)
                return

            # Handle user's choice
            if choice == 1:
                applicants = current_job.applicants()
                if len(applicants) > 0:
                    print("---\nAPPLICANTS")
                    for i, applicant in enumerate(applicants, start=1):
                        if applicant:
                            print(f"\n{i}. {applicant.name}")
                    # choice_confirmation = input("---\nWould you like to create a new application?Y/N\n").upper()
                    # if choice_confirmation == "Y":
                    applicant_choice(menu, current_job, applicants)
                        
                    back(menu)
                    return
                else:
                    print("No Applicants")
                back(menu)
                return
            
            elif choice == 2:
                create_new_application(menu, current_job)
                break

            elif choice == 3:
                delete_job_confirmation(menu, current_job)
                break

            else:
                print("Invalid choice.")
                back(menu)
                return
        else:
            # Handle case where job number is out of bounds
            print(f"No job found with the number {id}. Please try again.")
            continue

def create_new_job(menu):
    job_title = input("Please enter the job title: ")
    Job.create(job_title)
    print(f"Job with title {job_title} created!")
    menu()

  

def create_new_application(menu, job): #create new application1
    name = input("Enter name: ")
    try:
        Applicants.create(name, job.id)
        print(f"---\nApplication for {job.title} received.\n")
    except ValueError:
        print("Invalid input. Please enter an integer.")
    back(menu)

def fetch_all_applications(menu): #fetch applications
    apps = Applicants.get_all()
    for app in apps:
        print(f"\nApplication ID: {app.id}\nApplicant Name: {app.name}\nJob Title: {Job.find_by_id(app.job_id).title}\n---")
    while True:
        try:
            # Get input from the user for which application to view in detail
            view_app_next = int(input("Enter the application # you'd like more information on: "))
            
            # Check if the input corresponds to a valid application
            selected_app = Applicants.find_by_id(view_app_next)
            if selected_app:  # If application is found
                view_app(menu, selected_app)  # Pass the selected application to the next helper function
                break  # Exit the loop after successful selection
            else:
                print("No application found with that ID. Please try again.")
        except ValueError:
            print("Please enter a valid integer for the application ID.")

def view_app(menu, selected_app): #fetch application by id
    print(f"---\nNow viewing {selected_app.name}'s application.\n---")
        # Present options to the user
    while True:
        try:
            print(f"1. View Application\n2. Delete Application\n---")
            app_choice = int(input("Enter Choice (1 or 2): "))
            
            if app_choice in [1, 2]:
                handle_app_view_or_delete(menu, app_choice, selected_app)
                break
            else:
                print("Invalid choice. Please enter 1 to view or 2 to delete the application.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def handle_app_view_or_delete(menu, app_choice, app): #Delete app
    try:
        if app_choice == 1:
            print(f"---\nApplication ID: {app.id}\nApplicant Name: {app.name}\nJob Title: {Job.find_by_id(app.job_id).title}")
            back(menu)
        else:
            print(f"Job application #: {app.id} deleted.")
            app.delete()
            back(menu)
    except ValueError:
        print("Invalid input. Please enter an integer.")

def delete_job_confirmation(menu, current_job):
    choice_confirmation = input(f"---\nAre you sure you wish to delete this job: {current_job.title}? Y/N\n").upper()
    if choice_confirmation == "Y":
        print(f"{current_job.title} deleted")
        current_job.delete()
        print("POOF")
    else:
        back(menu)
    

def exit_program():
    print("Goodbye!")
    exit()

def applicant_choice(menu, current_job, applicants):
    try:
        # Prompt the user for their next action
        choice_confirmation = int(input("---\nWhat would you like to do next?\n1. Create new application\n2. Delete application\n"))
    except ValueError:
        print("---\nInvalid input. Please enter a number (1 or 2).")
        return

    if choice_confirmation == 1:
        # Call function to create a new application
        create_new_application(menu, current_job)
    elif choice_confirmation == 2:
        if not applicants:
            print("---\nNo applicants available to delete.")
            return
        
        # Display applicants and prompt for the number of the applicant to delete
        for i, applicant in enumerate(applicants, start=1):
            print(f"---\n{i}. {applicant.name}")
        
        try:
            # Ask for the applicant number to delete
            app_id = int(input("---\nChoose the number of the applicant you'll delete: "))
        except ValueError:
            print("---\nInvalid input. Please enter a valid number.")
            return

        # Check if the selected number is within the range of applicants
        if 1 <= app_id <= len(applicants):
            applicant_to_delete = applicants[app_id - 1]
            print(f"---\nDeleting applicant: {applicant_to_delete.name}")
            # Call the method to delete the selected applicant
            applicant_to_delete.delete()
            print("---\nApplicant deleted successfully.")
        else:
            print("---\nInvalid applicant number. Please try again.")
    else:
        print("---\nInvalid choice. Please select 1 or 2.")