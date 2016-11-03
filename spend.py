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


db.connect()
if not Income.table_exists():
    db.create_tables([Income, Bill, Spend])


class PositionalAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print('args: ', values)


class AddIncomeAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        income = Income.create(amount=values[0], period=values[1])
        income.save()


class ListIncomeAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print('Income:')
        total_daily_income = 0.0
        for income in Income.select():
            total_daily_income += income.daily_amount()
            print(income.amount, income.period)
        print('Total daily income: ', total_daily_income)


class AddBillAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        bill = Bill.create(amount=values[0], period=values[1])
        bill.save()


class ListBillAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print('Bill:')
        total_daily_bill = 0.0
        for bill in Bill.select():
            total_daily_bill += bill.dialy_amount()
            print(bill.amount, bill.period)
        print('Total daily bill: ', total_daily_bill)


class AddSpendAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if len(values) > 0:
            spend = Spend.create(amount=values[0])
            spend.save()


class ListSpendAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print('Spend:')
        for spend in Spend.select():
            print(spend.id, spend.amount, spend.date)


class PrintAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):

        listIncome = ListIncomeAction(option_string, dest=None)  # __init__
        listIncome(parser, namespace, values, None)  # __call__

        listBill = ListBillAction(option_string, dest=None)
        listBill(parser, namespace, values, None)
        
        listSpend = ListSpendAction(option_string, dest=None)
        listSpend(parser, namespace, values, None)


parser = argparse.ArgumentParser()
parser.add_argument('-p', '--print', nargs=0, action=PrintAction)

subparsers = parser.add_subparsers(dest='args')

# spend command
spend_parser = subparsers.add_parser('spend', help='list spending')
spend_parser.add_argument('list', nargs=0, action=ListSpendAction)
spend_parser.add_argument('-a', '--add', nargs=1, action=AddSpendAction)
spend_parser.add_argument('-d', '--delete', nargs=1)

# income command
income_parser = subparsers.add_parser('income', help='list income')
income_parser.add_argument('list', nargs=0, action=ListIncomeAction)
income_parser.add_argument('-a', '--add',  nargs=2, action=AddIncomeAction)
income_parser.add_argument('-d', '--delete', nargs=1)

# bill command
bill_parser = subparsers.add_parser('bill', help='list bill')
bill_parser.add_argument('list', nargs=0, action=ListBillAction)
bill_parser.add_argument('-a', '--add', nargs=2, action=AddBillAction)
bill_parser.add_argument('-d', '--delete', nargs=1)

import_parser = subparsers.add_parser('import')
import_parser.add_argument(file, nargs=1)
improt_parser.add_argument('-f', '--format', nargs=1)

args = parser.parse_args()
