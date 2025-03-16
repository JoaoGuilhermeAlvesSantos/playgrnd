#!/bin/bash 
num=${1?'Usage: $0 <number>'}
shift
echo "Number is: $num"
echo "Args before shift: $@"
shift $num
echo "Args after shift: $@"

