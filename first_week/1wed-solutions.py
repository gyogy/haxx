def gas_stations(distance, tank_size, stations):
	list_o_stations = []
	progress = 0

	while tank_size + progress < distance:

		for i in range(len(stations)):

			if tank_size + progress < stations[i]:
				list_o_stations.append(stations[i-1])
				progress = stations[i-1]

		if tank_size + progress < distance:
			list_o_stations.append(stations[-1])
			progress = stations[-1]

	print(list_o_stations)

# gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350])

def is_number_balanced(number):
    
    result = False

    if number <10:
    	result = True

    whole_string = str(number)
    x = len(whole_string)//2
    
    if len(whole_string) % 2 > 0:
    	left_part = whole_string[:x]
    	rite_part = whole_string[x+1:]
    else:
    	left_part = whole_string[:x]
    	rite_part = whole_string[x:]

    left_sum = sum(int(i) for i in left_part)
    rite_sum = sum(int(i) for i in rite_part)

    if left_sum == rite_sum:
    	result = True

    print(result)

# is_number_balanced(1238033)

def increasing_or_decreasing(seq):

	if all(x<y for x, y in zip(seq, seq[1:])):
		print("Up!")

	elif all(x>y for x, y in zip(seq, seq[1:])):
		print("Down!")

	else:
		print(False)

# increasing_or_decreasing([9,8,7,6])

def get_largest_palindrome(n):

	while n > 0:
		if str(n-1) == str(n-1)[::-1]:
			print(n-1)
			break
		else:
			n -= 1

# get_largest_palindrome(754649)

def sum_of_numbers(input_string):
	temp_holder = []
	box = []

	for i in range(len(input_string)):

		if input_string[i].isnumeric(): 
			temp_holder.append(input_string[i])

		elif temp_holder != []:
			box.append(int(''.join(temp_holder)))
			temp_holder = []

	if temp_holder != []:
		box.append(int(''.join(temp_holder)))

	print(sum(box))

# sum_of_numbers("1abc33xyz22")

def birthday_ranges(birthdays, ranges):

	bd_boys_and_girls = []
	cnt = 0

	for window in ranges:

		for i in birthdays:

			if i in range(window[0], window[1]+1):
				cnt += 1

		bd_boys_and_girls.append(cnt)
		cnt = 0

	print(bd_boys_and_girls)

# birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)])

def group(n):

	holder = ""
	res = []

	for i in range(len(n)):
		
		if i == 0:
			holder += str(n[i])

		elif n[i] == n[i-1]:
			holder += str(n[i])

		else:
			res.append(holder)
			holder = ""
			holder += str(n[i])

	res.append(holder)

	return res

# group([2, -1, 2, 2, -1, 2, 2, 2])

def normalize_group(raw):

	seq = []
	
	for i in raw:
		if i[0] == '7' or i[0] == '9':
			if len(i)%4 == 0:
				seq.append(int(i[:4]))
			else:
				seq.append(int(i[:len(i)%4]))

		else:
			if len(i)%3 == 0:
				seq.append(int(i[:3]))
			else:
				seq.append(int(i[:len(i)%3]))

	return seq

def numbers_to_message(pressed_sequence):

	caps = False

	small_letters = " abcdefghijklmnopqrstuvwxyz"
	capital_letters = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	numbers = [0,2,22,222,3,33,333,4,44,444,5,55,555,
	6,66,666,7,77,777,7777,8,88,888,9,99,999,9999]


	lower_case = {k: v for (k, v) in zip(numbers, small_letters)}
	lower_case[-1] = ""

	upper_case = {k: v for (k, v) in zip(numbers, capital_letters)}
	upper_case[-1] = ""

	msg = normalize_group(group(pressed_sequence))
	
	for i in msg:

		if i == 1:
			caps = True

		elif caps:
			print(upper_case[i], end="")
			caps = False
		else:
			print(lower_case[i], end="")

	print()

# numbers_to_message([1,4,4,4,8,8,8,6,6,6,0,3,3,0,1,7,7,7,7,7,2,6,6,3,2])

def message_to_numbers(message):

	neg = False

	small_letters = " abcdefghijklmnopqrstuvwxyz"
	capital_letters = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	numbers = ["0","2","22","222","3","33","333","4","44","444","5","55","555",
	"6","66","666","7","77","777","7777","8","88","888","9","99","999","9999"]

	lower_case = {k: v for (k, v) in zip(small_letters, numbers)}
	upper_case = {k: v for (k, v) in zip(capital_letters, numbers)}

	lst = []
	control = []
	nums = []

	for i in message:
		if i.isupper():
			lst.append("1")
			lst.append(upper_case[i])
		else:
			lst.append(lower_case[i])

	for i in range(1, len(lst)):
		if lst[i][0] == lst[i-1][0]:
			control.append(i)

	for i in range(len(control)):
		lst.insert(control[i]+i,"-1")
			
	for i in ''.join(lst):
		if i == "-":
			neg = True
		elif neg:
			nums.append(-int(i))
			neg = False
		else:
			nums.append(int(i))

	print(nums)

message_to_numbers("aabbcc")