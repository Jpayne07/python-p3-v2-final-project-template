# lib/helpers.py
from models.model_1 import Applicants, job
def helper_1():
    job_title = input("Please enter the job title: ")
    job.create(job_title)
    print(f"Job with title {job_title} created!")

def helper_2():
    print("Retrieving jobs. . .")
    job.get_all() #handled the print inside of the function so I can format the output better

def helper_3():
    find_job = input("Please enter job ID: ")
    job.find_by_id(find_job) #handled the print inside of the function so I can format the output better

def helper_4():
    job_applicants = input("Please enter job ID: ")
    job.find_by_id(job_applicants).applicants()

def helper_5():
    id = input("Enter ID of job you wish to delete: ")
    if item :=  job.find_by_id(id):
        item.delete()
    else:
        print("Job with that ID does not exist")




def exit_program():
    print("Goodbye!")
    exit()


