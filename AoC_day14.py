import re, itertools as itr

#fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_14_training.txt'
#fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_14_training_v2.txt'
fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_14.txt'

rawdata = [r.strip('\n') for r in open(fn).readlines()]

mem = {}
for row in rawdata:
  instr = re.findall('^\w*',row)[0]
  if instr == 'mask':
    msk = []
    for n, v in enumerate(row.split(' = ')[1]):
      if v != 'X':
        msk.append([n,v])
  elif instr == 'mem':
    p_str, v_str = row.split(' = ')
    p = re.findall('\d+',p_str)[0]
    v = '{:036b}'.format(int(v_str))
    for n, x in msk:
      v = v[:n]+x+v[n+1:]
      mem[p] = int(v,2)

print('Part 1:',sum(mem.values()))


mem = {}
for row in rawdata:
  instr = re.findall('^\w*',row)[0]
  if instr == 'mask':
    msk = []
    for n, v in enumerate(row.split(' = ')[1]):
      if v != '0':
        msk.append([n,v])
  elif instr == 'mem':
    p=[]
    p_str, v_str = row.split(' = ')
    tmp_p = '{:036b}'.format(int(re.findall('\d+',p_str)[0]))
    v = int(v_str)
    for n, x in msk:
      tmp_p = tmp_p[:n]+x+tmp_p[n+1:]
    iterations = itr.product('01', repeat = tmp_p.count('X'))
    for i in iterations:
      t=tmp_p
      for s in i:
        t = t.replace('X',s,1)
      mem[t] = v
      
print('Part 2:',sum(mem.values()))