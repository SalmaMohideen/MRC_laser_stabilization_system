import time
from struct import *
import decode 

class live_stream():
    live_stream_status = False
        

    # corrects the format the date for file title 
    def date_format(self, date_digit):

        # will add 0's before single digits for length uniformity
        # and convert all integer dates to strings 
        if date_digit < 10:
            return '0' + str(date_digit)
        else:
            return str(date_digit)

    # creates a file title using the current data and time
    def make_file_title(self):
        current_time = time.localtime()
        
        # sends each part of the date to th format method to be formatted and converted into a string
        self.year = self.date_format(current_time.tm_year)
        self.month = self.date_format(current_time.tm_mon)
        self.day = self.date_format(current_time.tm_mday)
        self.hour = self.date_format(current_time.tm_hour)
        self.minute = self.date_format(current_time.tm_min)
        file_title = self.year+ "_"+self.month+"_"+self.day+"_"+self.hour+"_"+ self.minute + ".txt"
        self.file_title = file_title
        
        return file_title
     

    # this will create the text file and write a heading for the text file 
    def make_file(self, file_title):   

        # date, time heading and key for the titles of data 
        # try importing to matlab and seeing how it comes out
        start_date = self.year+ "_"+self.month+"_"+self.day 
        start_time = self.hour+"_"+ self.minute 

        with open(file_title, "w") as f:  
            f.write("Live stream started on: \n"+ "Date: "+ start_date +"\nTime:"+ start_time +"\n")
        f.close()
        return f

    # this function will retreive the data from the controller
    def get_data(self, ser):
        ser.open()
        ser.write(bytes(('S1S;'.encode())))
        reading_new = bytes(ser.read_until())
        ser.close() # close port
        return reading_new 
    
    # this will set the stream rate, begin the live stream, then writes data to the file with the date stamped 
    def produce_data(self, ser, running, file_name):
        # prompts the user to choose a stream rate 
        sleep_time_input = int(input ('Please enter: \n  1. 1 shot/second \n  2. 2 shots/second\n 3. 1 shot/minute\n 4. 1 shot/2 minutes\n'))
        
        # default sleep time is once per minute 
        sleep_time = 60
       
        # sets the stream rate based on the user input
        if sleep_time_input == 1:
            sleep_time = 1
        if sleep_time_input == 2:
            sleep_time = 0.5
        if sleep_time_input == 3:
            sleep_time = 60
        if sleep_time_input == 4: 
            sleep_time = 120
        
        # if an invalid option entered then stream rate defaults to 1/min 
        else: 
            print('ivalid entry, the stream rate has defaulted to 1/min')

        ser.close()
        f = open(file_name , "a" )  

        # this will retrieve data, format it, and add it to the value 
        while running == True :
            f.flush()

            # formats and adds the time/date stamp next to the data 
            current_data = self.get_data(ser)
            current_time = time.localtime()
            year = self.date_format(current_time.tm_year)
            month = self.date_format(current_time.tm_mon)
            day = self.date_format(current_time.tm_mday)
            hour = self.date_format(current_time.tm_hour)
            minute = self.date_format(current_time.tm_min)
            time_stamp = year+"_"+month+"_"+day+"_"+hour+"_"+minute
           
            # this will write to the file
            f.write('\n')
            f.write(time_stamp + '\n')
            f.write (decode.decode_byte_to_ints(current_data))
            f.write('\n\n')

            # sleeps until the next data needs to be collected 
            time.sleep(sleep_time)
        
        f.close()

    # stops the data live stream and closes the file writer 
    def end_stream(self, f):
        print("Ending the live stream\nThe data is in:", self.file_title )
        self.live_stream_status = False
        f.close()

