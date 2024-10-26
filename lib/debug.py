# lib/seed.py
from models.job import Job
from models.applicants import Applicants
from models.interview import Interview

def seed_data():
    # Drop existing tables
    Applicants.drop_table()
    Job.drop_table()
    Interview.drop_table()

    # Create tables
    Job.create_table()
    Applicants.create_table()
    Interview.create_table()

    def seed_interviews():
        Interview.create("2024-10-15", "10:00 AM", "Scheduled", 1, 1)  # Alice Johnson, Software Engineer
        Interview.create("2024-10-16", "11:00 AM", "Completed", 2, 2)  # Bob Smith, Product Manager
        Interview.create("2024-10-17", "2:00 PM", "Pending", 3, 1)     # Charlie Lee, Software Engineer
        Interview.create("2024-10-18", "9:00 AM", "Scheduled", 4, 3)   # Dana White, Data Analyst
    
    print("Seeded Interviews:")
    print(Interview.get_all())

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
    seed_interviews()

if __name__ == "__main__":
    seed_data()


breakpoint()
