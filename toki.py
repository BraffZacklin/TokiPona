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
		self.definition = definition
		self.sound = getSound(spelling)

	def addDefinition(self, key, newDefinition):
		try:
			if self.definition[key]:
				if type(self.definition[key]) != list:
					self.definition[key] = [self.definition[key], newDefinition]
				else:
					self.definition[key].append(newDefinition)
		except KeyError:
			self.definition[key] = newDefinition

class rhymeDictionary():
	def __init__(self, *words):
		self.words = [word for word in words]

	def findRhyme(self, prototype):
		rhymes = {}
		protoypeSound = getSound(prototype)
		for word in self.words:
			if word != prototype:
				score = 0
				for wordIndex, prototypeIndex in zip(range(0,len(word.sound)), range(0,len(protoypeSound))):
					if word.sound[wordIndex] == protoypeSound[prototypeIndex]:
						score += 3
					elif word.sound[wordIndex] in protoypeSound[prototypeIndex] or protoypeSound[prototypeIndex] in word.sound[wordIndex]:
						score += 2
					elif word.sound[wordIndex][0] == protoypeSound[prototypeIndex][0]:	
						score += 1
					elif len(word.sound[wordIndex]) >= 2 and len(protoypeSound[prototypeIndex]) >= 2 and word.sound[wordIndex][1] == protoypeSound[prototypeIndex][1]:
						score += 1
				if score > 0:
					if score in rhymes:
						rhymes[score].append(word.spelling)
					else:
						rhymes[score] = [word.spelling]
		return rhymes