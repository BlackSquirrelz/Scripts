#!/bin/zsh


file=$1
n=$2

hexdump -n $n -C $file

