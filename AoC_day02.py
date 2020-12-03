fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_02.txt'
in_data = [r.split(' ') for r in open(fn).readlines()]

p_cnt = 0
for row in in_data:
  rule=row[0].split('-')
  l_cnt = 0
  for p in row[2]:
    if p==row[1][:-1]: l_cnt = l_cnt +1
  if l_cnt>=int(rule[0]) and l_cnt<=int(rule[1]): p_cnt = p_cnt + 1
print ('Part 1# of passwords: ' + str(p_cnt))

p_cnt = 0
for row in in_data:
  rule=row[0].split('-')
  if (row[2][int(rule[0])-1]==row[1][:-1])^(row[2][int(rule[1])-1]==row[1][:-1]): p_cnt = p_cnt + 1
print ('Part 2# of passwords: ' + str(p_cnt))
