import sys
import math

def wordFit(word, lettersString):
	'''
	Test if the word can be chosen with the following letters
	'''
	fit = True
	letters = list(lettersString)
	for letter in word:
		if letter in letters:
			pos = letters.index(letter)
			letters.pop(pos)
		else:
			fit = False
	return fit

def calculateScore(word):
	'''
	Calculate a Scrabble score for the word in parameter
	'''
	letterScore = {'e' : 1, 'a': 1, 'i' : 1, 'o' : 1, 'n' : 1, 'r' : 1, 't' : 1, 'l' : 1, 's' : 1, 'c' : 1, 'u' : 1, 'd' : 2, 'g' : 2, 'b' : 3, 'c' : 3, 'm' : 3, 'p' : 3, 'f' : 4, 'h' : 4, 'v' : 4, 'w' : 4, 'y' : 4, 'k' : 5, 'j' : 8, 'x' : 8, 'q' : 10, 'z' : 10}
	score = 0
	for letter in word:
		score += letterScore[letter]

	return score

maxScore = 0
bestWord = ""
dictionnary = []

n = int(raw_input())
for i in xrange(n):
	w = raw_input()
	dictionnary.append(w)

letters = raw_input()

for word in dictionnary:
	if(wordFit(word, letters)):
		score = calculateScore(word)
		if(score > maxScore):
			maxScore = score
			bestWord = word

print bestWord