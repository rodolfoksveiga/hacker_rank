def wrap(string, max_width):
	wrap_str = ''
	for i in range(0, len(string), max_width):
		wrap_str = '\n'.join([wrap_str, string[i: i + max_width]])
	wrap_str = wrap_str[1:]
	return(wrap_str)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
