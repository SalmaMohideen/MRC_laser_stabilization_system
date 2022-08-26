
def decode_byte_string (byte_val):
    # Declaring byte value
   

    # Converting to int
    int_val = int.from_bytes(byte_val, "big")

    # printing int equivalent
    # print(int_val)
    return str(int_val)




# for b in stuff: 
#     print (bytes(b))

# print(stuff[2:4])


# byte_string = str(stuff)

# byte_string = byte_string[7:len(byte_string)-2]
# print(byte_string)

# byte_string[2]

# print(stuff[4:6])

def decode_byte_to_ints(byte_string):
    return_value = ''
    
    if len(byte_string) == 21: 
        DX1 = byte_string[3:5]
        # print('DX1: ', DX1)
        # print ('DX1: ', decode_byte_string(DX1))

        return_value += 'DX1: '+ decode_byte_string(DX1) +'\n'
        # print('DX1: ', decode_byte_string(bytes(DX1, )))

        DY1 = byte_string[5:7]
        # print(DY1)
        # print('DY1: ', decode_byte_string(DY1))
        return_value += 'DY1: '+ decode_byte_string(DY1)+'\n'

        DI1 = byte_string[7:9]
        # print(DI1)
        # print('DI1: ',decode_byte_string(DI1))
        return_value += 'DI1: '+ decode_byte_string(DI1) + '\n'

        DX2 = byte_string[9:11]
        # print(DX2)
        # print('DX2: ',decode_byte_string(DX2))
        return_value += 'DX2: '+ decode_byte_string(DX2) + '\n'

        DY2 = byte_string[11:13]
        # print(DY2)
        # print('DY2: ', decode_byte_string(DY2))
        return_value += 'DY2: '+ decode_byte_string(DY2) + '\n'

        DI2 = byte_string[13:15]
        # print(DI2)
        # print('DI2: ',decode_byte_string(DI2))
        return_value += 'DI2: ' + decode_byte_string(DI2) + '\n'

        RX1 = byte_string[15:17]
        # print(RX1)
        # print('RX1:', decode_byte_string(RX1))
        return_value += 'RX1:'+ decode_byte_string(RX1) + '\n'

        RY1 = byte_string[17:18]
        # print(RY1)
        # print('RY1: ', decode_byte_string(RY1))
        return_value += 'RY1: '+ decode_byte_string(RY1) + '\n'

        RX2 = byte_string[18:19]
        # print(RX2)
        # print('RX2: ', decode_byte_string(RX2))
        return_value += 'RX2: '+ decode_byte_string(RX2) + '\n'

        RY2 = byte_string[19:20]
        # print(RY2)
        # print('RY2: ', decode_byte_string(RY2))
        return_value += 'RY2: ' + decode_byte_string(RY2) + '\n'
        
    else:
        return_value = 'The data shot was not the correct format'
        return_value += 'DX1: N\A'+'\n'+ 'DY1: N\A '+'\n'+'DI1: N\A'+'\n'+'DX2: N\A'+'\n'+'DY2: N\A' + '\n'+ 'DI2: N\A' +'\n'+'RX1: N\A'+'\n'+ 'RY1: N\A'+'\n'+  'RX2: N\A'+'\n'+ 'RY2: N\A' 
    return return_value

# stuff = b'\x00;\x00\x00\xf7\x01\xfbX\x0c\xd6\x03\xa5\x00\x00\x00\x88\x9a\x98oy;'

# stuff = b'\x00;\x06\x06\x00\x06\x00\x06\x00*\x00\xb9\xfc\x87\x01\xaa\x9d\x9bmk;'
# stuff = b'\x00;\x00\x00\x00\x06\x00\x06\x006\x00z\x00\x00\x00y\x98\x98ry;'

# stuff = b'\x00;\x06\x06\x00\x06\x00\x06\x00*\x00\xb2\xfc\xbb\x01\xc5\x9b\x99jl;'

# stuff = b'\x00;\x18\x18\xeck\xfa\xce\x01\xb2\x00A\x00\x00\x00y\x9a\x99qy;'
# print(decode_byte_to_ints(stuff)) 

# why is the last two bits not being able to be recognized 