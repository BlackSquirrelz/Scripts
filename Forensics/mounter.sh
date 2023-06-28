#!/bin/zsh

image=$1

echo "Attempt to Attach Image $image"

hdiutil attach -noverify -noautofsck $image -shadow

echo "Success"



