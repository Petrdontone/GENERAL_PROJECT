#!/bin/bash

echo "Enter any number"
read n
echo "5"
if [[  $n -eq 15 || $n  -eq 69  ]]
then
echo "You won the game"
else
echo "You lost the game"
fi

