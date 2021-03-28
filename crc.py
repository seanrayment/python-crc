from poly_gf2 import PolyGF2

class CRC:
    def __init__(self, poly):
        self.poly_gf2 = PolyGF2(poly)

    def checksum(self, msg):
        ascii_bytes = msg.encode('ascii')
        ascii_bits = [bin(b) for b in ascii_bytes]
        binary_string = ''.join(bit_str[2:] for bit_str in ascii_bits)
        msg_poly = PolyGF2(binary_string)
        msg_poly = msg_poly << (len(self.poly_gf2.polynomial) - 1)
        return msg_poly.remainder(self.poly_gf2).bitstring()

    def intact(self, msg, checksum):
        return self.checksum(msg) == checksum
