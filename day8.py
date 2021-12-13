from itertools import permutations

valid = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

fs = open('input.txt', 'r')
lines = list(map(lambda x: x.strip().split('|'), fs.readlines()))

alpha = list(permutations([chr(ord('a') + i) for i in range(7)]))
num = [0 for i in range(10)]
for i in range(len(lines)):
    train = lines[i][0].split()
    sample = lines[i][1].split()
    found = False
    for possible in alpha:
        clone_train = train[:]
        for j in range(len(clone_train)):
            newTrain = ""
            for k in range(len(clone_train[j])):
                newTrain += possible[ord(clone_train[j][k]) - ord('a')]
            clone_train[j] = newTrain 

        isPass = [False for i in range(10)]
        for each in clone_train:
            each = "".join(sorted(each))
            if valid.count(each) != 0:
                isPass[valid.index(each)] = True
        
        cnt = 0
        for each in isPass:
            if(each):
                cnt += 1

        if cnt == 10:
            for j in range(len(sample)):
                newTrain = ""
                for k in range(len(sample[j])):
                    newTrain += possible[ord(sample[j][k]) - ord('a')]
                sample[j] = newTrain 

            isPass = [False for i in range(10)]
            for each in sample:
                each = "".join(sorted(each))
                if valid.count(each) != 0:
                    num[valid.index(each)] += 1
            break

print(num[1] + num[4] + num[7] + num[8])