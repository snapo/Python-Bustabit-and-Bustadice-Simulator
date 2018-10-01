import hashlib
import time
import math

#Define the starting object Hash
hashobj = hashlib.sha256('Hello World'.encode('utf-8'))




start = time.time()
# Looperino starting here
for i in range(1000000):
    hashobj = hashlib.sha256(hashobj.hexdigest().encode('utf-8'))
    intversion = int(hashobj.hexdigest()[0:13], 16) # Javascript Original | parseInt(hash.slice(0,52/4),16);
    # Check if Divisible by 101, if yes put out immediately 1 so users loose (1% house edge)
    if (intversion % 101 == 0):
        number = 1.00
    else:
        b = 4503599627370496 # Javascript Original | Math.pow(2,52);
        number = math.floor((100 * b - intversion) / (b - intversion)) / 100
    #print(number) ### PLEASE PLEASE if doing bigger tests comment this out! 20x speed increase







end = time.time()
print("Time required: " + str(end - start))

 
