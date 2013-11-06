import datetime
from dateutil import parser
from dateutil import relativedelta


class DateIncrementor(object):

    def increment(self, date, column_spec):
        step = column_spec['step']
        date = parser.parse(date, yearfirst=True)

        if step == 'year':
            next_date = date + relativedelta.relativedelta(years =+ 1)
        elif step == 'month':
            next_date = date + relativedelta.relativedelta(months =+ 1)
        elif step == 'day':
            next_date = date + relativedelta.relativedelta(days =+ 1)

        return next_date.strftime('%Y-%m-%d')
