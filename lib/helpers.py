# lib/helpers.py
from models.model_1 import Applicants, job
def helper_1():
    job_title = input("Please enter the job title: ")
    job.create(job_title)
    print(f"Job with title {job_title} created!")

def helper_2(): #getting all jobs
    print("Retrieving jobs. . .")
    for job_item in job.get_all():
        print(f"Job Id: {job_item.id} | Job Title: {job_item.title}")

def helper_3(): #gets job by ID
    try:
        id = int(input("Please enter job ID: "))
        job_item = job.find_by_id(id)
        print(f"Job with ID: {job_item.id} | Job Title: {job_item.title}")
    except:
        print("Please enter an integer")

def helper_4(): # fetch job by application number
    try:
        id = int(input("Please enter job ID: "))
        applications = job.find_by_id(id).applicants()
        for applicant in applications:
            print(f"--- \nApplication ID: {applicant.id}\nApplicant Name: {applicant.name}\nJob ID: {applicant.job_id}\n")
        print(applications)
    except:
        print("Please enter an integer")

def helper_5(): # delete job by ID
    try:
        id = int(input("Enter ID of job you wish to delete: "))
        if item :=  job.find_by_id(id):
            print(f"Job - {item.title} deleted")
            item.delete()
            
        else:
            print("Job with that ID does not exist")
    except:
        print("Please enter an integer")

def helper_6(): #create new application1
    name = input("Enter name: ")
    try:
        job_id = int(input("\nEnter job ID: "))
        new_app = Applicants.create(name, int(job_id))
        new_app
        print(f"---\nJob application #{new_app.id} created")
        print(f"---\nApplication for {job.find_by_id(job_id).title} received.\n")
    except ValueError:
        print("Invalid input. Please enter an integer.")

def helper_7(): #fetch applications
    apps = Applicants.get_all()
    for app in apps:
        print(f"---\nApplication ID: {app.id}\nApplicant Name: {app.name}\nJob Title: {job.find_by_id(app.job_id).title}\n")

def helper_8(): #fetch application by id
    try:
        id =  int(input("Please enter the application ID: "))
        applicant = Applicants.find_by_id(id)
        print(f"---\nApplicant name: {applicant.name}\nApplication #: {applicant.id}\nApplicant Job Title: {job.find_by_id(applicant.id).title}\n---")
    except ValueError:
        print("Invalid input. Please enter an integer.")

def helper_9(): #Delete app
    try:
        id =  int(input("Please enter the job id: "))
        job_app = Applicants.find_by_id(id)
        print(f"Job application #: {job_app.id} deleted.")
        Applicants.delete(job_app)
    except ValueError:
        print("Invalid input. Please enter an integer.")

def helper_10(): #Delete app
    try:
        id_1=  int(input("Please enter the starting job id: "))
        id_2=  int(input("Please enter the ending job id: "))
        for i in range(id_1, id_2):
            job_app = Applicants.find_by_id(i)
            print(f"Job application #: {job_app.id} deleted.")
            Applicants.delete(job_app)
    except ValueError:
        print("Invalid input. Please enter an integer.")

    




def exit_program():
    print("Goodbye!")
    exit()


