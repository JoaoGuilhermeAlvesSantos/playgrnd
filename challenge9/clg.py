from itertools import product

# 9 [] 9 [] 9 [] 9 = 100
numbers = [9, 9, 9, 9]
opts = ['+', '-', '*', '/', "%", "^", "&", "|", ">>", "<<"]

# calculating all possible combinations
# Generate all possible combinations of operators for the given numbers
combinations = list(product(opts, repeat=3))
print(f'Number of combinations: {len(combinations)}')
for i in range(len(opts)):
    for j in range(len(opts)):
        for k in range(len(opts)):
            try:
                res = eval(f'{numbers[0]}{opts[i]}{numbers[1]}{opts[j]}{numbers[2]}{opts[k]}{numbers[3]}')
                if res == 100:
                    print("found")
                    print(f'{numbers[0]}{opts[i]}{numbers[1]}{opts[j]}{numbers[2]}{opts[k]}{numbers[3]}', "=", res)
                    exit

            except:
                pass
# Result: some MF said that the answer concatenate 2 9's (come on...) to make a 99, so sum with a 9/9 to get your 100
# True result (come on...) is that there is no way to get 100 with 4 9's and the operators above