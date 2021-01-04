

def return_10():
    return 10

def add(num_1, num_2):
    num_3 = num_1 + num_2
    return num_3

def subtract(num_4, num_5):
    num_6 = num_4 - num_5
    return num_6

def multiply(num_7, num_8):
    num_9 = num_7 * num_8
    return num_9

def divide(num_10, num_11):
    num_12 = num_10 / num_11
    return num_12


def length_of_string(string):
    return len(string)


def join_string(string_1, string_2):
    string_3 = string_1 + string_2
    return string_3

def add_string_as_number(string_4, string_5):
    string_6 = int(string_4) + int(string_5)
    return string_6

# import calender for date conversion capabilities 

import calender

# converting month number given as arguement into string literal of given month
def number_to_full_month_name(month_num):
    return calender.month_name[month_num]

def number_to_short_month_name(month_num):
    return calender.month_abbr[month_num]

def volume_of_cube(num):
    return num ** 3

def reverse_string(str):
    return str[::-1]

def fahrenheit_to_celsius(fahr_value):
    celsius = (fahr_value - 32) / 1.8
    return (round(celsius, 1))