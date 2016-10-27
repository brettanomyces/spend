#!/usr/bin/env python

import sqlite3
import argparse

# TODO everything

# spend

# command options
# --set-income <amount> <period>
# --set-monthly-income <amount> 30
# --set-weekly-income <amount> 7
# --set-daily-income <amount> 1

# --add-bill <amount> <period>
# --add-montly-bill <amount> 30
# --add-weekly-bill <amount> 7
# --add-daily-bill <amount> 1
# note: add savings as bills

# --record-spend <amount>

# --show
# note: ouput graph of spending over last 30 days

# spn_description | spn_amount | spn_date
# bll_description | bll_amount | bll_period
# inc_description | inc_amount | inc_period

conn = sqlite3.connect('spend.db')

def isDatabaseSetup():
    c = conn.cursor()
    c.execute("""SELECT 1 FROM sqlite_master WHERE type='table' AND name='inc_income'""")
    if c.fetchone()[0] == 1:
        c.close()
        return True

    c.close()
    return False

if not isDatabaseSetup():
    c = conn.cursor()
    c.execute("""CREATE TABLE inc_income (inc_description text, inc_amount real, inc_period integer)""")
    c.execute("""CREATE TABLE bll_bill (bll_description text, bll_amount real, bll_period integer)""")
    c.execute("""CREATE TABLE spn_spend (spn_description text, spn_amount real, spn_date integer)""")
    c.close()

