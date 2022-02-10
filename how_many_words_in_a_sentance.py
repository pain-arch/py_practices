
#if you want you can change the string
string_words = '''Then you’re in the right place Then We know how important it is to keep a regular publishing schedule .'''

word_list = string_words.split()

word_freq = [word_list.count(n) for n in word_list]

print("String:\n {} \n".format(string_words))

#list of used Words
print("List:\n {} \n".format(str(word_list)))

#list of the number of used Words
print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(word_list, word_freq)))))