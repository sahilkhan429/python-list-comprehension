numbers = list(range(1,21))
#SQUARE OF EACH ITEM OF LIST
squares = [n**2 for n in numbers]
#CUBE OF EACH ITEM OF LIST
cube = [n**3 for n in numbers]
#FILTERING EVEN NUMBERS USING LIST COMMREHENSION
even = [x for x in numbers if x % 2 == 0]
even_and_square = [x**2 for x in numbers if x % 2 == 0]
#FILTERING ODD NUMBERS USING LIST COMPREHENSION
odd = [x for x in numbers if x % 2 != 0]
odd_cubes = [x**3 for x in numbers if x % 2 != 0]
#FILTERING NUMBERS THAT DIVISIBLE BY #
devisible_by_3 = [x for x in numbers if x % 3 == 0]
#FILTERING NUMBERS GREATER THAN !)
greater_than_10 = [x for x in numbers if x >10]
#FILTERIN NUMBERS BETWEEN % AND !%
between_5_and_15 = [x for x in numbers if x >5 and x<15]
print("even_squares:\n",even_and_square)
print("squares:\n",squares)
print("cube:\n",cube)
print("Even:\n",even)
print("Odd:\n",odd)
print("odd_cubes:\n",odd_cubes)
print("Devisible by 3:\n",devisible_by_3)
print("greater_than_10:\n",greater_than_10)
print("between_5_and_15:\n",between_5_and_15)

