#A stream of n data packets arrives at a server. This server can only process packets that 
# are exactly 2^n units long for some non-negative integer value of n (0<=n).All packets 
# are repackaged in order to the 1 largest possible value of 2^n units. The remaining portion 
# of the packet is added to the next arriving packet before it is repackaged. Find the size 
# of the largest repackaged packet in the given stream.


def repackagepackets(pck):
    std_pck=[int(2**x)for x in range(31)]
    rem=0
    max=0
    for i in pck:
        i=i+rem
        for j in range(31):
            if i<std_pck[j]:
                break
        rem=i-std_pck[j-1]
        if max<=std_pck[j-1]:
            max=std_pck[j-1]
    return max
pck=[]
for i in range(int(input())):
    pck.append(int(input()))

print(repackagepackets(pck))
        
            