#!/bin/sh
echo "Compiling main..."
gcc -o main main.c -lm

echo "Executing main...--"
./main < in.txt

echo "--"
echo "Execution completed!"
exit
