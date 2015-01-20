'''ENDIANNESS

Write a program which prints the endianness of the system.

INPUT SAMPLE:
There is no input for this program.

OUTPUT SAMPLE:
Print to stdout the endianness, wheather it is LittleEndian or BigEndian.
For example:

BigEndian
'''
import sys
if sys.byteorder == 'little':
    print("LittleEndian")
else:
    print("BigEndian")
