def r_anagrams(words):
	
	left_chars = [i for i in words.lower().split(" ")[0]]
	right_chars = [j for j in words.lower().split(" ")[1]]

	if len(left_chars) != len(right_chars):
		print('NOT ANAGRAMS')

	elif sorted(left_chars) != sorted(right_chars):
		print('NOT ANAGRAMS')

	else:
		print('ANAGRAMS')		
	
#r_anagrams("sIlEnT LiStEn")

def is_credit_card_valid(number):

	ints_in_even_positions = [int(i) for i in str(number)[::2]]
	ints_in_oddd_positions = [2 * int(j) for j in str(number)[1::2]] 
	
	sum_oddd_p = sum(int(i)for i in str(ints_in_oddd_positions)[1:-1].replace(', ', ''))
	sum_even_p = sum(ints_in_even_positions)

	if (sum_oddd_p + sum_even_p) % 10 == 0:
		print(True)
	else:
		print(False)

#is_credit_card_valid(79927398715)

def primes_in_n(n):
	
	lst = []
	
	for val in range(2, n + 1):

	       for i in range(2, val): 
	           if (val % i) == 0: 
	               break
	       else: 
	           lst.append(val)
	
	return(lst)

def goldbach(n):
	
	primes = primes_in_n(n)
	used_primes = []
	result = []
	
	for i in primes:

		for j in primes:

			if i + j == n and not j in used_primes:
				used_primes.append(i)
				result.append((i, j))

	print(result)

#goldbach(100)

def matrix_bombing_plan(m):
	
	mx_dictionary = {}
	neighbours = {}
	initial_sum = 0
	
	# filling the starting vars with values
	for y in range(len(m)):

		for x in range(len(m[y])):

				mx_dictionary[(x, y)] = m[y][x]
				neighbours[(x, y)] = []
				initial_sum += m[y][x]

	# neighbour values = list of original value - bombing value)
	for key in mx_dictionary:

		for x in range(key[0]-1,key[0]+2):
				
				for y in range(key[1]-1,key[1]+2):

					if x != key[0] or y!= key[1]:
						
						try:
							if mx_dictionary[(x,y)] < mx_dictionary[key]:
								neighbours[key].append(mx_dictionary[(x,y)])
							else:
								neighbours[key].append(mx_dictionary[key])
						except:
							pass

	# returning desired output
	for key in mx_dictionary:
		print(key, ":", initial_sum - sum(neighbours[key]))

# matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]])