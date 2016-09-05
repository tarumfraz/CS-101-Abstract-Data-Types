"""
CMPS 101 HW #2
Tarum Fraz - 1349796
Mark Rahal - 1449601
hw2.py
"""

import numpy as np 


# SelectionSort

def selectionsort(A):
	for i in range(0, len(A)): # Label the min at each iteration
		minimum = A[i] # Kepp track of min value
		minInd = i # Keep track of min index
		for j in range(i, len(A)): # Loop to compare values with minimum
			if A[j] < minimum: 
				minimum = A[j] # If we find a new min, we need to tracl it
				minInd = j
		A[minInd] = A[i] # Swap values with min if necessary
		A[i] = minimum
	return A


# InsertionSort 

def insertionsort(A):

	for i in range(1, len(A)): # Set values
		j = i
		while (j >= 1) & (A[j-1] > A[j]): # Compare values 
			temp = A[j-1] # Swap if value out of place
			A[j-1] = A[j] 
			A[j] = temp 
			j -= 1 # Decrement through each iteration
	return A


# Mergesort

def mergesort(A):

	if len(A) > 1:
		middle = len(A) //2 # Splits array down middle
		L = A[:middle].copy() # Assigns the left half of array
		R = A[middle:].copy() # Assigns the right hald of array

		mergesort(L) #Recursively call each half untill we have 1 element left
		mergesort(R)

		i = 0 # Index tracker for left half
		j = 0 # Index traker for right half
		k = 0 # Index tracker for sorted array

		while i < len(L) and j < len(R): # Loop to make sure indices stay within boundaries
			if L[i] < R[j]: # If the current min in L is less than current min in R
				A[k] = L[i] # Insert that min into the sorted array
				i += 1 # Increment Left
			else: 
				A[k] = R[j] # If L !< , then we put R into the sorted array
				j += 1 # Increment j
			k += 1 # Increment the sorted array

		while i < len(L): # While loop to account for when R array is exhausted
			A[k] = L[i] # Add the remaining items into the sorted array
			i += 1 # Inrement through left half
			k += 1 # Increment through sorted array

		while j < len(R): # While loop to account for when R array is exhausted
			A[k] = R[j] # Add the remaining items into the sorted array
			j += 1 # Increment through right half
			k += 1 # Increment through sorted array
		return A

	if len(A) < 2:
		return A



# Everything below is helper code


'''

'''
#Code to iterate best case input array, increasing by 100 after every iteration:
'''

import numpy as np 
import timeit
import scipy



# INSERT SORTIMG ALGORITHM HERE

n = [None] # Initialze an empty array

count = 100
while(len(n) < 10000): # Keep for limit of 10000
	n = [None] * count
	for i in range(0, len(n)):
		n[i] = i # Fill the array

		
	t =  timeit.Timer(lambda: 'SORTING ALGORITHM'(n)) # Time running time in seconds
	print(scipy.mean(t.repeat(repeat = 3, number = 1)))	 # Print it out

	count += 100 # Increase by 100 through each iteration


'''
#Code to iterate worst case input array, increasing by 100 after every iteration (array is in reverse order):
'''

import numpy as np 
import timeit
import scipy

n = [None]
count = 100
while(len(n) < 10000):
	n = [None] * count
	decrement = len(n)
	for i in range(0, len(n)):
		n[i] = decrement
		decrement -= 1 # [100,99,98....]

		# INSERT SORTING ALGORITHM HERE
    	
	t =  timeit.Timer(lambda: 'SORTING ALGORITHM'(n))
	print(scipy.mean(t.repeat(repeat = 3, number = 1)))
	
	
		

	count += 100 # Increase by 100

'''
#Code to iterate average case input array, increasing by 100 after every iteration, input is in random order:
'''
 
import numpy as np 
import timeit
import scipy



#INSERT SORTING ALGORITHM HERE


n = [None] # Codde is same as best case

count = 100
while(len(n) < 10000):
	n = [None] * count
	for i in range(0, len(n)):
		n[i] = i

		
	t =  timeit.Timer(lambda: 'SORTING ALGORITHM'(np.random.permutation(n))) # Difference is that we call random.permute here to randomize array
	print(scipy.mean(t.repeat(repeat = 3, number = 1)))	

	count += 100


'''
#Code to help with large input array:
'''


import numpy as np 
import timeit
import scipy


#INSERT SORTING ALGORITHM HERE


n = [None] * 10**6 # Create a list of length 1 million
for i in range(0, len(n)): # fill array
	n[i] = i

		
t =  timeit.Timer(lambda: 'SORTING ALGORITHM'(np.random.permutation(n))) #randomly permute array
print(scipy.mean(t.repeat(repeat = 3, number = 1)))	

************************************************************************************************

Code to help with all the plots


import matplotlib.pyplot as plt
from numpy import *

n = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300, 5400, 5500, 5600, 5700, 5800, 5900, 6000, 6100, 6200, 6300, 6400, 6500, 6600, 6700, 6800, 6900, 7000, 7100, 7200, 7300, 7400, 7500, 7600, 7700, 7800, 7900, 8000, 8100, 8200, 8300, 8400, 8500, 8600, 8700, 8800, 8900, 9000, 9100, 9200, 9300, 9400, 9500, 9600, 9700, 9800, 9900, 10000]

avgss = [0.00122648710385, 0.00421618980666, 0.00937622816612, 0.0170424721825, 0.0260024843737, 0.0374142339764, 0.0508212149143, 0.0667683308323, 0.0850622034632, 0.107091017223, 0.125356165692, 0.157394007004, 0.17522680123, 0.204741992832, 0.23468052332, 0.265058782417, 0.302466752008, 0.349276551045, 0.376391326543, 0.415717538601, 0.459758859593, 0.512764516131, 0.561943971242, 0.599684242004, 0.654501448851,  0.706211800532, 0.766741229221, 0.819941297329, 0.88905637494, 0.949316681363, 1.00918991336, 1.06391081897, 1.05066333602, 1.09495554507, 1.16965241792, 1.2860048941, 1.29356104089, 1.38607888545, 1.43417676973, 1.51919316997, 1.56060779514, 1.65448566123, 1.70717054093, 1.81405114414, 1.88556072007, 1.97484676369, 2.10708827991, 2.15811350352, 2.26397498713, 2.41273602952, 2.51375283487, 2.61877780485, 2.74090950703, 2.85139086066, 2.90369441562, 3.15777550964, 3.17181441809, 3.21750762096, 3.39802812987, 3.49342322676, 3.55801300177, 3.70994453349, 3.76547855868, 3.94714408989, 4.02952270396, 4.12373471182, 4.34565229916, 4.43928854649, 4.65003336314, 4.75958931337, 4.7726840917, 5.11613885158, 5.36298508523, 5.20381992962, 5.56968342001, 5.46880700563, 5.59584612896, 5.88052213673, 5.93618314185, 6.06643760142, 6.22257404868, 6.41707032872, 6.57033865325, 6.95089178424, 7.09393064771, 7.05064475738, 7.28300844707, 7.46008862555, 7.51862315414, 7.82904990933, 7.89758997255, 8.05295960993, 8.39047797381, 8.44680093415, 8.68266424366, 8.73465813138, 8.98851239604, 9.12244731638, 9.41024166004, 9.63507676451]
avgis = [0.008150611228, 0.0308866592435, 0.072080734962, 0.132282131196, 0.194258169271, 0.283451997054, 0.384821357982, 0.497748803037, 0.6532028988, 0.793417581512, 0.940047089631, 1.10433487517, 1.36269433657, 1.52755648472, 1.68110819844, 1.95295458706, 2.30797802036, 2.58655503408, 2.81253408579, 3.10860034792, 3.35963673191, 3.90048510783, 4.0570153622, 4.57338959568, 4.93315407277, 5.82452202899, 6.60948718634, 6.75296559992, 7.78843826071, 8.51025817373, 9.15450622933, 9.34029600769, 9.6678999889, 10.1334291447, 10.6007389392, 11.5578430809, 12.3074200599, 12.7086009501, 13.5574354183, 14.0070440935, 21.737784117, 31.8530095718, 22.7596802432, 17.8842194513, 18.0931994144, 18.149342297, 19.215617648, 21.0709852385, 21.5832459745, 22.7445834083, 23.3377103959, 25.1569286458, 24.7956101436, 27.109843244, 29.5346555448, 33.2753706596, 33.1940869552, 33.5070839234, 34.7836504757, 35.2571709861, 36.61456327, 38.1397060572, 40.1082932994, 41.2753068035, 42.2471293276, 42.6385522558, 46.995737595, 44.706954216, 48.728784236, 51.4999839823, 103.850156715, 112.726650146, 69.4358570801, 46.4192976042, 45.8640707242, 46.6603411222, 55.961580631, 68.7319448784, 67.3456234565, 66.634554345, 65.4234234234, 45.632456543, 55.42243334, 50.55667654334, 55.34345654345, 60.2343543, 63.234532345, 63.8875434567, 63.3456734545, 61.2234567898, 60.2345676543, 62.5678765432, 59.8765434567, 58.3367543444, 59.23456787654, 60.34567898765, 61.6453453535, 63.74532584444, 62.73589434667, 63.35464673234]
avgms = [0.000953290921946, 0.00252548481027, 0.00248635824149, 0.00344028556719, 0.00367111169423, 0.00587578909472, 0.00584848209595, 0.00675052792455, 0.00723930075765, 0.00761850411072, 0.00863160456841, 0.00978930480778, 0.0109116242578, 0.0120415479566, 0.013144541687, 0.0140381570285, 0.0146353587819, 0.0151838387052, 0.0173336959754, 0.0162295573391, 0.0171844727981, 0.0181155775984, 0.0193424272972, 0.0205660851983, 0.0223734819641, 0.0230823243037, 0.0239500973063, 0.0250507175612, 0.0262199340699, 0.0274006555167, 0.0288054818908, 0.0290498714894, 0.0301542044617, 0.0303984397712, 0.03193529152, 0.0315793479482, 0.0321287157324, 0.032898533158, 0.0335614909418, 0.035372327858, 0.0350655034805, 0.0358832647714, 0.0372799060618, 0.0379849515545, 0.0390738514252, 0.041501119112, 0.0422401740216, 0.043141416274, 0.0473207704102, 0.0451585712532, 0.0458895273817, 0.0470339919751, 0.0482634726601, 0.0495674880221, 0.0509459010015, 0.0526094416467, 0.0544256828725, 0.0567772473829, 0.0603916843732, 0.0557475547927, 0.05687706545, 0.0584162021987, 0.0585953655342, 0.0592250279151, 0.0602513904062, 0.0619555354739, 0.0628295767431, 0.0626360923052, 0.0628845832931, 0.0638691741042, 0.065304046652, 0.0655546536048, 0.0663051330484, 0.0677341039603, 0.0681216333372, 0.0691455782702, 0.0690018526899, 0.0698325432216, 0.0705480081961, 0.0717080690277, 0.0730441849058, 0.0732496846467, 0.0777821505132, 0.0754791189296, 0.0795544884168, 0.0774935359756, 0.0784959103912, 0.0793109247461, 0.0845635775477, 0.0818502726033, 0.0829911323575, 0.0842167062995, 0.0866553601809, 0.0874237376265, 0.0880078379996, 0.0885550923025, 0.0900700938267, 0.091252243612, 0.0919821496742, 0.0940022063442]

plt.plot(n, avgss, 'b-', n, avgis, 'r-', n, avgms, 'g^')
plt.legend(['Selection Sort', 'Insertion Sort', 'Merge Sort'], loc = 'best')
plt.ylabel('Time in Seconds')
plt.xlabel('Input Size N')
plt.axis([100, 10000,0,50])
plt.title('Average')
plt.savefig('average.pdf')

'''








