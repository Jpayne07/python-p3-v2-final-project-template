#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb
from models.model_1 import job, Applicants

# uncomment for reset upon debug


job.create_table()

Applicants.create_table()




ipdb.set_trace()

Applicants.drop_table()
job.drop_table()
