matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
flatten = [n for row in matrix for n in row]
squares = [n**2 for row in matrix for n in row]
even = [n for row in matrix for n in row if n %2==0]
odd = [n for row in matrix for n in row if n %2!=0]
greater_than_5 = [n for row in matrix for n in row if n>5]
flatten_square_only_even = [n**2 for row in matrix for n in row if n%2==0]
number_square_pairs = {number:number**2 for row in matrix for number in row}
number_even_odd_pairs = {number:"even" if  number%2==0 else "odd" for row in matrix for number in row}

print("flatten:\n",flatten)
print("squares:\n",squares)
print("even:\n",even)
print("odd;\n",odd)
print("greater_than_5:\n",greater_than_5)
print("flatten_square_only_even:\n",flatten_square_only_even)
print("number_square_pairs:\n",number_square_pairs)
print("number_even_odd_pairs:\n",number_even_odd_pairs)