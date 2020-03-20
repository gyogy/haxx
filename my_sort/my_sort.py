def dict_sorter(iterable, key, ascending=True):
	
	list_o_keys = []
	sorted_dict = []

	for i in iterable:
		list_o_keys.append(i[key])

	for j in list_sorter(list_o_keys):

		for k in iterable:

			if k[key] == j:
				sorted_dict.append(k)

	if ascending:
		return sorted_dict
	else:
		return sorted_dict[::-1]

def tuple_sorter(iterable, ascending=True):
	
	tuple_as_list = list(iterable)

	result = list_sorter(tuple_as_list)

	if ascending:
		return tuple(result)
	else:
		return tuple(result[::-1])

def list_sorter(iterable, ascending=True):
	
	sorted_list = []
	
	while len(iterable) > 0:
		sorted_list.append(iterable.pop(iterable.index(min(iterable))))

	if ascending:
		return sorted_list
	else:
		return sorted_list[::-1]
	

def my_sort(iterable=None, ascending=True, key=''):
	
	if str(type(iterable)) == "<class 'str'>" or str(type(iterable)) == "<class 'int'>":
		raise ValueError('Please enter an iterable type.')

	elif str(type(iterable)) == "<class 'list'>":
		
		if str(type(iterable[0])) == "<class 'int'>":
			list_sorter()

		elif str(type(iterable[0])) == "<class 'dict'>":
			dict_sorter()

	elif str(type(iterable)) == "<class 'tuple'>":
		tuple_sorter()

def main():
	pass

if __name__ == '__main__':
	main()