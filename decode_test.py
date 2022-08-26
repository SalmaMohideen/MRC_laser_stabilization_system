# # # my_bytes = 'one é two'.encode('latin-1')
# # # print(my_bytes)
# # # my_str = my_bytes.decode('latin-1')

# # # print(my_str) 

# # import binascii
  
# # # Initializing a binary string
# # Text = b"GFG is a CS Portal"
  
# # # Calling the b2a_uu() function to
# # # Convert the binary string to ascii
# # Ascii = binascii.b2a_uu(Text)
  
# # # Getting the ASCII equivalent
# # print(Ascii)

from codecs import latin_1_decode
from struct import *
import struct
import math

# # \x00\x06
# def int_from_bytes(xbytes: bytes) -> int:
#     return int.from_bytes(xbytes, 'big')

# print('hi', int_from_bytes(stuf) )

# stuff = b'\x00;~~\x03\x90\x06\xfe\r2\xfa\xbe\x08i\t\xf3m\x15\xa0\x10\xd2\x12\xd5;\x00;'
# stuff = b'\x00;~~\x03\x92\x06\xff\r0\xfa\xb4\x08\x80\t\xe4n\x15\xa0\x10\xd2\x12\xd6;\x00;'


# format = 'h'
# stuff =  b'\x01;'
# # stuff = b'\x00;\x01\x00;'
# size = struct.calcsize(format)
# print(len(stuff))

# print(size)

# un_stuff = unpack(format,stuff)




# print (un_stuff)


# stuff_S1S = b'\x00;\x06\x06\x00\x06\x00\x06\x00*\x00\xb9\xfc\x87\x01\xaa\x9d\x9bmk;'




# format = 'xcBBhhHhhHhhc'

# print(un_stuff)


# print(len(un_stuff))

# size = struct.calcsize(format)
# print(size)

# size_stuff = len(stuff)
# print(size_stuff)


# stuff = b'\x00;\x06\x06\x00\x06\x00\x06\x00*\x00\xb9\xfc\x87\x01\xaa\x9d\x9bmk;'


# stuff = b'\x00;\x06\x06\x00\x06\x00\x06\x00*\x00\xb2\xfc\xbb\x01\xc5\x9b\x99jl;'

# stuff = b'\x00;\x00\x00\xf7\x01\xfbX\x0c\xd6\x03\xa5\x00\x00\x00\x88\x9a\x98oy;'

def decode_byte (stuff):
    format = 'hhhHhhHhhhc'
    beam_diameter_1 = float(1)
    beam_diameter_2 = float(1)

    x_position_1 = float(0)
    x_position_2 = float(0)

    y_position_1 = float(0)
    y_position_2 = float(0)


    data_map = {} 
    position_map = {}

    values_list = bytes_to_int(stuff)
    print (values_list)
    # packed  = pack(format, un_stuff[0], un_stuff[1],  un_stuff[2],  un_stuff[3], un_stuff[4],  un_stuff[5],  un_stuff[6],un_stuff[7],un_stuff[8], un_stuff[9], un_stuff[10])
    objects_order = ['DX1', 'DY1', 'DI1','DX2','DY2', 'DI2', 'RX1', 'RY1','RX2', 'RY2', ';']

    for i in range (len(values_list)-1):
        data_map[objects_order[i]] = (values_list[i]) 
        # print (objects_order[i] , ":  " , (un_stuff[i]))


    x_position_1 = data_map['DX1']/1.2
    y_position_1 = data_map['DY1']/1.2

    x_position_2 = data_map['DX2']/1.2
    y_position_2 = data_map['DI2']/1.2

    print(data_map)

    position_map['x_position_1'] = x_position_1
    position_map['y_position_1'] = y_position_1
    position_map['x_position_2'] = x_position_2
    position_map['y_position_2'] = y_position_2
    print (position_map)
    return position_map

def bytes_to_int(bytes):
    result = 0
    values_list = []
    for b in bytes:
       
        # values_list.append(b)

        result = result * 256 + int(b)
       

    # print(values_list)
    return result


stuff2 = b'\x00;\x00\x00\xf7\x03\xfbZ\x0c\xd8\x03\xa4\x00\x00\x00\x86\x99\x99my;'


stuff = b'\x00;\x00\x00\xf7\x01\xfbX\x0c\xd6\x03\xa5\x00\x00\x00\x88\x9a\x98oy;'


print(list(stuff))
stuff1 = b'\x00'

stuff2 = b';'
stuff3 = b'\x00'
stuff4 = b'\x00'

DX1 = b'\xf7'

other_stuff = b'\x01'

DY1 = b'\xfb'
theX = b'X'
print('yoyo', bytes_to_int(b'Z'))


other_stuff_1 = b'\x0c'
print(bytes_to_int(DY1))
print(bytes_to_int(other_stuff_1))

DI1 = b'\xd6\x03'
print(bytes_to_int(DI1))
DX2 = b'\xa5\x00'
print(bytes_to_int(DX2))
DY2 = b'\x00\x00'
print(bytes_to_int(DY2))
DI2 = b'\x88\x9a'
print(bytes_to_int(DI2))
RX1 = b'\x98oy'
print(bytes_to_int(RX1))

# stuff.encode('utf-8')
# print(bytes_to_int(stuff))
# print (bytes_to_int(DY1))
# decoded = list(stuff)
# print(decoded)
# print(bytes(decoded))

# decoded1 = list(stuffo)
# print(decoded1)
# print(bytes(decoded1))
# # print(stuff.decode('latin_1'))
# # decode_byte (stuff)


# def get_data():
#         ser = serial.Serial('/dev/cu.usbserial-D308C1SJ', bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout = 1, write_timeout=1, rtscts=False, dsrdtr=False, xonxoff= True,inter_byte_timeout = 1, exclusive= None)  # open serial port
#         ser.baudrate = 115200 
#         ser.write(bytes(('S1S;'.encode())))
#         reading_new = bytes(ser.read_until())
#         print(reading_new)


# def produce_data(running):
#     sleep_time = 1//int(input ('Please enter: \n  1. 1 shot/second \n  2. 2 shots/second'))
    
#     while running == True :
#         get_data()
#         time.sleep(sleep_time)




# print (int.from_bytes(stuff, "big"))


# for b in stuff: 
#     print (bytes(b))

# print(stuff[2:4])


# byte_string = str(stuff)

# byte_string = byte_string[7:len(byte_string)-2]
# print(byte_string)

# byte_string[2]

# print(stuff[4:6])



# stuff = b'\x00;\x00\x00\xf7\x01\xfbX\x0c\xd6\x03\xa5\x00\x00\x00\x88\x9a\x98oy;'

# stuff = b'\x00;\x06\x06\x00\x06\x00\x06\x00*\x00\xb9\xfc\x87\x01\xaa\x9d\x9bmk;'
# stuff = b'\x00;\x00\x00\x00\x06\x00\x06\x006\x00z\x00\x00\x00y\x98\x98ry;'

# stuff = b'\x00;\x06\x06\x00\x06\x00\x06\x00*\x00\xb2\xfc\xbb\x01\xc5\x9b\x99jl;'

# stuff = b'\x00;\x18\x18\xeck\xfa\xce\x01\xb2\x00A\x00\x00\x00y\x9a\x99qy;'
# print(decode_byte_to_ints(stuff)) 

# why is the last two bits not being able to be recognized 