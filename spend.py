#!/usr/bin/env python3

from peewee import *
import argparse
import datetime

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

def add_income(amount, period):
    income = Income.create(amount, period)
    income.save()

def print_income():
    total_daily_income = 0.0
    for income in Income.select():
        total_daily_income += income.daily_amount()
        print(income.amount, income.period)
    print('Total daily income: ', total_daily_income)

def add_bill(amount, period):
        bill = Bill.create(amount, period)
        bill.save()

def print_bill():
    total_daily_bill = 0.0
    for bill in Bill.select():
        total_daily_bill += bill.dialy_amount()
        print(bill.amount, bill.period)
    print('Total daily bill: ', total_daily_bill)

def add_spend(amount):
    spend = Spend.create(amount)
    spend.save()

def print_spend():
    for spend in Spend.select():
        print(spend.id, spend.amount, spend.date)

def import_spending(file, format):
    print(file, format)

def print_all():
    print_income()
    print_bill()
    print_spend()

db.connect()
if not Income.table_exists():
    db.create_tables([Income, Bill, Spend])

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--print')

subparsers = parser.add_subparsers(dest='subcommand')

# spend command
spend_parser = subparsers.add_parser('spend')
spend_parser.add_argument('list')
spend_parser.add_argument('-a', '--add', nargs=1)
spend_parser.add_argument('-d', '--delete', nargs=1)

# income command
income_parser = subparsers.add_parser('income')
income_parser.add_argument('list')
income_parser.add_argument('-a', '--add',  nargs=2)
income_parser.add_argument('-d', '--delete', nargs=1)

# bill command
bill_parser = subparsers.add_parser('bill')
bill_parser.add_argument('list')
bill_parser.add_argument('-a', '--add', nargs=2)
bill_parser.add_argument('-d', '--delete', nargs=1)

import_parser = subparsers.add_parser('import')
import_parser.add_argument('file', nargs=1)
import_parser.add_argument('-f', '--format', nargs=1)

args = parser.parse_args()

if args.subcommand == 'spend':
    print('spend')
elif args.subcommand == 'income':
    print('income')
elif args.subcommand == 'bill':
    print('bill')
elif args.subcommand == 'import':
    print('import')
else :    
    print(args)

