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
    for job in Job.get_all():
        print(f"{job.id}. {job.title}")
        
def view_applicants(menu, current_job=None):
    try:
        id = int(input("---\n\nEnter the job ID you wish to see more information on\n"))
    except ValueError:
        print("Invalid input. Please enter a valid job ID.")
        back(menu)
        return

    for job in Job.get_all():
        if id == job.id:
            current_job = job
            print(f"---\nWhat information would you like to know about position {job.title}?")
            print(f"\n1. View Applicants: ")
            print(f"\n2. Create Application: ")
            print(f"\n3. Delete Job: ")
            try:
                choice = int(input("---\nEnter Choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                back(menu)
                return

            if choice == 1:
                applicants = current_job.applicants()
                if len(applicants) > 0:
                    print("---\nAPPLICANTS")
                    for i, applicant in enumerate(applicants, start=1):
                        if applicant:
                            print(f"\n{i}. {applicant.name}")
                else:
                    print("No Applicants")
                back(menu)
                return
            
            elif choice == 2:
                create_new_application(menu, job)

            elif choice == 3:
                choice_confirmation = input(f"---\nAre you sure you wish to delete this job: {current_job.title}? Y/N\n").upper()
                if choice_confirmation == "Y":
                    print(f"{current_job.title} deleted")
                    current_job.delete()
                    print("POOF")
                back(menu)
                return

            else:
                print("Invalid choice.")
                back(menu)
                return


     
def create_new_job(menu):
    job_title = input("Please enter the job title: ")
    Job.create(job_title)
    print(f"Job with title {job_title} created!")
    menu()

def view_all_jobs(menu): #getting all jobs
    print("---\nRetrieving jobs. . .\n")
    print_job_list()
    view_applicants(menu, current_job=None)      

def create_new_application(menu, job): #create new application1
    name = input("Enter name: ")
    try:
        job_id = job.id#take in a job object instead of job id
        new_app = Applicants.create(name, int(job_id))
        new_app
        print(f"---\nJob application #{new_app.id} created")
        print(f"---\nApplication for {Job.find_by_id(job_id).title} received.\n")
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


def exit_program():
    print("Goodbye!")
    exit()

# def helper_3(menu):  # Gets job by ID
    # print(f"Enter job you'd like to review (by ID)")
    # print_job_list()
    # job_found = False  # Initialize job_found before the loop
    # while not job_found:
    #     try:
    #         id = int(input("---\n Please enter job ID: \n---"))
    #         job_item = Job.find_by_id(id)
    #         if job_item:  # Check if the job is found
    #             print(f"Job with ID: {job_item.id} | Job Title: {job_item.title}")
    #             view_applicants(menu, job_item)
    #             job_found = True  # Exit loop once the job is found
    #         else:
    #             print("No job found with that ID. Please try again.")
    #     except ValueError:
    #         print("Please enter a valid integer for the job ID.")

        

    #     back(menu)
        


# def helper_4(): # fetch job by application number
#     try:
#         id = int(input("Please enter job ID: "))
#         applications = Job.find_by_id(id).applicants()
#         for applicant in applications:
#             print(f"--- \nApplication ID: {applicant.id}\nApplicant Name: {applicant.name}\nJob ID: {applicant.job_id}\n")
#         print(applications)
#     except:
#         print("Please enter an integer")

# def helper_5(): # delete job by ID
    # try:
    #     print_job_list()
    #     title = int(input("\n---\nEnter name of job you wish to delete: "))
    #     for job in Job.find_by_id():
    #         if title == job.title:
    #             print(f"\n---\nJob - {job.title} deleted")
    #             job.delete()
                
    #     else:
    #         print("Job with that name does not exist")
    # except:
    #     print("Please enter an integer")
