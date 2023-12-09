import struct 
from enum import Enum

class OPCODE(Enum):
    mov = b'100010'

    
class WREG(Enum):
    al = b'0000'
    cl = b'0001'
    dl = b'0010'
    bl = b'0011'
    ah = b'0100'
    ch = b'0101'
    dh = b'0110'
    bh = b'0111'
    ax = b'1000'
    cx = b'1001'
    dx = b'1010'
    bx = b'1011'
    sp = b'1100'
    bp = b'1101'
    si = b'1110'
    di = b'1111'
    


with open('listing_0038_many_register_mov', 'rb') as f:
    s = bin(int(f.read().hex(), base=16))[2:]
    for line in [s[i:i+16] for i in range(0, len(s), 16)]:
        
        op_code = line[:6].encode()
        direction = line[6].encode()
        word1_byte0 = line[7].encode()
        mode = line[8:10].encode()
        reg1 = line[10:13].encode()
        reg2 = line[13:].encode()
        
        to_ = WREG(word1_byte0+reg2).name
        from_ = WREG(word1_byte0+reg1).name
        
        if direction == b'1':
            to_, from_ = from_, to_
        
        print(f'{OPCODE(op_code).name} {to_}, {from_}')
    