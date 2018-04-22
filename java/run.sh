#!/bin/sh
echo "Compiling main..."
javac Main.java

echo "Executing main...--"
java Main < in.txt

echo "--"
echo "Execution completed!"
exit
