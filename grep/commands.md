# Useful Commands with Grep

## Find Specific Contents in any file on the machine.
`grep "FE" $(find .. -name "*.pdb")`

Find a specific string in a bunch of files

`find . -type f | xargs grep -i 'TERM' `
