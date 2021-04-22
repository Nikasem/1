#1
fruit = ('apple', 'pear', 'cherry', 'banana', 12)
vegetables = ['tomato', 'onion', 'carrot', 17]
berries = ('blueberry', 'cranberry', 'watermelon', 8)
fruit= list(fruit)
fruit[2] = 'watermelon'
berries = list(berries)
berries[2] = 'cherry'
vegetables.insert(3, 'cabbage')
fruit = tuple(fruit)
vegetables = tuple(vegetables)
berries = tuple(berries)
print (fruit)
print (berries)
print (vegetables)
#2
shop = {'fruit' : ['apple', 'pear', 'watermelon', 'banana', 12], 'vegetables' : ['tomato', 'onion', 'carrot', 'cabbage', 17],
        'berries' : ['blueberry', 'cranberry', 'cherry', 8]  }
#3
finished = []
finished.append ("carrot")
finished.append ('watermelon')
print(finished)
fruit = list(fruit)
vegetables = list(vegetables)
fruit =fruit.remove('watermelon')
print(fruit)
#4


