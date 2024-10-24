#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb
from models.model_1 import Job_board, Applicants

# uncomment for reset upon debug


Job_board.create_table()

Applicants.create_table()
# Applicants.drop_table()
# Job_board.drop_table()



ipdb.set_trace()
