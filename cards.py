#deck of cards
import itertools,random
deck=list(itertools.product(range(1,14),['spade','heart','diamond','club']))
random.shuffle(deck)
print('THE CARDS ARE:')
n=int(input("n"))
for i in range(n):
    print(deck[i][0],deck[i][1])
