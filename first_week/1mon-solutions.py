def sum_of_digits(n):
	s = str(n)
	r = 0

	for i in s:
		if i == "-":
			continue
		else:
			r += int(i)
	print(r)

# sum_of_digits(888)

def sum_of_digits2(n):
	print([sum(int(i) for i in str(n))])

# sum_of_digits2(123456789)

def to_digits(n):
	s = str(n)
	l = []

	for i in s:
		l.append(int(i))
	print(l)

# to_digits(97854)

def to_digits2(n):
	print([int(i) for i in str(n)])

# to_digits2(123)

def to_number(*args):
	s = ''.join(map(str, args))
	print(s)

# to_number(21,3,16)

def to_number2(digits):
	s = int(''.join([str(i) for i in digits]))
	print(s)

# to_number2([20,3,4])

def fact_digits(n):
	ft = 1
	r = 0
	s = str(n)
	l = []

	for i in s:
		l.append(int(i))

	for j in l:
		for k in range(1, j+1):
			ft = ft * k
		r += ft
		ft = 1
	print(r)

# fact_digits(333)

def palindrome(obj):
	s = str(obj)
	l = len(s)
	z = s[l::-1]
	is_palindrome = True

	for i in range(0,l):
		if not s[i] == z[i]:
			is_palindrome = False

	print(is_palindrome)

# palindrome('abcba')

def count_vowels(str):
	vowels = ("a","e","o","u","i","y","A","E","O","U","I","Y")
	vcnt = 0

	for i in str:
		if i in vowels:
			vcnt += 1

	print(vcnt)

# count_vowels("A nice day to code!")

def count_consonants(str):
	vowels = ("a","e","o","u","i","y","A","E","O","U","I","Y")
	ccnt = 0

	for i in str:
		if not i in vowels and i.isalpha():
			ccnt += 1

	print(ccnt)

# c_con("Github")

def char_histogram(string):
    gram = {}

    for i in string:
    	gram[i] = string.count(i)

    print(gram)


# char_histogram("AAAAaaa!!!")


m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def sum_matrix(m):
	s = 0

	for i in m:
		for j in i:
			s += j

	print(s)

# sum_matrix(m)

def sum_matrix2(m):
	print([sum(j for i in m for j in i)])
	
# sum_matrix2(m)

def nan_expand(times):
	if times > 0:
		print("Not a " * times + "Nan")
	else:
		print("\"\"")

# nan_expand(0)

def group(n):
	res = []
	group_index = 0

	for i in range(len(n)):

		if i == 0:
			res.append([])
			res[group_index].append(n[i])
		
		elif i > 0 and n[i] == n[i-1]:
			res[group_index].append(n[i])

		else:
			group_index +=1
			res.append([])
			res[group_index].append(n[i])

	return res

# group([1, 1, 1, 2, 3, 1, 1])

def max_consecutive(items):

	cnt = 0
	max_cnt = 0

	for i in group(items):
		cnt = len(i)
		if cnt > max_cnt:
			max_cnt = cnt

	print(max_cnt)

# max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5])

def prime_factorization(n):

	divisor = 2
	primes = []
	tupled_primes = []

	while n > 1:
		if n % divisor == 0:
			primes.append(divisor)
			n = n / divisor
			divisor = 2
		else:
			divisor += 1

	x = group(primes)

	for i in range(len(x)):
		prime_and_power = x[i][0], x[i].count(x[i][0])
		tupled_primes.append(tuple(prime_and_power))
	
	print(tupled_primes)


prime_factorization(6532)