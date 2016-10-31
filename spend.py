#!/usr/bin/env python

from peewee import *
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

db = SqliteDatabase('spend.db')

class Income(Model):
    amount = DoubleField()
    period = IntegerField()

    class Meta:
        database = db

class Bill(Model):
    amount = DoubleField()
    period = IntegerField()

    class Meta:
        database = db

class Spend(Model):
    amount = DoubleField()
    date = DateTimeField()

    class Meta:
        database = db

db.connect()
db.create_tables([Income, Bill, Spend])

class AddIncomeAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print('%r %r %r' % (namespace, values, option_string))

class AddBillAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print('%r %r %r' % (namespace, values, option_string))

class SpendAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print('%r %r %r' % (namespace, values, option_string))

class PrintAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print('%r %r %r' % (namespace, values, option_string))

parser = argparse.ArgumentParser(description='Process commandline input')
parser.add_argument('--add-income', nargs=2, action=AddIncomeAction)
parser.add_argument('--add-bill', nargs=2, action=AddBillAction)
parser.add_argument('--spend', nargs=1, action=SpendAction)  # TODO allow user to enter date
parser.add_argument('--print', nargs=0, action=PrintAction)
args = parser.parse_args()
