#!/bin/bash

#fix working directory
cd "$(dirname "$0")"
# Test shifter.sh
echo "Testing shifter.sh"
chmod +x shifter.sh
./shifter.sh 1 2 3 4 5


echo "Test shifter_num.sh"
chmod +x shifter_num.sh
./shifter_num.sh 3 1 2 3 4 5

# Back to the original directory
cd - > /dev/null