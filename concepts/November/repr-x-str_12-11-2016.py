"""
The goal of __repr__ is to be unambiguous.
The goal of __str__ is to be readable.
"""

import datetime

date_time = datetime.datetime.utcnow()

date_string_format = str(date_time) #date_string_format is a string (str of date_time)

print('Function str from date_time: {}'.format(str(date_time)))
print('Function repr from date_time: {}'.format(repr(date_time)))#print('Function str from date_string_format:{}'.format(str(date_string_format)))

print('Function str from date_string_format: {}'.format(str(date_string_format)))
print('Function repr from date_string_format: {}'.format(repr(date_string_format)))
