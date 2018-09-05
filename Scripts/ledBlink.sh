#!/bin/bash

gpio mode 0 out

for i in `seq 0 9`
do
gpio write 0 1
sleep 0.5
gpio write 0 0
sleep 0.5
done
