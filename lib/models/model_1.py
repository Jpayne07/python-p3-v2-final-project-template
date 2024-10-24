#handling imports
from __init__ import CURSOR, CONN

#creating the first model class
#one class
class Job_board:
    def __init__(self, job_title, company, location):
        self.job_title = job_title
        self.company = company
        self.location = location

#many class
class Applicants:
    all = [] #list of applicants
    def __init__(self, name, job_id):
        self.name = name
        self.job_id = job_id



