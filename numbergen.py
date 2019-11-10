import hashlib
import hmac
import time
import math
import statistics
import binascii

#Define the starting object Hash
salt = binascii.hexlify(bytes('0000000000000000004d6ec16dafe9d8370958664c1dc422f452892264c59526', 'utf-8'))
seed = binascii.hexlify(bytes('a767b5b64dd68d677a7b21508ca835e1d15a92b2b953885c66aa28ffe34a14fd', 'utf-8'))
hashobj = hmac.new(salt, seed, hashlib.sha256)

numberslist = []
start = time.time()

# Looperino starting here
for i in range(1):
    number = 0
    intversion = int(hashobj.hexdigest()[0:int(52/4)], 16)             # parseInt(hash.slice(0,52/4),16);
    X = 99 / (1 - (intversion / (2 ** 52)))  # Math.pow(2,52);
    number = max(1, math.floor(X) / 100)
    numberslist.append(number)
    print(number) ### PLEASE PLEASE if doing bigger tests comment this out! 20x speed increase
    hashobj = hashlib.sha256(hashobj.hexdigest().encode('utf-8'))

end = time.time()

start2 = time.time()
resulthighest = max(numberslist)

resultmean = statistics.mean(numberslist) 
resultharmonic_mean = statistics.harmonic_mean(numberslist)
resultmedian = statistics.median(numberslist)
resultmedian_low = statistics.median_low(numberslist)
resultmedian_high = statistics.median_high(numberslist)
resultmedian_grouped = statistics.median_grouped(numberslist)
end2 = time.time()


print("----------------------------------")
print("Time required Bust numbers: " + str(end - start))
print("Time required for Statistics: " + str(end2 - start2))

print("Highest Number: " + str(resulthighest))

print("Arithmetic mean (“average”) of data: " + str(resultmean))
print("Harmonic mean of data: " + str(resultharmonic_mean))
print("Median (middle value) of data: " + str(resultmedian))
print("Low median of data: " + str(resultmedian_low))
print("High median of data: " + str(resultmedian_high))
print("Median, or 50th percentile, of grouped data: " + str(resultmedian_grouped))
