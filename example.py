from crc import CRC

msg = 'Hello, world!'
crc = CRC('1000000100001')
checksum = crc.checksum(msg)
print(checksum)
print(crc.intact('Hello, world!', checksum))
