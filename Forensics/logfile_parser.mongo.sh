#!/bin/bash

# MongoDB Log File Parser
# ----------------------------------------------------------------------------------------------
#
# This script is licensed under the MIT License.
# Copyright (c) 2024 BlackSquirrelz
#
# Description:
# This script parses the MongoDB log file and extracts specific fields to a CSV file,
# ready to be ingested into a data analysis tool for further investigation.
#
# Usage:
#
# ./logfile_parser.mongo.sh -f <logfile> -o <outfile> [-v]
#
# ---------------------------------------------------------------------------------------------- 


# This script parses the mongodb log file
parse_logfile() {

    echo "[+] Parsing MongoDB log file..."
    local logfile=$1
    local outfile=$2

    if [ -z "$logfile" ]; then
        echo "Usage: $0 <logfile>"
        exit 1
    fi

    # Delete the Outfile if already 
    echo "[+] Deleting the Outfile if already exists..."
    >"$outfile"

    # Check if outfile has csv ending and append it if not
    if [[ ! "$outfile" =~ \.csv$ ]]; then
        outfile="${outfile}.csv"
    fi

    # Define the header for the CSV file
    header="Date,Timezone,Severity,Components,Identifier,CTX,SVC,Message,Attributes,Tags,Truncated,Size,IP Address,Port"
    echo "$header" >> "$outfile"

    # Extract specific fields from a JSON file
    echo "[+] Extracting fields from the log file..."
    while IFS= read -r line; do

        # Extract fields using grep or perl
        t_datetime=$(echo "$line" | awk '{ print $1 }' | grep -iEo '([0-9]{4}\-[0-9]{2}\-[0-9]{2}T[0-9]{2}\:[0-9]{2}\:[0-9]{2}\.[0-9]{3}\+[0-9]{2}\:[0-9]{2})')
        timezone=$(echo "$t_datetime" | awk -F'+' '{ print $2 }')
        severity=$(echo "$line" | perl -nle 'print $& if m{"s":"\K[^"]+}')
        components=$(echo "$line" | perl -nle 'print $& if m{"c":"\K[^"]+}')
        identifier=$(echo "$line" | perl -nle 'print $& if m{"id":\K\d+}')
        ctx=$(echo "$line" | perl -nle 'print $& if m{"ctx":"\K[^"]+}')
        svc=$(echo "$line" | perl -nle 'print $& if m{"svc":"\K[^"]+}')
        msg=$(echo "$line" | perl -nle 'print $& if m{"msg":"\K[^"]+}')
        attr=$(echo "$line" | perl -nle 'print $& if m{"attr":"\K[^"]+}')
        tags=$(echo "$line" | perl -nle 'print $& if m{"tags":"\K[^"]+}')
        truncated=$(echo "$line" | perl -nle 'print $& if m{"truncated":"\K[^"]+}')
        size=$(echo "$line" | perl -nle 'print $& if m{"size":"\K[^"]+}')
        ip_address=$(echo "$line" | grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}')


        if [ -z "$ip_address" ]; then
            ip_address=$(echo "$line" | grep -oE '([0-9a-fA-F]{1,4}\:){7}[0-9a-fA-F]{1,4}')
            port=$(echo "$line" | grep -oE '([0-9]{1,5})$')
        fi

        if [ $verbose ]; then
            echo "Date: $t_datetime"
            echo "Timezone: $timezone"
            echo "Severity: $severity"
            echo "Components: $components"
            echo "Identifier: $identifier"
            echo "CTX: $ctx"
            echo "SVC: $svc"
            echo "Message: $msg"
            echo "Attributes: $attr"
            echo "Tags: $tags"
            echo "Truncated: $truncated"
            echo "Size: $size"
            echo "IP Address: $ip_address"
            echo "Port: $port"
            echo "----------------------"
        fi
        
        echo "$t_datetime,$timezone,$severity,$components,$identifier,$ctx,$svc,$msg,$attr,$tags,$truncated,$size,$ip_address,$port" >> "$outfile"

    done < "$logfile"

    echo "[+] Parsing completed. Results are stored in $outfile"
}

# Check if the required arguments are provided
if [ $# -lt 4 ]; then
    echo "Usage: $0 -f <logfile> -o <outfile>"
    exit 1
fi

# Parse the command line arguments
while getopts ":f:o:v" opt; do
    case $opt in
        f)
            logfile=$OPTARG
            ;;
        o)
            outfile=$OPTARG
            ;;
        v)
            verbose=true
            ;;
        \?)
            echo "Invalid option: -$OPTARG"
            exit 1
            ;;
        :)
            echo "Option -$OPTARG requires an argument."
            exit 1
            ;;
    esac
done


# Call the parse_logfile function with the provided arguments
parse_logfile "$logfile" "$outfile"