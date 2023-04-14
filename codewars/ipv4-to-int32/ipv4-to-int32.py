'''
Take the following IPv4 address: 128.32.10.1. This address has 4 octets where each octet is a single byte (or 8 bits).

    1st octet 128 has the binary representation: 10000000
    2nd octet 32 has the binary representation: 00100000
    3rd octet 10 has the binary representation: 00001010
    4th octet 1 has the binary representation: 00000001

So 128.32.10.1 == 10000000.00100000.00001010.00000001

Because the above IP address has 32 bits, we can represent it as the 32 bit number: 2149583361.

Write a function ip_to_int32(ip) ( JS: ipToInt32(ip) ) that takes an IPv4 address and returns a 32 bit number.

Example
    "128.32.10.1" => 2149583361
'''

def ip_to_int32(ip):
    splitter = ip.split('.')
    values = [int(splitter[0]) * (2 ** 24), int(splitter[1]) * (2 ** 16), int(splitter[2]) * (2 ** 8), int(splitter[3])]
    total = 0
    for val in values:
        total += val
    return total

def ip_to_int32(ip):
    splitter = ip.split('.')
    bitCount = 24
    total = 0
    for val in splitter:
        total += int(val) * (2 ** bitCount)
        bitCount -= 8
    return total