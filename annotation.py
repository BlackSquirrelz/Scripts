#!/bin/python3

# How to use:
# Open Terminal, type python3 -m pip install -r requirements.txt
# python3 annotation.py <GERMAN_SENTENCES>.txt
# If you want to use an English model you will first need to download it from spacy.
# Model Source: https://spacy.io/usage/linguistic-features
# read the POS, and DEP results.

import spacy
from sys import argv

model = 'de_core_news_sm'

nlp = spacy.load(model)

exercise_file = argv[1]

with open(exercise_file, 'r') as document:
    sentences = [sentence for sentence in document]

for sentence in sentences:
    print(f"\nOriginal: {sentence}\n")
    print("-" * 50)
    print()
    doc = nlp(sentence)
    print(f"Token \t POS \t DEP\n")
    for token in doc:
        print(f"{token.text} \t {token.pos_} \t {token.dep_}")
    print()
    print("="*50)



