# lib/seed.py
from models.job import Job
from models.applicants import Applicants

def seed_data():
    # Drop existing tables
    Applicants.drop_table()
    Job.drop_table()

    # Create tables
    Job.create_table()
    Applicants.create_table()

    # Seed job data
    job_1 = Job.create("Software Engineer")
    job_2 = Job.create("Data Scientist")
    job_3 = Job.create("Product Manager")

    # Seed applicants data
    Applicants.create("Alice Johnson", job_1.id)
    Applicants.create("Bob Smith", job_1.id)
    Applicants.create("Charlie Adams", job_2.id)
    Applicants.create("Dana White", job_3.id)
    
    # Display seeded data
    print("\nSeeded Jobs:")
    for job in Job.get_all():
        print(f"Job ID: {job.id}, Title: {job.title}")

    print("\nSeeded Applicants:")
    for applicant in Applicants.get_all():
        print(f"Applicant ID: {applicant.id}, Name: {applicant.name}, Job ID: {applicant.job_id}")

if __name__ == "__main__":
    seed_data()


breakpoint()
