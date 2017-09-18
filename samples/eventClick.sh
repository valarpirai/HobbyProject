#!/bin/bash

n=$1

for (( c=1; c<=$n; c++ ))
do
	adb shell input tap 385 455
done

echo "We are done!!! $n clicks.."
