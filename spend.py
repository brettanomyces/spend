#!/usr/bin/env python

from peewee import *
import argparse
import datetime

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

    def daily_amount(self):
        return self.amount / self.period


class Bill(Model):
    amount = DoubleField()
    period = IntegerField()

    class Meta:
        database = db

    def daily_amount(self):
        return self.amount / self.ieriod

class Spend(Model):
    amount = DoubleField()
    date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

db.connect()
if not Income.table_exists():
    db.create_tables([Income, Bill, Spend])

class AddIncomeAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print('%r %r %r' % (namespace, values, option_string))

        income = Income.create(amount=values[0], period=values[1])
        income.save()

class AddBillAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print('%r %r %r' % (namespace, values, option_string))

        bill = Bill.create(amount=values[0], period=values[1])
        bill.save()

class SpendAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print('%r %r %r' % (namespace, values, option_string))

        spend = Spend.create(amount=values[0])
        spend.save()

class PrintAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):

        print('Income:')
        total_daily_income = 0.0
        for income in Income.select():
            total_daily_income += income.daily_amount()
            print(income.amount, income.period)
        print('Total daily income: ', total_daily_income)
        
        print('Bill:')
        total_daily_bill = 0.0
        for bill in Bill.select():
            total_daily_bill += bill.dialy_amount()
            print(bill.amount, bill.period)
        print('Total daily bill: ', total_daily_bill)

        print('Spend:')
        for spend in Spend.select():
            print(spend.amount, spend.date)

parser = argparse.ArgumentParser(description='Process commandline input')
parser.add_argument('--add-income', nargs=2, action=AddIncomeAction)
parser.add_argument('--add-bill', nargs=2, action=AddBillAction)
parser.add_argument('--spend', nargs=1, action=SpendAction)  # TODO allow user to enter date
parser.add_argument('--print', nargs=0, action=PrintAction)
args = parser.parse_args()
