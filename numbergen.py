import hashlib
import time
import math
import statistics

#Define the starting object Hash
hashobj = hashlib.sha256('Hello World'.encode('utf-8'))



numberslist = []
start = time.time()
# Looperino starting here
for i in range(1000000):
    number = 0
    hashobj = hashlib.sha256(hashobj.hexdigest().encode('utf-8'))
    intversion = int(hashobj.hexdigest()[0:13], 16) # Javascript Original | parseInt(hash.slice(0,52/4),16);
    if (intversion % 101 == 0): # Check if Divisible by 101, if yes put out immediately 1 so users loose (1% house edge)
        number = 1.0
    else:
        b = 4503599627370496 # Javascript Original | Math.pow(2,52);
        #number = math.floor((100 * b - intversion) / (b - intversion)) / 100
        number = math.ceil((100 * b - intversion) / (b - intversion)) / 100 # not yet sure if this is truly the bug to be found.
    numberslist.append(number)
    #print(number) ### PLEASE PLEASE if doing bigger tests comment this out! 20x speed increase


end = time.time()

resultmean = statistics.mean(numberslist) 
resultharmonic_mean = statistics.harmonic_mean(numberslist)
resultmedian = statistics.median(numberslist)
resultmedian_low = statistics.median_low(numberslist)
resultmedian_high = statistics.median_high(numberslist)
resultmedian_grouped = statistics.median_grouped(numberslist)
resultmode = statistics.mode(numberslist)

resultpstdev = statistics.pstdev(numberslist)
resultpvariance = statistics.pvariance(numberslist)
resultstdev = statistics.stdev(numberslist)
resultvariance = statistics.variance(numberslist)



print("----------------------------------")
print("Time required: " + str(end - start))
print("Arithmetic mean (“average”) of data: " + str(resultmean))
print("Harmonic mean of data: " + str(resultharmonic_mean))
print("Median (middle value) of data: " + str(resultmedian))
print("Low median of data: " + str(resultmedian_low))
print("High median of data: " + str(resultmedian_high))
print("Median, or 50th percentile, of grouped data: " + str(resultmedian_grouped))
print("Mode (most common value) of discrete data: " + str(resultmode))

print("Population standard deviation of data: " + str(resultpstdev))
print("Population variance of data: " + str(resultpvariance))
print("Sample standard deviation of data: " + str(resultstdev))
print("Sample variance of data: " + str(resultvariance))

