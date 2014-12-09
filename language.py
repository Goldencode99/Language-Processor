import random

def process(sentence):
	chopped=sentence.split()
	for place, word in enumerate(chopped):
		if word not in wordBank:
			wordBank.append(word)
			wordFollowers[word] = []
		if place < len(chopped)-1:
			wordFollowers[word].append(chopped[place+1])
			

def generateSentence():
	sentence = []
	seedWord = random.choice(wordBank)
	while seedWord[0].islower():
		seedWord = random.choice(wordBank)
	sentence = [seedWord]
	while seedWord[len(seedWord)-1] not in [".","!","?"]:
		seedWord=random.choice(wordFollowers[seedWord])
		sentence.append(seedWord)
	return " ".join(sentence)

wordBank = []
wordFollowers = {}

print "Enter training text:"
process(raw_input())
print ""
for i in xrange(10):
	print generateSentence()