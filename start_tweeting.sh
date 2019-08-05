#!/bin/bash
line_file='./_seacabo.txt'

dir = os.listdir(os.getcwd())
print dir
simulation_file='./simulation.txt'
sed -i 's/\r//' $simulation_file
total_lines=($(wc -l $file))
total_lines=${total_lines[0]}

line=1
while not line_file.is_file():
  line_file=line+'.txt'
  if line > total_lines:
    return
  line=line+1

python -c "import services.api; services.api.tweet_line_from_file('$simulation_file','$line')"

os.rename($line_file, str($line) + '.txt')
