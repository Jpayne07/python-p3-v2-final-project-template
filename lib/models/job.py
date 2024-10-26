# lib/models/model_1.py
#handling imports
#need to break out class into separate files
from models.__init__ import CONN, CURSOR
from models.applicants import Applicants

#creating the first model class
#one class
class Job:

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
        return [cls.get_instance_from_db(row) for row in rows]
    
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
        return([Applicants.get_instance_from_db(row) for row in rows])


