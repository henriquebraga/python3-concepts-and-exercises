'''
__getitem__ and __len__ methods.
Special thanks to Luciano Ramalho and his book Fluent Python (highly recommended after
spending some time with Python :)) with a really
brilliant explanation covering about built-in python functions.

Python really looks like a 'framework', we implement some methods that are gonna
be called later by it and then
we get a complete infrastructure to use (all due to its great DATA MODEL also known as
Python Data Model) :)

This special methods are always followed by __[built-in-function-name]__ (double or dunder)
and that it's not recommended to call them directly (excepted by sub-classes that need
to call __init__ method from their parents).

Below it's an example from Fluent Python with a FrenchDeck.
Notice both methods __len__ and __getitem__ are implemented.

Just by that, there are bunch of thing we can do with this class. 
Let's take a look:

First of all, the class is completely able to use len() method such as:
len(deck) due to __len__ implementation;

Just by implementing __getitem__, our class has support for slicing operations (since it comes
to be a immutable sequence also because of __getitem__ implementation). 

And also, since we've implemented __getitem__, our deck is iterable :). so we could something
like that in our class:

for card in deck:
	print(card)

'''

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
	ranks = [str(n) for n in range(2, 11)] + list('JQKA')
	suits = 'spades diamonds clubs hearts'.split()

	def __init__(self):
		self._cards = [Card('rank', 'suit') for suit in self.suits for rank in self.ranks]

	def __getitem__(self, pos):
		return self._cards[pos]

	def __len__(self):
		return len(self._cards)


deck = FrenchDeck()

print(deck[0]) 
print(deck[1:5]) #Supports slicing
for card in deck: #It's iterable! :)
	print(card) 

from random import choice
print(choice(deck)) #It's a sequence!





		



