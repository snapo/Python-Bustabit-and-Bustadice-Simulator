import hashlib
import hmac
import time
import math
import binascii
import statistics
#Define the starting object Hash
salt = '0000000000000000004d6ec16dafe9d8370958664c1dc422f452892264c59526'.encode()
seed = "94809b699a42899197d863be47fe12fe15ae06bd481821c74b060868a7812260"
hashobj = hmac.new(salt, binascii.unhexlify(seed), hashlib.sha256)

numberslist = []
start = time.time()

# Looperino starting here
for i in range(10000000):
    number = 0
    intversion = int(hashobj.hexdigest()[0:int(52/4)], 16)             # parseInt(hash.slice(0,52/4),16);
    X = 99 / (1 - (intversion / (2 ** 52)))  # Math.pow(2,52);
    number = max(1, math.floor(X) / 100)
    numberslist.append(number)
    #print(number) ### PLEASE PLEASE if doing bigger tests comment this out! 20x speed increase
    seed = hashlib.sha256(seed.encode()).hexdigest()
    hashobj = hmac.new(salt, binascii.unhexlify(seed), hashlib.sha256)

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
