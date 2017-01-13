def break_words(stuff):
	"This function will break up words for us."
	words = stuff.split(' ')
	return words

def sort_words(word):
	"this sort the words. "
	return sorted(word)

def print_first_word(word):
	"print first word."
	return word.pop()

def print_last_word(word):
	"print last word"
	return word.pop(-1)

def sort_sentence():
	words = break_words("this function will sort sentence")
	return sort_words(words)

words = break_words("My name ?")
print words
sorted_words = sort_words(words)
print sorted_words
first_word = print_first_word(words)
print first_word
last_word = print_last_word(words)
print last_word
sort_sentence = sort_sentence()
print sort_sentence
