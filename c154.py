def f(data='190.168.0.96 190.168.0.96 45 04 05 dc b7 3a 40 00 2e 06 a6 df 36 f1 f0 fd c0 a8 00 67'):#test='t154.txt'):
    split = data.index(' ', data.rindex('.',0,32))
    header = data[split+1:split+int(data[split+2],16)*3*4]
    IPstring = data[:split]
    IPstring = IPstring.split()
    IPstring[0] = IPstring[0].split('.')
    IPstring[1] = IPstring[1].split('.')
    newIP = []
    for i in (0,1):
        for address in IPstring[i]:
            if int(address) < 16:
                newIP.append('0' + address)
            else:
                newIP.append(hex(int(address))[2:])
    newIP = ' '.join(newIP)
    s = (header[:30] + newIP).split()
    v = 0
    for i in range(0,len(s),2):
        v+=int(s[i] + s[i+1], 16)
    v = hex(v)
    v2 = int(v[3:],16) + int(v[2],16)
    compliment = int( (len(hex(v2))-2)*4 * '1', 2)
    newchecksum = hex(v2 ^ compliment)
    newchecksum = newchecksum[2:4] + ' ' + newchecksum[4:6] + ' '
    return header[0:30] + newchecksum + newIP
