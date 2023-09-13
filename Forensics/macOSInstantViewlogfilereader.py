#!/bin/python3

import sys

def process_file(input_file, output_file, char_mapping):
    with open(input_file, 'r') as file_in, open(output_file, 'w') as file_out:
        for line in file_in:
            modified_sentence = replace_chars(line.strip(), char_mapping)
            print(modified_sentence)
            file_out.write(modified_sentence + '\n')


def replace_chars(sentence, char_map):
    # Initialize an empty result string
    result = ''

    # Iterate through each character in the input sentence
    for char in sentence:
        # Check if the character is in the char_map dictionary
        if char in char_map:
            # If it is, replace it with the corresponding value
            result += char_map[char]
        else:
            # If not, keep the original character
            result += char

    return result

def main():

    char_mapping = {"0":"a", "1":"b", "2":"c", "3":"D", "4":"e", "5":"f","6":"g","7":"h","8":"i","9":"j","a":"k","b":"l","c":"m",
"d":"n","e":"o","f":"p","g":"q","h":"r","i":"s","j":"t","k":"u","l":"v","m":"w","n":"x","o":"y","p":"z","q":"0","r":"1",
"s":"2","t":"3","u":"4","v":"5","w":"6","x":"7","y":"8","z":"9","A":"A","B":"L","C":"C","D":"n","E":"o","F":"p","H":"R","I":"S",
"J":"t","K":"u","L":"V","M":"W","Q":"a","R":"b","S":"c","T":"d", "U":"e","V":"f","W":"g","X":"h","Y":"i","Z":"J"}
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    process_file(input_file, output_file, char_mapping)

if __name__ == "__main__" :
    main()
