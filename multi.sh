#!/bin/bash

NUM_INSTANCES=${NUM_INSTANCES:-1}

for i in $(seq 1 $NUM_INSTANCES)
do
   python3 -u consumer.py &
done

tail -f /dev/null
