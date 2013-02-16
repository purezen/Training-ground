#!/usr/bin/env python

class Dog():
	def __init__(self,dogname,dogcolour,dogheight,dogbuild,dogmood,dogage):
		#Here we setup the attributes of dog
		self.name=dogname
		self.colour=dogcolour
		self.height=dogheight
		self.build=dogbuild
		self.mood=dogmood
		self.age=dogage
		self.Hungry=False
		self.Tired=False

	def Eat(self):
		if self.Hungry:
			print "Yum Yum.. Num Num.."
			self.Hungry= False
		else:
			print "Sniff Sniff.. Not Hungry"

	def Sleep(self):
		print "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZzzzzzzzzzzz"
		self.Tired=False

	def Bark(self):
		if self.mood=='Grumpy':
			print "Grrrrr.. Woof woof..."
		elif self.mood=='Laid Back':
			print 'Yawn.. ok.. woof..'
		elif self.mood=='Crazy':
			print 'Bark bark bark bark bark bark...'
		else:
			print 'Woof woof..'

Beagle=Dog('Archie','Brown','Short','Chubby','Grumpy',12)
print 'My name is %s' %Beagle.name
print 'My colour is %s' %Beagle.colour
print 'I am %s' %Beagle.mood
Beagle.Hungry=False
Beagle.Eat()
Beagle.Bark()
