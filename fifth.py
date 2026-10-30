
words = ["python","machine","learning","ai","data","science","deep","nueral"]

length_of_words = [len(word)for word in words]

uppercase_of_every_word = [word.upper() for word in words]

words_greter_than_4_charcters = [word for word in words if len(word)>4]

words_shorter_than_4_charcters = [word for word in words if len(word)<4]

words_contains_a = [word for word in words if "a" in word.upper()]

words_contains_a_upper = [word for word in words if "a" in word.lower()]
first_letter_of_each_word = [word[0] for word in words]

last_letter_of_each_word = [word[-1] for word in words]

words_whose_length_is_even =[word for word in words if len(word)%2==0]

reverse_each_word = [word[::-1]for word in words]


print("length of word:\n",length_of_words)
print("upper words:\n",uppercase_of_every_word)
print("words with len>4:\n",words_greter_than_4_charcters)
print("words with len<4:\n",words_shorter_than_4_charcters)
print("words contain a:\n",words_contains_a)
print("words contain a upper:\n",words_contains_a_upper)
print("first_letter_of_each_word:\n",first_letter_of_each_word)
print("last_letter_of_each_word:\n",last_letter_of_each_word)
print("words_whose_length_is_even:\n",words_whose_length_is_even)
print("reverse_each_word:\n",reverse_each_word)

