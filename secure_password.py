import random
import string

# some adjectives - list can be much longer
adjectives = ['dirty', 'sleepy', 'smelly',
'jelous', 'happy', 'proud',
'chicky', 'amazing', 'brave',
'toxic', 'fluffy', 'clean',
'aware', 'smoky', 'misterious'
]

# nouns taken from bird's names
nouns = ['albatross', 'biddy', 'blackbird',
'canary', 'crow', 'cuckoo',
'dove', 'pigeon', 'duck',
'eagle', 'falcon', 'finch',
'flamingo', 'goose', 'gull',
'hawk','jackdaw', 'jay',
'kestrel', 'kookaburra', 'mallard',
'nightingale', 'nuthatch', 'ostrich',
'owl', 'parakeet', 'parrot',
'peacock', 'pelican', 'penguin',
'pheasant', 'piranha', 'raven'
'robin', 'rooster', 'sparrow',
'stork', 'swallow', 'swan',
'swift', 'tit', 'turkey',
'vulture', 'woodpecker', 'wren'
]

#nouns taken from mammal's names
nouns2 = ['armadillo','ass','bat',
'bear','beaver','cat',
'chimpanzee','cow','coyote',
'deer','dog','dolphin',
'elephant','fox','panda',
'gibbon','giraffe','goat',
'gopher','hedgehog','hippopotamus',
'horse','humpback-whale','jaguar',
'kangaroo','koala','leopard',
'lion','llama','lynx',
'mole','monkey','mouse',
'narwhal','orangutan','orca',
'otter','ox','pig',
'polar-bear','porcupine','puma',
'rabbit','raccoon','rat',
'rhinoceros','squirrel','tiger',
'walrus','weasel','wolf',
'zebra'
]

#

# not a full list of special characters
special_characters = [
'!', '@', '#',
'$', '%', '^',
'&', '*', '(',
')', '_', '|',
'?', '/', '+',
'}', '{', '=',
']', '[', '-'
]

print('Password creator 1.0')

adjective = random.choice(adjectives)
noun = random.choice(nouns)
number = random.randrange(0, 1000)
special_char = random.choice(special_characters)

password = adjective + noun + str(number) + special_char
print('Your secure password is: %s' % password)
