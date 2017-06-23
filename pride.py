class pFloat:
  def __init__(self, index):
    self.index = index

  def setColor(self, color):
    # red, orange, yellow, green, blue, violet, pink
    self.color = color

  def setName(self, name):
    # Christopher, Courtney, Harvey, Kimball, Li, Patria, Phyllis
    self.name = name

  def setDirection(self, direction):
  	# west, east
    self.direction = direction

  def canSee(self, who):
  	if self.direction == 'east':
  		return who.index > self.index
  	else:
  		return who.index < self.index

  def howManyISee(self):
  	if self.direction == 'west':
  		return self.index
  	else:
  		return 6 - self.index

  def getNeighbors(self):
  	neighbors = []
  	if self.index > 0:
  		neighbors.append(floatArray[self.index - 1])
  	if self.index < 6:
  		neighbors.append(floatArray[self.index + 1])
  	return neighbors

  def getFloatInFront(self):
  	if self.direction == 'east':
  		if self.index < 6:
  			return floatArray[self.index + 1]
  	else:
  		if self.index > 0:
  			return floatArray[self.index - 1]
  	return None

  def getLetter(self):
    if self.index >= len(self.name):
      return ''

    if self.direction == 'east':
      return self.name[self.index]
    else:
      return self.name[-(self.index + 1)]

def findColor(color):
  for f in floatArray:
  	if f.color == color:
  		return f

def findName(name):
  for f in floatArray:
  	if f.name == name:
  		return f

## Rules
varx = 0
vary = 0
varz = 0

def rule1():
	# The person in the orange float can see exactly x floats 
	# more than Phyllis can, where x is some number.
	global varx
	orange = findColor('orange')
	phyllis = findName('Phyllis')
	varx = orange.howManyISee() - phyllis.howManyISee()
	return True

def rule2():
  # If the blue and violet floats are facing the same direction, 
  # then Patria is in one of those floats; otherwise, Patria is in the green float.
  blue = findColor('blue')
  violet = findColor('violet')
  if blue.direction == violet.direction:
  	return 'Patria' in (blue.name, violet.name)
  else:
  	green = findColor('green')
  	return green.name == 'Patria'

def rule3():
	# The person in the blue float can see, directly in front of it, 
	# another float whose driver has x letters in his/her name.
	global varx
	blue = findColor('blue')
	neighbor = blue.getFloatInFront()
	if neighbor is None:
		return False
	else:
		return len(neighbor.name) == varx

def rule4():
	# There is an even number of floats between Harvey's and 
	# the pink float (not including themselves).
	harvey = findName('Harvey')
	pink = findColor('pink')
	return abs(harvey.index - pink.index + 1) % 2 == 0

def rule5():
	# The red float is the farthest west.
	return floatArray[0].color == 'red'

def rule6():
	# If Courtney's float is blue, orange, violet, or green, 
	# then at least one of Courtney's neighbors has a name containing the letter Y.
	# CONTRAPOSITIVE
	courtney = findName('Courtney')
	cNeighbors = courtney.getNeighbors()
	if courtney.color in ('blue', 'orange', 'violet', 'green'):
		for neighbor in cNeighbors:
			if 'y' in neighbor.name:
				return True
		return False
	else:
		# for neighbor in cNeighbors:
		# 	if 'y' in neighbor.name:
		# 		return False
		return True

def rule7():
	# Harvey can see Kimball's float directly in front of him.
	harvey = findName('Harvey')
	kimball = findName('Kimball')
	return harvey.canSee(kimball)

def rule8():
	# The violet float is next to the yellow float if and only if Li's float is pink.
	li = findName('Li')
	violet = findColor('violet')
	yellow = findColor('yellow')
	if li.color == 'pink':
		return abs(violet.index - yellow.index) == 1
	else:
		return abs(violet.index - yellow.index) != 1

def rule9():
	# The people in the orange and pink floats can see the blue float somewhere ahead.
	orange = findColor('orange')
	pink = findColor('pink')
	blue = findColor('blue')
	return orange.canSee(blue) and pink.canSee(blue)

def rule10():
	# If Li's float is east of Harvey's, then Li's float is either orange or pink.
	# CONTRAPOSITIVE
  liColors = ('orange', 'pink')
  li = findName('Li')
  harvey = findName('Harvey')
  if li.index > harvey.index:
    return li.color in liColors
  else:
		# return li.color not in liColors
    return True

def rule11():
	# If Harvey's float is red or orange, then Kimball's float is a primary color.
	# CONTRAPOSITIVE
  primary = ('red', 'yellow', 'blue')
  harvey = findName('Harvey')
  kimball = findName('Kimball')
  if harvey.color in ('red', 'orange'):
    return kimball.color in primary
  else:
		# return kimball.color not in primary
    return True

def rule12():
	# If the red and yellow floats are next to each other, 
	# then the person in the red float can see fewer than y other floats, where y = x + 1.
	# CONTRAPOSITIVE
  global varx
  global vary
  vary = varx + 1
  red = findColor('red')
  yellow = findColor('yellow')
  if abs(red.index - yellow.index) == 1:
    return red.howManyISee() < vary
  else:
		# return red.howManyISee() >= vary
    return True

def rule13():
	# If Christopher's float is a secondary color, 
	# then he can see more floats than Courtney can.
	# CONTRAPOSITIVE
  secondary = ('orange', 'green', 'violet')
  christopher = findName('Christopher')
  courtney = findName('Courtney')
  if christopher.color in secondary:
    return christopher.howManyISee() > courtney.howManyISee()
  else:
    # return christopher.howManyISee() <= courtney.howManyISee()
    return True

def rule14():
	# The person in the red float has a name that is z letters long, where z = x * y.
	global varx
	global vary
	global varz
	varz = varx * vary
	red = findColor('red')
	return len(red.name) == varz

def rule15():
	# The pink, violet, and green floats are facing the same direction.
  pink = findColor('pink')
  violet = findColor('violet')
  green = findColor('green')
  return pink.direction == violet.direction and pink.direction == green.direction

#### Run

floatArray = []
for i in range(7):
	floatArray.append(pFloat(i))

allNames = ['Christopher', 'Courtney', 'Harvey', 'Kimball', 'Li', 'Patria', 'Phyllis']
allColors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'pink']
# allColors = ['red', 'pink', 'violet', 'blue', 'green', 'yellow', 'orange']
allDirections = ['east', 'west']
allRules = [rule1, rule2, rule3, rule4, rule5,
						rule6, rule7, rule8, rule9, rule10,
						rule11, rule12, rule13, rule14, rule15]

def addColor(colorArray, index):
  for i in range(len(colorArray)):
  	floatArray[index].setColor(colorArray[i])
  	if index == 6:
  		addName(allNames, 0)
  	else:
  		newColorArray = colorArray[:i] + colorArray[i + 1:]
  		addColor(newColorArray, index + 1)

def addName(nameArray, index):
  for i in range(len(nameArray)):
  	floatArray[index].setName(nameArray[i])
  	if index == 6:
  		addDirection(allDirections, 0)
  	else:
  		newNameArray = nameArray[:i] + nameArray[i + 1:]
  		addName(newNameArray, index + 1)

def addDirection(dirArray, index):
  for i in range(len(dirArray)):
  	floatArray[index].setDirection(dirArray[i])
  	if index == 6:
  		checkRules()
  	else:
  		addDirection(dirArray, index + 1)

def printArray():
  for f in floatArray:
    print f.color, f.name, f.direction

def printAnswer():
  answer = ''
  for f in floatArray:
    answer += f.getLetter()
  return answer

numArray = 0
def checkRules():
  global numArray
  numArray += 1
  if numArray % 10000 == 0:
    print numArray
    printArray()
  for rule in allRules:
    if not rule():
      return
  with open('answer.txt', 'a') as af:
    for f in floatArray:
      af.write(f.color + ' ' + f.name + ' ' + f.direction + '\n')
    af.write(printAnswer() + '\n')
    af.write('\n')

addColor(allColors, 0)