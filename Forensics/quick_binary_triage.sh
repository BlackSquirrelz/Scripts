#!/bin/zsh
#
# ===========================================================================
#
# Loops through each application in the specified directory 
# to determine the entitlements, and file headers to finding potential vulnerabilities 
# in the applications.
#
# ===========================================================================

directory=$1
report="scan_report.md"

for file in $directory/*.app; do

binary="$file/Contents/MacOS"

cat >> $report << EOF

==================== Checking $file ====================

---------------------- Entitlements --------------------

$(codesign -dv --entitlements - $file)

-------------- End of Entitlements Section -------------

-------------------- OBJDUMP ---------------------------

$(objdump -m -h $binary/**/*)

==================== Finished $file ====================


EOF
done