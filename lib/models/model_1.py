# lib/models/model_1.py
#handling imports
from models.__init__ import CONN, CURSOR

#creating the first model class
#one class
class job:

    all = {} #dictionary of jobs saved to db
    def __init__(self, title, id = None):
        
        self.id = id
        self.title = title

    #name validation
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            raise Exception("Attribute title must be of type string")
     
    #create table
    @classmethod
    def create_table(cls):
        '''will persist the attributes of job instances'''
        sql = """
            CREATE TABLE IF NOT EXISTS jobs(
            id INTEGER PRIMARY KEY,
            title TEXT
            )
        """
        print("Creating jobs table")
        CURSOR.execute(sql)
        print("Table created")
        CONN.commit()

    #drop
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS jobs;
        """
        print("Dropping jobs table")
        CURSOR.execute(sql)
        print("Table dropped")
        CONN.commit()
    
    #save
    def save(self):
        '''save instance to db'''
        sql = '''
            INSERT INTO jobs (title)
            VALUES (?)
        '''

        CURSOR.execute(sql, (self.title,))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    # create row
    @classmethod
    def create(cls, title):
        '''create instance and save to db'''
        job = cls(title)
        job.save()
        return job
    
    #delete
    def delete(self):
        sql = '''
            DELETE from jobs 
            where id = ?
            '''
        CURSOR.execute(sql,(self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None



    #get all
    @classmethod
    def get_all(cls):
        '''return all rows from the jobs table'''
        sql = '''
            select * from jobs
        '''
        
        rows = CURSOR.execute(sql).fetchall() #store all selected rows as tuples
        for row in rows:
            print(f"Job Id: {row[0]} | Job Title: {row[1]}")
            return [cls.get_instance_from_db(row)]
    
    @classmethod
    def get_instance_from_db(cls, row):
        job = cls.all.get(row[0])
        if job:
            job.title = row[1]
        else:
            job = cls(row[1])
            job.id = row[0]
            cls.all[job.id] = job
        return job
    
    #find by ID
    @classmethod
    def find_by_id(cls, id):
        sql = '''
            SELECT * from jobs
            WHERE id = ?
            '''
        row  = CURSOR.execute(sql, (id,)).fetchone()

        if row:
            print(f"Job with ID: {cls.get_instance_from_db(row).id} | Job Title: {cls.get_instance_from_db(row).title}")
            return cls.get_instance_from_db(row) 
        else:
            None
    
   
        
    def applicants(self):
        sql = '''
            SELECT * FROM applicants
            where job_id = ?
            '''
        CURSOR.execute(sql,(self.id,))

        rows = CURSOR.fetchall()
        if self:
            print(f"Fetching applicants for {self.title} position")
        return [
            Applicants.get_instance_from_db(row) for row in rows
        ]


#many class
class Applicants:
    all = {}  #dictionary of applicants saved to db
    def __init__(self, name, job_id, id = None):
        self.name = name
        self.job_id = job_id #foreign key
        self._id = id #job id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception("Attribute name must be of type string")
        
    @property
    def job_id(self):
        return self._job_id
    
    @job_id.setter
    def job_id(self, job_id):
        if isinstance(job_id, int) and job.find_by_id(job_id):
            self._job_id = job_id
        else:
            raise Exception("Job id must exist in jobs table and must be of type integer")

    #repr placeholder so I can ensure this is working
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
            id INTEGER PRIMARY KEY,
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

    #save
    def save(self):
        '''save instance to db'''
        sql = '''
            INSERT INTO applicants (name, job_id)
            VALUES (?, ?)
        '''

        CURSOR.execute(sql, (self.name, self.job_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    #create
    @classmethod
    def create(cls, name, job_id):
        '''create instance and save to db'''
        applicant = cls(name, job_id)
        applicant.save()
        return applicant
    #get all

    @classmethod
    def get_all(cls):
        '''return all rows from the applicants table'''
        sql = '''
            select * from applicants
        '''

        rows = CURSOR.execute(sql).fetchall() #store all selected rows as tuples
        return [row for row in rows ]

    @classmethod
    def get_instance_from_db(cls, row):
        applicant = cls.all.get(row[0])
        
        if applicant:
            applicant.name = row[1]
            applicant.job_id = row[2]
        else: 
            applicant  = cls(row[1], row[2])
            applicant.id = row[0]
            cls.all[applicant.id] = applicant
        return applicant
    
    #find by ID
    @classmethod
    def find_by_id(cls, id):
        sql = '''
            SELECT * FROM applicants
            where id = ?
        '''

        row  = CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.get_instance_from_db(row) 
        else:
            None
        return cls.get_instance_from_db(row) if row else None
    
    def delete(self):
        sql = '''
            DELETE from applicants 
            where id = ?
            '''
        CURSOR.execute(sql,(self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None



