#handling imports
from models.__init__ import CONN, CURSOR

#creating the first model class
#one class
class job:

    all = {} #dictionary of jobs saved to db
    def __init__(self, title, id = None):
        
        self.id = id
        self.title = title
     
    
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

    #get all
    @classmethod
    def get_all(cls):
        '''return all rows from the jobs table'''
        sql = '''
            select * from jobs
        '''

        rows = CURSOR.execute(sql).fetchall() #store all selected rows as tuples
        return [row for row in rows ]
    
    @classmethod
    def get_instance_from_db(cls, row):
        job = cls.all.get(row[0])
        if job:
            job.title = row[1]
        else:
            job = cls(row[1])
            job.id = row[0]
        return job
    #find by ID
    @classmethod
    def find_by_id(cls, id):
        sql = '''
            SELECT * from jobs
            WHERE id = ?
            '''
        row  = CURSOR.execute(sql, (id,)).fetchone()
        return cls.get_instance_from_db(row) if row else None
    
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
        


#many class
class Applicants:
    all = {}  #dictionary of applicants saved to db
    def __init__(self, name, job_id, id = None):
        self.name = name
        self.job_id = job_id #foreign key
        self._id = id #job id
        Applicants.all.append(self) #adding applicants to all list

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
    def create(cls, title, job_id):
        '''create instance and save to db'''
        job = cls(title, job_id)
        job.save()
        return job
    #get all
    @classmethod
    def get_all(cls):
        '''return all rows from the applicants table'''
        sql = '''
            select * from applicants
        '''

        rows = CURSOR.execute(sql).fetchall() #store all selected rows as tuples
        return [row for row in rows ]

    #find by ID



