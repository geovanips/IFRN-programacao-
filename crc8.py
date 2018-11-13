def crc8(buff):
    crc = 0
    for b in buff:
        crc ^= b
        for i in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0x8C
            else:
                crc >>= 1
    return crc

buff = [0x12, 0xAB, 0x34]
crc = crc8(buff)
print(hex(crc))
