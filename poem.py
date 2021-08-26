'''
This parses the dictionary text file
Entries may be added, but the must follow the format of:
	(WORD WITHOUT SPACES)
	usage: definition
'''
from toki import *
from random import sample

rhymeDict = rhymeDictionary()

print("Welcome to Jan Wajen's Toki Pona Rhyming Dictionary Tool!\n")
print("Loading dictionary now...")

with open("./dict.txt", "r") as file:
	fileList = file.readlines()
	for index, line in enumerate(fileList):
		line = line.strip()
		if len(line) != 0:
			if '//' not in line and ' ' not in line:
				if str('!') in line:
					line = ''.join(line.split('!'))
				newWord = word(line, fileList[index+1])
				rhymeDict.addWord(newWord)

print("Dictionary loaded!")

while len(rhymeDict.words) != 0:
	print(len(rhymeDict.words), ' words left')
	words = sample(rhymeDict.words, 10)
	for word in words:
		word.printDefinitions()
	
	print("")

	for word in words:
		print(word.spelling, end=' ')

	remove = input("\nEnter words to remove: ").split(' ')
	
	for word in remove:
		word = rhymeDict.findWord(word)
		if word == False:
			continue
		else:
			rhymeDict.words.remove(word)

'''
	print("\nPlease enter one or more words separated by spaces to retrieve rhymes")
	print("Insert a number at the end of the query only retrieve rhymes with a score of that number or higher (default 3)")
	print("Alternatively, type 'exit' or 'quit' to close the dictionary")
	search = input("Enter phrase: ").strip()
	if search == 'exit' or search == 'quit':
		quit()

	lowest = 3
	search = [item.strip() for item in search.split(' ')]
	for item in search:
		if item.isdigit():
			lowest = int(item)
			search.remove(item)

	for word in search:
		rhymes = rhymeDict.findRhymes(word, lowest=lowest)
		if len(rhymes) == 0:
			print(f'No results for word "{word}"')
			continue
		else:
			results = True
			print(f'{word}:')
			keysList = list(rhymes.keys())
			keysList.sort()
			keysList.reverse()
			for key in keysList:
				print(f'{key} Points:')
				for result in rhymes[key]:
					result.printDefinitions()
'''