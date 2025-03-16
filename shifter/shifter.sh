#!/bin/bash -xe
# shebang (-xe) is used to enable debugging mode

echo "Args before shift: $@"

shift 

echo "Args after shift: $@"