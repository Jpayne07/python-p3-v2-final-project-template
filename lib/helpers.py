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
        find_job = int(input("Please enter job ID: "))
        job_item = job.find_by_id(find_job)
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

def helper_5():
    try:
        id = int(input("Enter ID of job you wish to delete: "))
        if item :=  job.find_by_id(id):
            item.delete()
        else:
            print("Job with that ID does not exist")
    except:
        print("Please enter an integer")

def helper_6(): #create new application
    name = input("Enter name")
    try:
        job_id = int(input("Enter job ID"))
        print("The entered number is:", job_id)
        Applicants.create(name, int(job_id))
    except ValueError:
        print("Invalid input. Please enter an integer.")

def helper_7(): #fetch applications
    Applicants.get_all()

def helper_8(): #fetch application by id
    try:
        id =  int(input("Please enter the application ID: "))
        Applicants.find_by_id(id)
    except ValueError:
        print("Invalid input. Please enter an integer.")

def helper_10(): #Delete app
    try:
        id =  int(input("Please enter the job id: "))
        job_app = Applicants.find_by_id(id)
        Applicants.delete(job_app)
    except ValueError:
        print("Invalid input. Please enter an integer.")

    




def exit_program():
    print("Goodbye!")
    exit()


