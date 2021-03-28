from crc import CRC

msg = 'Hello, world!'
crc = CRC('10011')
checksum = crc.checksum(msg)
print(checksum)
print(crc.intact('Hello, world!', checksum))
