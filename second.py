numbers = list(range(1,11))

#FLTERING EVEN AND ODD USING TRANSFIRMATION AND FILTERING METHOD
even_and_odd = ["even" if n %2==0 else "odd" for n in numbers]
print("even_and_odd",even_and_odd)


#STRINGS + CONDITIONS

#a simple python list that contains multiple words/strings
words = ["python","java","c++","machin learning","deep learning","SQL","data"]
#FILTERING WORDS THAT LENGTH IS GREATER THAN $
lenghty_strings = [word for word in words if len(word)>4]
#CONVERTING ALL STRINGS INTO UPPERCASE
upper_case = [word.upper()for word in words]
#CONVERTING ALL THOSE WORDS INTO UPPER CASE THAT LENGTH IS GREATER THAN 4
upper_case_and_lenghty = [word.upper()for word in words if len(word)>4]
print("epper_case:\n",upper_case)
print("lengthy_words:\n",lenghty_strings)
print("upper_case_and_lenghty:\n",upper_case_and_lenghty)
