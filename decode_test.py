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
# # def int_from_bytes(xbytes: bytes) -> int:
# #     return int.from_bytes(xbytes, 'big')

# # print('hi', int_from_bytes(stuf) )

# # stuff = b'\x00;~~\x03\x90\x06\xfe\r2\xfa\xbe\x08i\t\xf3m\x15\xa0\x10\xd2\x12\xd5;\x00;'
# # stuff = b'\x00;~~\x03\x92\x06\xff\r0\xfa\xb4\x08\x80\t\xe4n\x15\xa0\x10\xd2\x12\xd6;\x00;'

#
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
        print(result )

    # print(values_list)
    return result


stuffo= b'\x00;\x18\x18\x00\x06\x00\x06\x00,\x00m\x00\x00\x00w\x99\x98ry;'

stuff = b'\x00;\x00\x00\xf7\x01\xfbX\x0c\xd6\x03\xa5\x00\x00\x00\x88\x9a\x98oy;'
stuff1 = b'\x00'
stuff2 = b';'
stuff3 = b'\x00'
stuff4 = b'\x00'
DX1 = b'\xf7\x01'
DY1 = b'\xfbX\x0c'
DI1 = b'\xd6\x03'
DX2 = b'\xa5\x00'
DY2 = b'\x00\x00'
DI2 = b'\x88\x9a'
RX1 = b'\x98oy'

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





