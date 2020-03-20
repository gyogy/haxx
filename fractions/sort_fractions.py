def denormalize_sorted_fractions(fractions, key):
	divisors = []
	result = []
	holder = []

	nominators = [fractions[i][0] for i in range(len(fractions))]
	denominators = [fractions[i][1] for i in range(len(fractions))]

	for i in key:
		divisor = 1
		
		for j in i:
			divisor = divisor * j
		
		divisors.append(divisor)

	for k in range(len(nominators)):

		holder.append(int(nominators[k]/divisors[k]))
		holder.append(int(denominators[k]/divisors[k]))
		result.append(tuple(holder))
		holder = []


	return result

def sort_norm_fractions(fractions, key):

	sorted_norm_fractions = []
	sorted_key = []
	normalized_nominators = [fractions[i][0] for i in range(len(fractions))]

	for i in sorted(normalized_nominators):

		for j in fractions:

			if j[0] == i:
				sorted_norm_fractions.append(j)
				sorted_key.append(key[fractions.index(j)])

	return sorted_norm_fractions, sorted_key

def normalize_fractions(noms, denoms, key):

	normalized_fractions = []
	holder = []

	for i in range(len(key)):

		for j in key[i]:

			noms[i] = noms[i] * j
			denoms[i] = denoms[i] * j

	for k in range(len(noms)):

		holder.append(noms[k])
		holder.append(denoms[k])
		normalized_fractions.append(tuple(holder))
		holder = []

	return normalized_fractions

def get_key(noms, denoms):
	
	key= []

	for i in range(len(noms)):
		key.append([])
		for j in range(len(denoms)):
			if i == j:
				pass
			else:
				key[i].append(denoms[j])

	return key

def sort_fractions(fractions, ascending=True):
	
	nominators = [fractions[i][0] for i in range(len(fractions))]
	denominators = [fractions[i][1] for i in range(len(fractions))]

	key = get_key(nominators, denominators)

	normalized_fractions = normalize_fractions(nominators, denominators, key)

	sorted_norm_fractions = sort_norm_fractions(normalized_fractions, key)[0]
	sorted_key = sort_norm_fractions(normalized_fractions, key)[1]

	sorted_original_fractions = denormalize_sorted_fractions(sorted_norm_fractions, sorted_key)

	if ascending:
		return sorted_original_fractions
	else:
		return sorted_original_fractions[::-1]

def main():
	print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)], False))

if __name__ == '__main__':
	main()