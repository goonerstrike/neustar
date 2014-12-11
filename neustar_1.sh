#!/bin/bash
if [[ ! $1 ]]; then
	echo "usage: ./script <output_file>"
	exit 1
fi

if [[ $UID != 0 ]]; then
	echo -e "\nOS Type: `cat /proc/version`\n"
	echo "Total Memory: `cat /proc/meminfo  | grep -i MemTotal | awk '{print $2, $3}'`"
else 
	echo "You cannot run this script as root."
fi
