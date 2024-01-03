#!/usr/bin/python3
for _char in range(97,123):
  if _char == 113 or _char == 101:
     continue
  print('{}'.format(chr(_char)), end='')

