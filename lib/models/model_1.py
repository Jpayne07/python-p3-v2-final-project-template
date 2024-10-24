#handling imports
from models.__init__ import CONN, CURSOR

#creating the first model class
#one class
class Job_board:
    def __init__(self, job_title, id = None):
        
        self.id = id
        self.job_title = job_title
     
    
    #create table
    @classmethod
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

    #drop
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS jobs;
        """
        CURSOR.execute(sql)
        CONN.commit()
    #save
    def save(self):
        '''save instance to db'''
        sql = '''
            INSERT INTO jobs (title)
            VALUES (?)
        '''

        CONN.execute(sql, (self.name))
        CONN.commit()

    # create row
    @classmethod
    def create(cls, title):
        '''create instance and save to db'''
        job = cls(title)
        job.save()
        return job

    #get all

    #find by ID

#many class
class Applicants:
    all = [] #list of applicants
    def __init__(self, name, job_id, id = None):
        self.name = name
        self.job_id = job_id
        self._id = id
        Applicants.all.append(self)
        
    def __repr__(self):
        return (
            f"<Applicant {self.id}: {self.name} " +
            f"Job ID: {self.job_id}>"
        )
     
    #create table
    @classmethod
    def create_table(cls):
        '''will persist the attributes of applicants instances'''
        sql = """
            CREATE TABLE IF NOT EXISTS applicants(
            id INT PRIMARY KEY,
            name TEXT,
            job_id INT,
            FOREIGN KEY (job_id) references jobs(id)
            )
        """

        CURSOR.execute(sql)
        CONN.commit()

    #drop
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS applicants;
        """
        CURSOR.execute(sql)
        CONN.commit()

    #create
    @classmethod
    def create(cls, name, job_id)
    #save
   
    def save(self):
        '''save instance to db'''
        sql = '''
            INSERT INTO applicants (name, job_id)
            VALUES (?, ?)
        '''

        CONN.execute(sql, (self.name, self.job_id))
        CONN.commit()
    #get all

    #find by ID



