def wrap(string, max_width):
	for i in range(0, len(string), max_width):
		wrap_str = '\n'.join(string[i: i + max_width])
	return (wrap_str)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
