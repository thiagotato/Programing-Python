from random import *
from statistics import *
from collections import *

# Six roulette wheels -- 18 red 18 black 2 greens
choice(['red'] * 18 + ['black'] * 18 + ['green'] * 2)
'red'
>>> population = ['red'] * 18 + ['black'] * 18 + ['green'] * 2
>>> [choice(population) for i in range(6)]
['black', 'black', 'black', 'red', 'green', 'red']
>>> Counter([choice(population) for i in range(6)])
Counter({'black': 3, 'red': 2, 'green': 1})
>>> choices(population, k=6)
['red', 'red', 'red', 'black', 'black', 'red']
>>> Counter(choices(population, k=6))
Counter({'red': 4, 'black': 2})
>>> choices(['red', 'black', 'green'], [18, 18, 2], k=6)
['black', 'black', 'black', 'red', 'black', 'black']
>>> Counter(choices(['red', 'black', 'green'], [18, 18, 2], k=6))
Counter({'red': 3, 'black': 2, 'green': 1})


#Deal 20 playing cards eithout replacement (16 tens, 36 low)

>>> Counter(tens=16, low=36)
Counter({'low': 36, 'tens': 16})
>>> deck = Counter(tens=16, low=36)
>>> deck = list(deck.elements())
>>> deal = sample(deck, 20)
>>> deal
['low', 'low', 'tens', 'tens', 'low', 'low', 'low', 'tens', 'low', 'low', 'tens', 'low', 'low', 'tens', 'low', 'low', 'low', 'low', 'low', 'tens']
>>> Counter(deal)
Counter({'low': 14, 'tens': 6})
>>> deal = sample(deck, 52)
>>> Counter(deal)
Counter({'low': 36, 'tens': 16})
>>> remaider = deal[20:]
>>> Counter(remaider)
Counter({'low': 22, 'tens': 10})

