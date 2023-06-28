#!/bin/bash

snapshot=$1
mountpoint=$2


mount_apfs -s $snapshot /System/Volumes/Data $mountpoint
