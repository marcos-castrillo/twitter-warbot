#!/bin/bash
file=$1
sed -i 's/\r//' $file
lines=($(wc -l $file))
lines=${lines[0]}
i=1
while [ "$i" -lt "$lines" ]; do
    python -c "import services.api; services.api.tweet_line_from_file('$file','$i')"
    i=$((i+1))
done
