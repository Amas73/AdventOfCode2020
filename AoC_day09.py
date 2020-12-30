from itertools import combinations

fn,p_amt = 'c:/LocalData/aslade/AdventOfCode/2020/input_09_training.txt',5
fn,p_amt = 'c:/LocalData/aslade/AdventOfCode/2020/input_09.txt',25

rawdata = [int(r.strip('\n')) for r in open(fn).readlines()]

preamble = rawdata[:p_amt]
missing=[]
weakness=[]

for l in range(p_amt,len(rawdata)):
  comb = [sum(s) for s in combinations(preamble,2)]
  if rawdata[l] not in comb:
    missing.append(rawdata[l])
    s,e = 0,1
    while True:
      t = sum(rawdata[s:e+1])
      if t==rawdata[l]:
        weakness.append(min(rawdata[s:e+1])+max(rawdata[s:e+1]))
        break
      if t<rawdata[l]: e+=1
      if t>rawdata[l]: 
        s+=1
        while t>rawdata[l]:
          t = sum(rawdata[s:e+1])
          e+=-1
  preamble.pop(0)
  preamble.append(rawdata[l])

print('Part 1:', missing[0])
print('Part 2:', weakness[0])