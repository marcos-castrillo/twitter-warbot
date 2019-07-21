#!/bin/bash 
sed -i 's/\r//' *
chmod +x ./main.py
./main.py &
