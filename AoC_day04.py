import re
fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_04.txt'
#training data
#fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_04_training.txt'
#fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_04_training_p2valid.txt'
in_data = [r for r in open(fn).readlines()]

#join data not separated by an empty line & remove the extra \n
in_data = [r.replace('\n','') for r in ' '.join(in_data).split('\n \n ')]
flds = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
opt_flds = ['cid']

v_passports = 0
for row in in_data:
  valid=True
  for chk in flds:
    if chk not in row: valid=False
  if valid: v_passports +=1
print ('Part 1: Valid Passports = '+str(v_passports))

regex_flds = [r'byr:(200[0-2]|19[2-9][0-9])\b',r'iyr:(201[0-9]|2020)\b',r'eyr:(202[0-9]|2030)\b',r'hgt:(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)\b',r'hcl:(\#([0-9]|[a-f]){6})\b',
              r'ecl:(amb|blu|brn|gry|grn|hzl|oth)\b',r'pid:(\d{9})\b']
v_passports = 0
for row in in_data:
  valid=True
  for chk in regex_flds:
    if not(re.findall(chk,row)): valid=False
  if valid: v_passports +=1
print ('Part 2: Valid Passports = '+str(v_passports))
