def getSound(word):
	vowels = ['a', 'e', 'i', 'o', 'u']
	assert type(word) == str
	length = len(word)
	assert length > 0
	sound = []

	if length <= 2:
		sound = [word]
	elif length % 2 == 0:
		if word[0] in vowels and word[-1] not in vowels:
			if length == 3:
				sound = [word]
			elif length == 4:
				sound.append(word[0])
				sound.append(word[::-1][0:3][::-1])
			else:
				sound.append(word[0])
				for index in range(1,length-4,2):
					sound.append(word[index] + word[index+1])
				sound.append(word[::-1][0:3][::-1])
		else:
			for index in range(0,length-1,2):
				sound.append(word[index] + word[index+1])
	else:
		if word[0] in vowels:
			sound.append(word[0])
			for index in range(1,length-1,2):
				sound.append(word[index] + word[index+1])
		else: 
			for index in range(0,length-4,2):
				sound.append(word[index] + word[index+1])
			sound.append(word[::-1][0:3][::-1])

	return sound

class word():
	def __init__(self, spelling, definition):
		self.spelling = spelling
		self.definition = {}
		self.sound = getSound(spelling)

		defList = definition.strip().split(':')
		if len(defList) >= 2:
			self.definition[defList[0]] = [defList[1].split('.')[0]]
		else:
			self.definition[None] = [definition]

	def addDefinition(self, key, newDefinition):
		if key in self.definition:
			if type(self.definition[key]) != list:
				self.definition[key] = [self.definition[key], newDefinition]
			else:
				self.definition[key].append(newDefinition)
		else: 
			self.definition[key] = newDefinition

	def printDefinitions(self):
		print(f'\t{self.spelling}')
		for key in self.definition.keys():
			print(f'\t\t{key}: {self.definition[key][0]}')
			if len(self.definition[key]) > 1:
				for definition in self.definition[key][1:]:
					print(f'\t\t\t{definition}')


class rhymeDictionary():
	def __init__(self, *words):
		self.words = [word for word in words]

	def addWord(self, newWord):
		match = self.findWord(newWord.spelling)
		if match == False:
			self.words.append(newWord)
		else:
			match.addDefinition(list(newWord.definition.keys())[0], newWord.definition[list(newWord.definition.keys())[0]])

	def findWord(self, spelling):
		for word in self.words:
			if word.spelling == spelling:
				return word
		return False

	def findRhymes(self, prototype, lowest=1):
		rhymes = {}
		protoypeSound = getSound(prototype)
		for word in self.words:
			if word.spelling != prototype:
				score = 0
				if len(protoypeSound) == 1:
					if prototype[-1] == word.spelling[-1]:
						score += 2
					try:
						if prototype[-2] == word.spelling[-2]:
							score += 2
					except IndexError:
						continue
				else:
					for wordIndex, prototypeIndex in zip(range(0,len(word.sound)), range(0,len(protoypeSound))):
						if word.sound[wordIndex] == protoypeSound[prototypeIndex]:
							score += 3
						elif word.sound[wordIndex] in protoypeSound[prototypeIndex] or protoypeSound[prototypeIndex] in word.sound[wordIndex]:
							score += 2
						elif word.sound[wordIndex][0] == protoypeSound[prototypeIndex][0]:	
							score += 1
						elif len(word.sound[wordIndex]) >= 2 and len(protoypeSound[prototypeIndex]) >= 2 and word.sound[wordIndex][1] == protoypeSound[prototypeIndex][1]:
							score += 1
				if score >= lowest:
					if score in rhymes:
						rhymes[score].append(word)
					else:
						rhymes[score] = [word]
		return rhymes