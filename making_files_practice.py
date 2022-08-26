from datetime import date
import time

def date_format(date_digit):
    if date_digit < 10:
        return '0' + str(date_digit)
    else:
        return str(date_digit)


def make_file_title():
    current_time = time.localtime()
    # year, month day(preceeding 0 if not)
    # check if hour is in 24 hour format 

    year = date_format(current_time.tm_year)
    month = date_format(current_time.tm_mon)
    day = date_format(current_time.tm_mday)
    hour = date_format(current_time.tm_hour)
    minute = date_format(current_time.tm_min)

    print(year)
    print(month)
    print(day)
    print(hour)
    print(minute)
    
    file_title = year+ "_"+month+"_"+day+"_"+hour+"_"+ minute + ".txt"
    return file_title 

def make_file(file_title):   
    # date, time heading and key for the titles of data 
    # try importing to matlab and seeing how it comes out
    with open(file_title, "w") as f:  
        f.write('this is a file to write too')

    return f


file_title = make_file_title()
make_file = make_file(file_title)