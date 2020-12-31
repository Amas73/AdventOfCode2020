#fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_10_training.txt'
#fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_10_training_v2.txt'
fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_10.txt'

rawdata = [int(r.strip('\n')) for r in open(fn).readlines()]

rawdata.sort()
rawdata.insert(0,0)
rawdata.append(max(rawdata)+3)

one_jolt=[]
two_jolt=[]
three_jolt=[]

for p in range(1,len(rawdata)):
  diff = rawdata[p]-rawdata[p-1]
  if diff == 1: one_jolt.append(rawdata[p])
  if diff == 2: two_jolt.append(rawdata[p])
  if diff == 3: three_jolt.append(rawdata[p])

print('Part 1:', len(one_jolt)*len(three_jolt))


memo={}
def seq(s, lst):
  if s in memo:
    return memo[s]
  if s == max(lst):
    return 1
  if s not in lst:
    return 0
  t = seq(s+1, lst) + seq(s+2, lst) + seq(s+3, lst)
  memo[s] = t
  return t

print('Part 2:', seq(min(rawdata),rawdata))