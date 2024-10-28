# lib/helpers.py
from models.job import Job
from models.applicants import Applicants
from helpers_application import view_job_applicants
from helpers_application import create_new_application
def back(menu): #this is the back function to return to main menu
    while True:
        prompt = input("\n--- Press B to return to main menu, 0 to exit: ").upper()
        if prompt == 'B':
            menu()
            return
        elif prompt == '0':
            exit()
        else:
            print("Invalid input. Please try again.")

def print_job_list():#this prints all of the jobs
    i=1
    for job in Job.get_all():
        if (job):
            print(f"{i}. {job.title}")
            i += 1
        else:
            print("No jobs available")

def view_all_jobs(menu): #getting all jobs and opening the next prompt
    print("---\nRetrieving jobs. . .\n")
    print_job_list()
    view_applicants(back, menu, current_job=None)    
        
def view_applicants(back, menu, current_job=None): #this views all applicants of a job
    while True:
        try:
            id = int(input("---\n\nEnter the job # you wish to see more information on\n"))
        except ValueError:
            print("Invalid input. Please enter a valid job #.")
            back(menu)
            return

        jobs = Job.get_all()

        if 1 <= id <= len(jobs):
            current_job = jobs[id - 1]
            view_jobs_printer(current_job)
            
            try:
                choice = int(input("---\nEnter Choice: "))

            except ValueError:
                print("Invalid input. Please enter a number.")
                back(menu)
                return

            # Handle user's choice
            if choice == 1:
                view_job_applicants(back, menu, current_job)
                break
            
            elif choice == 2:
                create_new_application(back, menu, current_job)
                break

            elif choice == 3:
                delete_job_confirmation(menu, current_job)
                break

            else:
                print("Invalid choice.")
                back(menu)
                return
        else:
            print(f"No job found with the number {id}. Please try again.")
            continue

def create_new_job(menu): #tree 2.0
    job_title = input("Please enter the job title: ") #2.1
    Job.create(job_title) #creates the job with the input from the previous line
    print(f"Job with title {job_title} created!")
    menu() #gives the user the menu again


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
        back(menu)
    else:
        back(menu)
    

def exit_program():
    print("Goodbye!")
    exit()

def view_jobs_printer(current_job):
    print(f"---\nWhat information would you like to know about position {current_job.title}?")
    print(f"\n1. View Applicants: ")
    print(f"\n2. Create Application: ")
    print(f"\n3. Delete Job: ")