#!/bin/bash
file="val1.txt"
IFS=$'\n'
for var in $(cat $file)
do
echo "$var"
done

# This is a comment
pwd
whoami
cd GENERAL_PROJECT
git add val1.txt








