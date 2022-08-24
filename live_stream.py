from curses import KEY_B2
import time
import serial  
from struct import *
import decode_test

# To Do:
# make each file have a heading at the top
# currectly format the date and time
# time_stamp each data 

class live_stream():
    live_stream_status = False

    def __init__(self):
        live_stream_status = False
        file_title = ''
        year = 0
        month = 0
        day = 0
        hour = 0
        minute = 0
        
        
        
    # # function which retreives the current data from the controller 
    # def get_data(ser):
    #     ser.open()
    #     ser.write(bytes(('S1S;'.encode())))
    #     reading_new = bytes(ser.read_until())
    #     print(reading_new )
    #     ser.close() # close port


    # # funtion to write data to a text file 
    # def produce_data(self, ser, running, file_title):
    #     # prompts the user to enter a streaming rate 
    #     sleep_time = 1//int(input ('Please enter: \n  1. 1 shot/second \n  2. 2 shots/second'))
       
    #     # opens the file and infinitley continues to write data to the file 
    #     with open(file_title, "w") as f:  
    #             f.write('this is a file to write too')
    #             while self.live_stream_status == True :
    #                 self.get_data(ser)
    #                 time.sleep(sleep_time)
            
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

    
    def get_data(self, ser):
        # ser = serial.Serial('/dev/cu.usbserial-D308C1SJ', bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout = 1, write_timeout=1, rtscts=False, dsrdtr=False, xonxoff= True,inter_byte_timeout = 1, exclusive= None)  # open serial port
        # ser.baudrate = 115200 
        ser.open()
        ser.write(bytes(('S1S;'.encode())))
        reading_new = bytes(ser.read_until())
        print(reading_new)
        ser.close() # close port
        return reading_new 

    # def decode_byte_data(self, data_byte_string):

    #     format = 'hhhHhhHhhhc'
    #     # stuff = b'\x00;\x06\x06\x00\x06\x00\x06\x00*\x00\xb9\xfc\x87\x01\xaa\x9d\x9bmk;'

    #     stuff = b'\x00;\x06\x06\x00\x06\x00\x06\x00*\x00\xb2\xfc\xbb\x01\xc5\x9b\x99jl;'

    #     beam_diameter_1 = float(1)
    #     beam_diameter_2 = float(1)

    #     x_position_1 = float(0)
    #     x_position_2 = float(0)

    #     y_position_1 = float(0)
    #     y_position_2 = float(0)


    #     data_map = {} 
    #     position_map = {}

    #     un_stuff = unpack(format,stuff)
    #     print (un_stuff)
    #     # packed  = pack(format, un_stuff[0], un_stuff[1],  un_stuff[2],  un_stuff[3], un_stuff[4],  un_stuff[5],  un_stuff[6],un_stuff[7],un_stuff[8], un_stuff[9], un_stuff[10])
    #     objects_order = ['DX1', 'DY1', 'DI1','DX2','DY2', 'DI2', 'RX1', 'RY1','RX2', 'RY2', ';']

    #     for i in range (len(un_stuff)-1):
    #         data_map[objects_order[i]] = (un_stuff[i]) 
    #         # print (objects_order[i] , ":  " , (un_stuff[i]))


    #     x_position_1 = data_map['DX1']/1.2
    #     y_position_1 = data_map['DY1']/1.2

    #     x_position_2 = data_map['DX2']/1.2
    #     y_position_2 = data_map['DI2']/1.2

    #     # print(data_map)

    #     position_map['x_position_1'] = x_position_1
    #     position_map['y_position_1'] = y_position_1
    #     position_map['x_position_2'] = x_position_2
    #     position_map['y_position_2'] = y_position_2


    #     return position_map


    # this will take the formatted map into a string which will be printed to the text file 
    def format_map_to_string(self, data_map):
        # make into a collumn rather than  four lines 
        data_string = ""
        for key in data_map.keys():
            data_string += key + ": "+ str(data_map[key]) + '\n'
        return data_string 


    def produce_data(self, ser, running, file_name):
        # add options for much slower speed 
        sleep_time = 1//int(input ('Please enter: \n  1. 1 shot/second \n  2. 2 shots/second\n'))
        ser.close()
        
        f = open(file_name , "a" )  

        while running == True :

            f.flush()
            current_data = self.get_data(ser)
           
            data_map = decode_test.decode_byte(current_data)

            # f.write(str(list(data_map)))
            # print(current_data)

            f.write(self.format_map_to_string(data_map))
            f.write('\n\n')
            time.sleep(sleep_time)

        f.close()


    # this will start the live stream of data to a text file 
    # def start_stream(self, ser):
    
    #     # date/time stamp for each data remove underscores fix format add 0s 
    #     print ("starting live stream")
    #     self.make_file_title()    

    #     sample_rate = float(input("Please enter a number between 1-60 for sampling rate of data (1 sample/sec to 60 samples/second\n"))
       
    #     if(sample_rate in range(1,60)):
            
    #         sleep_time = (1000/sample_rate)*0.001
    #         with open(self.file_title, "w") as f:  
    #             f.write('this is a file to write too')
    #             # with condition:
    #             #     condition.notify()
    #             self.live_stream_status = True
    #             while self.live_stream_status == True:
    #                 test.produce_data(True, sleep_time)
    #                 # f.flush()
    #                 # # data = str(self.get_data(ser))+'\n'
    #                 # test.get_data()
    #                 # # f.write(data )
    #                 # # print(data)
    #                 # time.sleep(sleep_time)
            
    #     else:
    #         print("you have entered an invalid number")


    # stops the data live stream and closes the file writer 
    def end_stream(self, f):
        print("Ending the live stream\nThe data is in:", self.file_title )
        self.live_stream_status = False
        f.close()


# stream = live_stream()
# file_title = stream.make_file_title()
# ser = serial.Serial('/dev/cu.usbserial-D308C1SJ', bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout = 1, write_timeout=1, rtscts=False, dsrdtr=False, xonxoff= True,inter_byte_timeout = 1, exclusive= None)  # open serial port
# ser.baudrate = 115200
# ser.close()
# f = stream.make_file(stream.file_title)
# stream.produce_data(ser, True, stream.file_title)
# # current_data = stream.get_data(ser)
# # data_map = stream.decode_byte_data(current_data)
# # f.write(str(list(data_map)))
# # print(current_data)
