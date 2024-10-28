 
from models.applicants import Applicants
def view_job_applicants(back, menu, current_job):
    applicants = current_job.applicants()
    if len(applicants) > 0:
        print("---\nAPPLICANTS")
        for i, applicant in enumerate(applicants, start=1):
            if applicant:
                print(f"\n{i}. {applicant.name}")
        applicant_choice(back, menu, current_job, applicants)
            
        return
    else:
        print("No Applicants")
    back(menu)

def create_new_application(back, menu, job): #create new application1
    name = input("Enter name: ")
    try:
        Applicants.create(name, job.id)
        print(f"---\nApplication for {job.title} received.\n")
    except ValueError:
        print("Invalid input. Please enter an integer.")
    back(menu)

def applicant_choice(back, menu, current_job, applicants):
    try:
        # Prompt the user for their next action
        choice_confirmation = int(input("---\nWhat would you like to do next?\n1. Create new application\n2. Delete application\n3. Go back\n"))
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
            back(menu)
        else:
            print("---\nInvalid applicant number. Please try again.")
    elif choice_confirmation == 3:
        back(menu)
    else:
        print("---\nInvalid choice. Please select 1 or 2.")
