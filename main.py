# this main file will call other classes and manage communication with the controller
from ast import arg
from multiprocessing.synchronize import Condition
from tkinter import EXCEPTION
from serial_setup import serial_operations
import on_off_active_stabilization
from live_stream import live_stream
import threading
from threading import Condition
import test 
import time 
import serial

# default port address will automatically be connected to at the start of the program 
# user can change the default port adress by entering one and connecting to a different port 
DEFUALT_PORT_ADDRESS = '/dev/cu.usbserial-D308C1SJ'

def get_data():
        ser = serial.Serial('/dev/cu.usbserial-D308C1SJ', bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout = 1, write_timeout=1, rtscts=False, dsrdtr=False, xonxoff= True,inter_byte_timeout = 1, exclusive= None)  # open serial port
        ser.baudrate = 115200 
        ser.write(bytes(('S1S;'.encode())))
        reading_new = bytes(ser.read_until())
        print(reading_new)


def produce_data(running):
    sleep_time = 1//int(input ('Please enter: \n  1. 1 shot/second \n  2. 2 shots/second'))
    
    while running == True :
        get_data()
        time.sleep(sleep_time)


def main():
    
    # uses default port adress to connect to the controller and opens communication
    try: 
        my_serial = serial_operations('', False, False)
        my_serial.name = DEFUALT_PORT_ADDRESS
        my_serial.transmission_status = True 
        my_serial.receiving_status = True 
        ser = my_serial.open_port()

    except serial.SerialException as e: 
        # if the default device can't be found, then an error will be printed 
        print('The device could not be connected using the default address.\nPlease enter 1 to connect to the controller.\nThen store this address as the DEFUALT_PORT_ADDRESS variable in line 15 of main.py file. ')

    menu_options_message = "Please enter a command:\n (1) setup a new controlller connection\n (2) turn on active stabilization\n (3) turn off active stabilization\n (4) set up a data live stream\n (5) end the live stream\n (6) set and hold a position\n (7) re-set the set and hold postion\n (8) open the troubleshooting menu\n (9) exit the program\n"
    menu_input = input(menu_options_message).strip()
    
    while menu_input == '1'or '2' or '3' or '4' or '5' or '6' or '7'or '8' or '9':

        # helps the user find a different port adress, connect to the controller, and verify that connection is working
        if menu_input == '1':  
            try:
                my_serial = serial_operations('', False, False)
                ser =  my_serial.setup_controller(my_serial)
                
                
                if my_serial.receiving_status  == False or my_serial.transmission_status  == False :
                    print('Controller had issues recieving/transmitting commands please turn on and connect the controller to the computer and turn on the laser beam\n')
                    quit()
                else:
                    print('Device has been setup properly and is ready to use')
                    
            except serial.SerialException as e: 
                if e.errno == 2:
                    print("The port could not be connected to becuase adress you entered is incorrect or not found.")
            
        
        elif menu_input == '2' or '3' or '4' or '5' or '6' or '7':
            try:   
                # allows the user to turn on active stablization 
                if menu_input == '2': 
                    stage_number = input ('Please enter:\n (1)Turn on only stage one\n (2)Turn on only stage two\n (3)Turn on stage one and two\n')
                    on_off_active_stabilization.start_active_stabilization(ser , stage_number.strip())
                
                # allows the user to turn off active stablization
                elif menu_input == '3': 
                    stage_number = input ('Please enter:\n (1)Turn off only stage one\n (2)Turn off only stage two\n (3)Turn off stage one and two\n ')
                    on_off_active_stabilization.stop_active_stabilization(ser , stage_number.strip())

                # allows the user to turn on the data live stream 
                elif menu_input == '4':
                    # live_stream = test()
                    ser.close()
                    live_stream.start_stream(ser, True)
                    
                # allows the user to turn off a data live stream
                elif menu_input == '5':
                    ser.close()

                # allows the user to create a set and hold position
                elif menu_input == '6':
                    # turns off active stabilization for both systems
                    print('Active stabilization must be off in order to set and hold. Turning off both active stabilization for both stages...')
                    ser.write(bytes(('CEA\x01;'.encode())))
                    reading = bytes(ser.read_until())
                    ser.write(bytes(('CEA\x02;'.encode())))
                    reading = bytes(ser.read_until())

                    # option to set and hold the position on detector 1 
                    print('Would you like to set and hold the current position to be the target position for the closed loop stabilization for STAGE 1')
                    if input("Enter:\n 1. Yes\n2. No") == '1':
                        ser.write(bytes(('SSH\x01;'.encode())))
                        reading = bytes(ser.read_until())

                    # option to set and hold the position on detector 2
                    print('Would you like to set and hold the current position to be the target position for the closed loop stabilization for STAGE 2')
                    if input("Enter:\n 1. Yes\n2. No") == '1':
                        ser.write(bytes(('SSH\x02;'.encode())))
                        reading = bytes(ser.read_until())

                    print ('Okay! The new postions have been stored as the target postions')
                    print('These target positions are stored in non-volatile memory and will be continued for stailization after the controller has been disconected and reconnected ')
                
                # allows the user to reset the stabilization target positions to be the detectors centers 
                elif menu_input == '7':
                    # first turns off active stabilizaition for both detectors 
                    print('Active stabilization must be off in order to set and hold. Turning off both active stabilization for both stages...\n')
                    ser.write(bytes(('CEA\x01;'.encode())))
                    reading = bytes(ser.read_until())
                    ser.write(bytes(('CEA\x02;'.encode())))
                    reading = bytes(ser.read_until())

                    print('Would you like to deactivate of STAGE 1. Reset target position to “0” on detector of STAGE 1.')
                    if input('Enter:\n1. Yes\n2. No\n').strip() == '1':
                        ser.write(bytes(('CSH\x01;'.encode())))
                        reading = bytes(ser.read_until())
                        print ('The target position on detector 1 has been reseg to “0,0”.')


                    print('Would you like to deactivate STAGE 2. Reset target position to “0” on detector of STAGE 2.')
                    if input('Enter:\n1. Yes\n2. No\n') == '1':
                        ser.write(bytes(('CSH\x02;'.encode())))
                        reading = bytes(ser.read_until())
                        print ('The target position on detector 1 has been reseg to “0,0”.')
            except serial.SerialException as e: 
                print('Serial device is not correctly connected, please enter 1 and properly set up the device')
            except  UnboundLocalError as error:
                print('Serial device is not correctly connected, please enter 1 and properly set up the device')

        #opens the file trouble_shooting.txt
        elif menu_input == '8':
            print('Opeining the trouble shooting file..')
        
        # otherwise the program is exited 
        else: 
            try:
                print('Program is exiting.')
                ser.close()
                quit() 
            except UnboundLocalError as error:
                print("You exited the program without connecting the controller first")
                quit() 

        menu_input = input(menu_options_message).strip()
    
    # once an invalid entry has been entered, while loop is exited and program quits
    else: 
        print('You have entered an invalid menu option ... program has exited.')
        ser.close()
        quit() 
    

    
if __name__ == "__main__":
    main()

