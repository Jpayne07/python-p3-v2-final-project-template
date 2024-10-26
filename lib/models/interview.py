from models.__init__ import CONN, CURSOR
from models.applicants import Applicants  # Importing Applicant to handle relationships
from models.job import Job  # Importing Job to handle relationships

class Interview:
    all = {}  # dictionary of interviews saved to db

    def __init__(self, date, time, status, applicant_id, job_id, id=None):
        self.date = date
        self.time = time
        self.status = status
        self.applicant_id = applicant_id
        self.job_id = job_id
        self._id = id

    # repr placeholder for debugging
    def __repr__(self):
        return f"<Interview {self.id}: Applicant {self.applicant_id}, Job {self.job_id}, Status: {self.status}>"

    # create table
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS interviews(
                id INTEGER PRIMARY KEY,
                date TEXT,
                time TEXT,
                status TEXT,
                applicant_id INT,
                job_id INT,
                FOREIGN KEY (applicant_id) REFERENCES applicants(id),
                FOREIGN KEY (job_id) REFERENCES jobs(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    # drop table
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS interviews;
        """
        CURSOR.execute(sql)
        CONN.commit()

    # save interview instance to db
    def save(self):
        sql = '''
            INSERT INTO interviews (date, time, status, applicant_id, job_id)
            VALUES (?, ?, ?, ?, ?)
        '''
        CURSOR.execute(sql, (self.date, self.time, self.status, self.applicant_id, self.job_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    # create interview instance and save to db
    @classmethod
    def create(cls, date, time, status, applicant_id, job_id):
        # Ensure the applicant and job exist
        applicant = Applicants.find_by_id(applicant_id)
        job = Job.find_by_id(job_id)

        if applicant and job:
            interview = cls(date, time, status, applicant_id, job_id)
            interview.save()
            return interview
        else:
            raise Exception("Applicant or Job not found in the database.")

    # get all interviews from table
    @classmethod
    def get_all(cls):
        sql = '''
            SELECT * FROM interviews
        '''
        rows = CURSOR.execute(sql).fetchall()
        return [cls.get_instance_from_db(row) for row in rows]

    @classmethod
    def get_instance_from_db(cls, row):
        interview = cls.all.get(row[0])

        if interview:
            interview.date = row[1]
            interview.time = row[2]
            interview.status = row[3]
            interview.applicant_id = row[4]
            interview.job_id = row[5]
        else:
            interview = cls(row[1], row[2], row[3], row[4], row[5])
            interview.id = row[0]
            cls.all[interview.id] = interview
        return interview

    # find interview by ID
    @classmethod
    def find_by_id(cls, id):
        sql = '''
            SELECT * FROM interviews
            WHERE id = ?
        '''
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.get_instance_from_db(row) if row else None

    # delete interview
    def delete(self):
        sql = '''
            DELETE FROM interviews
            WHERE id = ?
        '''
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None
