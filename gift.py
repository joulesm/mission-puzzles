letters = [
'AMV',
'EAZ',
'KOYSB',
'OPQRSTU',
'YRGI',
'N',
'OPE',
'AY',
'ABCDEFG',
'ZFOKJIJ',
'R',
'PYIER',
'ITHDBS'
]

options = ['']
for i in range(len(letters)): # i = 0
  temp_options = []
  for k in range(len(options)): # k = 0, range 1
    for j in range(len(letters[i])): # j = 0, range 3
      temp_options.append(options[k] + letters[i][j]) # '' + A
  options = temp_options # options = 'A'

with open('gift.txt', 'w') as f:
  for o in options:
    f.write(o + '\n')

# i is where we are in the array
# return array of strings that are the combos
#def combo(i):
#  if i == len(letters):
#      return ''
#  for word in letters[i:]:
#    return letter + combo()
