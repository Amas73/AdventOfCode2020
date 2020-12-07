fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_06.txt'
#training data
#fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_06_training.txt'
rawdata = open(fn).read()

#join data not separated by an empty line & remove the extra \n
in_data = [r.split('\n') for r in rawdata.split('\n\n')]

tot = 0
grp_q = []
for grp in in_data:
  questions = []
  for row in grp:
    for r in row:
      if r not in questions: questions.append(r)
  grp_q.append(''.join(questions))
  tot += len(questions)
print('Part 1: '+str(tot))

tot = 0
for i,grp in enumerate(grp_q):
  for r in grp:
    cnt=0
    for row in in_data[i]:
      if r in row: cnt += 1
    if cnt==len(in_data[i]): tot += 1
print('Part 2: '+str(tot))
