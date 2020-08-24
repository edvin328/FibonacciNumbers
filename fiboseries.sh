#!/bin/bash

echo "Fibonacci rindas kārtas skaitlis:" $1
n=$1
a=0
b=1

echo -n "Fibonacci rinda ar kārtas skaitli $1 ir : 0, " 

while [ "$n" != 0 ]
do
  a=$(($a+$b))
  b=$(($a-$b))
  n=$(($n-1))

  echo -n "$a, "
done

echo "<- uzdevums ir izpildīts :))))"
