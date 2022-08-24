# this file takes you through setting up and connecting MRC controller to the computer 
# then some tests will be run to ensure that receiving and transmitting work correctly 
import serial 
import serial.tools.list_ports
import time

class serial_operations:
  def __init__(self, name, transmission_status, receiving_status):
    self.name = name
    self.transmission_status = transmission_status 
    self.receiving_status =receiving_status
    
  # takes the user through the process of finding and setting the correct serial port adress for the controller 
  def setting_port_address(self):

    print('Hello, welcome to the serial setup\n')
    print('First we will set up the port adress which will be referred to throughout the program \n')
    
    # if user enters anything other than one the program is exited 
    if input('Please type the number (1) to continue and (2) to cancel \n')  != '1':
      print('exiting...')
      quit()


    print('We will be printing all detected serial port information\n')
    print('The MRC controller should have the following properites\n port_address:FT230X Basic UART [USB VID:PID=0403:6015 SER=D308C1SJ LOCATION=1-1.3] \n')
    print('The following is a list of all of your computers recognized ports, and the attributes of those serial devices:\n\n')
   
    # produces a list all the serial ports that are connected to the computer 
    all_ports = serial.tools.list_ports.comports()

    # prints out the list of all the serial devices which are connected to your computer and some of there properties 
    for port, desc, hwid in sorted(all_ports):
      print('{}: {} [{}]'.format(port, desc, hwid))
      print()

    # asks the user to input the name of serial port so it can be stored and referenced throughout the program 
    self.name = input('Please copy and paster the serial port adress (info before the colon) below\n').strip()
      

  #  function that opens the port with the proper settings  
  def open_port(self):
    # open serial port and sets the correct settings 
    try: 
      ser = serial.Serial(self.name, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout = 1, write_timeout=1, rtscts=False, dsrdtr=False, xonxoff= True,inter_byte_timeout = 1, exclusive= None)  
      ser.baudrate = 115200 
      return ser 
      
    except serial.SerialException as e: 
      print('Serial device cannot be connected to please check the address entered and enter 1 to restart the setup process')
    

  # function that checks command transmisson functionality by swithcin on and off active stabilization for both stages 
  def set_receiving_transmission_status(self, ser):
    stage_one_activated = False 
    stage_two_activated = False 

    try:
      # turning on active stabilization stage one and processing feedback 
      print('Turning on Active Stabilization stage one')
      ser.write(bytes(('SEA\x01;'.encode())))
      reading = bytes(ser.read_until())
      print(reading)

      # checks for feedback error from turning on stage one
      if reading.strip() !=  b'\x00;':
        print('Controller could not recieve command for active stabilization of stage 1\n')
      
      else:
        stage_one_activated = True
      time.sleep(1)


      # turning on active stabilization stage two and processing feedback 
      print('turning on active stabilization stage two')
      ser.write(bytes(('SEA\x02;'.encode())))
      reading = bytes(ser.read_until())
      print(reading)
      if reading.strip() !=  b'\x00;':
        print('Controller could not recieve command for active stabilization of stage 2\n')
      else:
        stage_two_activated = True 
      

      time.sleep(1)


      # turning off active stabilization stage one and processing feedback 
      print('turning off active stabilization stage one')
      ser.write(bytes(('CEA\x01;'.encode())))
      reading = bytes(ser.read_until())

      time.sleep(1)

      
      # turning off active stabilization stage two and processing feedback 
      print('turning off active stabilization stage two')
      ser.write(bytes(('CEA\x02;'.encode())))
      reading = bytes(ser.read_until())

    except serial.SerialException as e: 
      print('transmitting commands to the controller is not working, please ensure that the controller is plugged in, turned on, and there are high intensity beams on the detectors')
    
    # prompts the user to verify that the data was being received by the controller
    # if anything other than 1 is entered, the program is exited 
    if input('Enter (1) to verify that the sequence of steps worked, and (2) if it did not\n') != '1':
      print('please ensure that the controller is plugged in, turned on, and there are high intensity beams on the detectors')
      quit()

    
    # otherwise the field of transmission status is verified 
    elif stage_one_activated and stage_two_activated :
      self.receiving_status = True
      self.transmission_status = True

  # this function will 
  def setup_controller(self, my_serial):
    # my_serial = serial_operations('', False, False)
    my_serial.setting_port_address()
    ser = my_serial.open_port()

    print('We will now check that the controller can receive and transmit and receive data by turning on/off active stabilization for both stages')
    my_serial.set_receiving_transmission_status(ser)
    
    if my_serial.receiving_status == True and my_serial.transmission_status == True:
      print('The device seems to be receiving and transmitting information correctly!')
      print('The setup process for ',  my_serial.name, ' has been completed')
    
    return ser

      

