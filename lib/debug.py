#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb
from models.model_1 import job, Applicants

# uncomment for reset upon debug


job.create_table()
Applicants.create_table()

job.create("Marketer")
job.create("SEO Man")
Applicants.create("Jacob", 1)
Applicants.create("Mark", 1)
Applicants.create("James", 1)
Applicants.create("Jordan", 2)



ipdb.set_trace()

Applicants.drop_table()
job.drop_table()
