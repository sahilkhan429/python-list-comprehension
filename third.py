matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#FLATTEN OF MATRIX
flatten = [n for row in matrix for n in row]
print("flatten:\n",flatten)

#SQUARE OF EACH FLATTEN ITEM
flatten_and_square = [n**2 for row in matrix for n in row ]
print("flatten_and_square:\n",flatten_and_square)
#CONVERT TO FLATTEN AND RETURN ONLY SQUARE NUMBERS
flatten_only_even = [n for row in matrix for n in row if n%2==0]
print("flatten_only_even:\n",flatten_only_even)
#THIS CONCEPT SOLVE THE NESTED LOOP problem
nested_concept = [(x,y) for x in range(1,3) for y in range(1,3)]
print("nested concept:\n",nested_concept)
