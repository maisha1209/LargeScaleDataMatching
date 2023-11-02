test = {'p1':{'x1':0.2, 'x3':0.6}, 'p2':{'x3':0.9}}

for key, value in test.items():
    print(key, len(value))
    scores = [score for paper, score in value.items()]
    average = sum(scores)/ len(scores)
    print(average)
    # for paper, score in value.items():
    #     print(key, paper, score)