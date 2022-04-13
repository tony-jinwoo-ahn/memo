#!/bin/bash
rm -f result.log

for (( c=1; c<=5; c++ ))
do
#	echo "Welcome $c times..."
    echo "Welcome $c times..." >> result.log
    sleep 1
done
