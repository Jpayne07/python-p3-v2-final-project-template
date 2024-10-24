#handling imports
from __init__ import CURSOR, CONN

#creating the first model class
#one class
class Job_board:
    def __init__(self, job_title, company, location):
        self.job_title = job_title
        self.company = company
        self.location = location
    
    #create table
    def create_table(cls):
        '''will persist the attributes of job instances'''
        sql = """
            CREATE TABLE IF NOT EXISTS jobs(
            id INT PRIMARY KEY,
            title TEXT
            )
        """

        CURSOR.execute(sql)
        CONN.commit()

    #save

    #get all

    #find by ID

#many class
class Applicants:
    all = [] #list of applicants
    def __init__(self, name, job_id):
        self.name = name
        self.job_id = job_id
        Applicants.all.append(self)

     
    #create
    def create_table(cls):
        '''will persist the attributes of applicants instances'''
        sql = """
            CREATE TABLE IF NOT EXISTS applicants(
            id INT PRIMARY KEY,
            name TEXT
            FOREIGN KEY (job_id) references jobs(id)
            )
        """

        CURSOR.execute(sql)
        CONN.commit()
    #save

    #get all

    #find by ID



