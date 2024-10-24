#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb
from models.model_1 import Job_board, Applicants

# uncomment for reset upon debug
# Applicants.drop_table()
# Applicants.create_table()

# Job_board.drop_table()
# Job_board.create_table()

ipdb.set_trace()
