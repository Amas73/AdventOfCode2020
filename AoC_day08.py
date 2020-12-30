import copy

fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_08.txt'
#fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_08_training.txt'

rawdata = [r.strip('\n').split(' ') for r in open(fn).readlines()]

def instruction_loop(data):
  accumulator = 0
  pos = 0
  checked = []
  while pos not in checked:
    checked.append(pos)
    if data[pos][0] == 'acc':
      accumulator += int(data[pos][1])
      pos += 1
    elif data[pos][0] == 'jmp':
      pos += int(data[pos][1])
    elif data[pos][0] == 'nop':
      pos += 1
    if pos >= len(data):
      break
  return (accumulator,len(data)==pos)

print('Part 1:', instruction_loop(rawdata)[0])

fixed_data = rawdata
c_pos = 0
chg_code = 'jmp'
while not instruction_loop(fixed_data)[1]:
  while True:
    c_pos += 1
    if c_pos >= len(rawdata):
      if chg_code == 'jmp':
        chg_code = 'nop'
        c_pos = 0
      else:
        break
    if rawdata[c_pos][0] == chg_code:
      break
  if c_pos >= len(rawdata) and chg_code == 'nop':
    break
  fixed_data = copy.deepcopy(rawdata)
  if chg_code == 'jmp':
    fixed_data[c_pos][0] = 'nop'
  else:
    fixed_data[c_pos][0] = 'jmp'

print('Part 2:', instruction_loop(fixed_data)[0])