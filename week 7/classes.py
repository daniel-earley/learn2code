class Animal:
	def __init__(self, speciesType, numLegs, hasFur):
		self.speciesType = speciesType
		self.numLegs = numLegs
		self.hasFur = hasFur

	def __str__(self):
		result = self.speciesType + ", " + str(self.numLegs) + ", " + str(self.hasFur)
		return result

	def getNumLegs(self):
		return self.numLegs
	
	def setNumLegs(self, legs):
		self.numLegs = legs

class Hippo(Animal):
	def __init__(self, name, numLegs):
		super().__init__("Hippo", numLegs, False)
		self.name = name
	
	def __str__(self):
		result = self.name + ", " + self.speciesType + ", " + str(self.numLegs) + ", " + str(self.hasFur)
		return result
	
	def getName(self):
		return self.name
		

dog = Animal("Dalmation", 4, True)
dog.setNumLegs(3)
print(dog.getNumLegs())

hippo = Hippo("Poke", 4)
print(hippo)