#!/usr/bin/env python

class FighterClass(object):
	def __init__(self, name):
		self.name = name

	def attack(self, attacker):
		print "{} attacked".format(self.name)

	def defend(self, defender):
		print "{} defended".format(self.name)

class F1(FighterClass):
	def __init__(self, name):
		super(F1, self).__init__(name)

class F2(FighterClass):
        def __init__(self, name):
                super(F2, self).__init__(name)

def main():
	f1 = F1(name='AA')
	f2 = F2(name='BB')
	f1.attack(f2)

if __name__ == '__main__':
	main()
