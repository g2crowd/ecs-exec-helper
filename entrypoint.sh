#!/bin/sh -l
set -e

python /src/main.py --org "$1" --repo "$2" --pr "$3"  --cluster "$4" --task "$5"

BUILD_RESULT=$?
if [ $BUILD_RESULT -eq 0 ]; then
  echo ::set-output name=success::true
  exit 0
else
  echo ::set-output name=success::false
  exit 1
fi

