# Useful Commands with Grep

## Find Specific Contents in any file on the machine.
`grep "FE" $(find .. -name "*.pdb")`

Find a specific string in a bunch of files

`find . -type f | xargs grep -i 'TERM' `


## Add highlighting
`grep --color`

## Grep for a specific pid
`grep '"pid":57416' <file>`


## Grep for processes in a specific pgid
`ps -aux |grep '"pgid":57416'`


## Double Space all output
`sed G`


## Grep for a specific pid and then show the 10 lines surrounding the hits
`grep '"pid":57416' -n10 --color`


## Grep for a specific pid and only pull back the command line
`cat <file_path> | grep EXEC | grep '"pid":57416' | grep -E "(\"command\":.*?)", -o`


## Count the number of lines in any given output
`wc -l`


## look for two event types
`grep -E '(NOTIFY_FORK|NOTIFY_EXEC)' event`


## Remove certain events
`grep -v ES_EVENT_TYPE_NOTIFY_OPEN file`

## Find programs with SetUID bit
`find / -perm -4000 2>/dev/null`
