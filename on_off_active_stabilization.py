
# function will sart active stabilization for the provided stage actuator
def start_active_stabilization(ser, stage_nums):

    # option one: have only active stabilization for only stage one 
    if stage_nums == '1':

        # turning on active stabilization stage one and processing feedback 
        print("turning on active stabilization stage one")
        ser.write(bytes(('SEA\x01;'.encode())))
        reading = bytes(ser.read_until())
        
        # turning off active stabilization for stage two and processing feedback 
        print("turning off active stabilization stage two")
        ser.write(bytes(('CEA\x02;'.encode())))
        reading = bytes(ser.read_until())


    # option two: have active stabilization for only stage two 
    elif stage_nums == '2':
    
        # turning on active stabilization stage two and processing feedback 
        print("turning on active stabilization stage two")
        ser.write(bytes(('SEA\x02;'.encode())))
        reading = bytes(ser.read_until())

        # turning on active stabilization stage one and processing feedback 
        print("turning off active stabilization stage one")
        ser.write(bytes(('CEA\x01;'.encode())))
        reading = bytes(ser.read_until())
       
    # option three: turning on active stabilzation for stages one and two   
    elif stage_nums == '3':
        
        # turning on active stabilization stage one and processing feedback 
        print("turning on active stabilization stages one and two")
        ser.write(bytes(('SEA\x01;'.encode())))
        reading = bytes(ser.read_until())

        # turning on active stabilization stage one and two and processing feedback 
        ser.write(bytes(('SEA\x02;'.encode())))
        reading = bytes(ser.read_until())
        
    # an invlaid number was entered 
    else:
        print("An invalid command was entered. Exiting the program.")
        quit()

# this function will turn off active stabilization for any/all actuator stages 
def stop_active_stabilization(ser, stage_nums):
    # option  1: turn off active stabilization for stage 1 only 
    if stage_nums == '1':

        # turning off active stabilization stage one and processing feedback 
        print("turning off active stabilization stage one")
        ser.write(bytes(('CEA\x01;'.encode())))
        reading = bytes(ser.read_until())


    # option 2: turn off active stabilization for stage two only 
    elif stage_nums == '2':
    

        # turning off active stabilization stage two and processing feedback 
        print("turning off active stabilization stage two")
        ser.write(bytes(('CEA\x02;'.encode())))
        reading = bytes(ser.read_until())
    
    # option 3: turn off active stabilization for stages one and two 
    elif stage_nums == '3':
        
        # turning off active stabilization stage one and processing feedback 
        print("turning off active stabilization stages one and two ")
        ser.write(bytes(('CEA\x01;'.encode())))
        reading = bytes(ser.read_until())

        # turning off active stabilization stage one and processing feedback 
        ser.write(bytes(('CEA\x02;'.encode())))
        reading = bytes(ser.read_until())

    # an invlaid number was entered    
    else:
        print("An invalid command was entered. Exiting the program.")
        quit()

