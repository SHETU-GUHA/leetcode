def length_of_last_word(s):
	words = s.split()
	if len(words) ==0:
	   return 0
	return len(words[-1])
print(length_of_last_word(" Welcome To Hello World"))
print(length_of_last_word("How Are You?"))
print(length_of_last_word(""))

