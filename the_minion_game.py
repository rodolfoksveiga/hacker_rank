def minion_game(string):
	vowels = 'AEIOU'
	stuart = 0
	kevin = 0
	
	for c, v in enumerate(string):
		if v in vowels:
			kevin += len(string) - c
		else:
			stuart += len(string) - c
	
	if kevin > stuart:
		print('Kevin {}'.format(kevin))
	elif stuart > kevin:
		print('Stuart {}'.format(stuart))
	else:
		print('Draw')

if __name__ == '__main__':
