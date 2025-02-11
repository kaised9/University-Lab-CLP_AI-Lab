given_text = "Green University Of Bangladesh Green University Purbachal."

given_text_words = given_text.split()

given_text_words_count = {}

for word in given_text_words:
    given_text_words_count[word] = given_text_words_count.get(word, 0) + 1

print("Count Words : ",given_text_words_count)