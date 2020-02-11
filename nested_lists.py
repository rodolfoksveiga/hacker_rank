def function(names, scores):
	index = scores.index(max(scores))
	scores.pop(index)
	names.pop(index)
	index = scores.index(max(scores))
	return(names[index])

if __name__ == '__main__':
	for _ in range(int(input())):
		names = []
		scores = []
		names = names.append(input())
		scores = scores.append(float(input()))
	print(function(name, score))
