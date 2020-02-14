def function(names, scores):
    second_lowest = []
    for c, v in enumerate(scores):
        if v == sorted(set(scores))[1]:
            second_lowest.append(names[c])
    second_lowest = sorted(second_lowest)
    print('\n'.join(second_lowest))

if __name__ == '__main__':
    names = []
    scores = []
    for _ in range(int(input())):
        names.append(input())
        scores.append(float(input()))
    function(names, scores)



