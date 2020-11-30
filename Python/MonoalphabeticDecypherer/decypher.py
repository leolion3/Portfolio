""" 
==================== LICENSE ====================
 Made By: Leonard Haddad
 
 Permission is hereby granted, in accords to the MIT
 license. You may modify and use this file however
 you like. Any damages done will be your own problem, 
 not mine.

==================== LICENSE ==================== 
"""
from os import system, name
import json

# Cypher text
cypher = []


# Matchings of letters to cypher letters
matchings = []


# Alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"


# All Lowercase
lowercase = True

# All uppercase
uppercase = False


# Clears the screen
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# Help
def help():
    clear()
    print("==================== Monoalphabetic Decypherer ====================")
    print("\n-h --help                              - display this screen")
    print("-d --decypher                           - replace single letter")
    print("-db --decypher-brute                    - brute force letter replacement")
    print("-wm --word-match                        - replace whole word")
    print("-cm --clear-matches                     - clear letter matchings")
    print("-lc --letter-count                      - display letter counts and percentage")
    print("-p --print                              - print decyphered text")
    print("-dm --display-matchings                 - display current matchings")
    print("-s --save                               - save json export")
    print("-l --load                               - load matchings from json")
    print("--exit                                  - exit")
    print("\n===================================================================\n")
    main_loop()


# Replace already picked letters
def get_decypehred_text():
    global cypher, matchings
    indexes_changed = []
    i = 0
    cypher_letters = list(cypher)
    while i<len(cypher_letters):
        for (c,w) in matchings:
            if cypher_letters[i] == c:
                cypher_letters[i] = w
                indexes_changed.append(i)
                break
        i+=1
    return ((cypher_letters,indexes_changed))


# Start decyphering
def decypher():
    global cypher, matchings
    cyphered_letter = input("Letter to replace: ")
    replace_with = input("Replace with: ")
    new_text, indexes = get_decypehred_text()
    i = 0
    while i<len(new_text):
        if new_text[i] == cyphered_letter:
            contained_in_indexes = False
            for a in indexes:
                if a == i:
                    contained_in_indexes = True
                    break
            if not contained_in_indexes:
                new_text[i] = replace_with
        i+=1
    clear()
    print("".join(new_text))
    ok = input("\n\nReplacing: " + cyphered_letter + " | with: " + replace_with + "\nKeep changes? y/n: ")
    if 'y' in ok:
        matchings.append((cyphered_letter,replace_with))
    main_loop()


# Brute force letter replacement
def brute_force():
    global cypher, matchings, alphabet
    clear()
    cyphered_letter = input("Letter to replace: ")
    i = 0
    while i < len(alphabet):
        clear()
        new_text, indexes = get_decypehred_text()
        j = 0
        for o in new_text:
            if o == cyphered_letter:
                contained_in_indexes = False
                for a in indexes:
                    if a == j:
                        contained_in_indexes = True
                        break
                if not contained_in_indexes:
                    already_decyphered = False
                    for (c,w) in matchings:
                        if w == o:
                            already_decyphered = True
                    if not already_decyphered:
                        new_text[j] = alphabet[i]
            j+=1
        clear()
        print("".join(new_text))
        ok = input("\n\nReplacing: " + cyphered_letter + " | with: " + alphabet[i] + "\nKeep changes? y/n: ")
        if 'y' in ok:
            matchings.append((cyphered_letter,alphabet[i]))
            break
        i+=1
    main_loop()
    
    
# Replace entire words, randomly or specifically
def word_match():
    global cypher, matchings
    clear()
    match_type = input("Would you like to match specific words or random (based on word length)?\nr/s: ")
    replacement_word = input("Word to replace with: ")
    cypher_words = cypher.split()
    if 'r' in match_type:
        i = 0
        while i<len(cypher_words):
            replacement_letters = []
            if len(cypher_words[i]) == len(replacement_word):
                cypher_letters = list(cypher_words[i])
                replacement_word_letters = list(replacement_word)
                j=0
                while j<len(replacement_word):
                    replacement_letters.append((cypher_letters[j],replacement_word_letters[j]))
                    j+=1
                new_text, indexes = get_decypehred_text()
                j=0
                while j<len(new_text):
                    for (c,w) in replacement_letters:
                        if new_text[j] == c:
                            contained_in_indexes = False
                            for a in indexes:
                                if a == j:
                                    contained_in_indexes = True
                                    break
                            if not contained_in_indexes:
                                new_text[j] = w
                                break
                    j+=1
                clear()
                print("".join(new_text))
                ok = input("\n\nReplacing: " + cypher_words[i] + " | with: " + replacement_word + "\nKeep changes? y/n: ")
                if 'y' in ok:
                    for o in replacement_letters:
                        matchings.append(o)
                    break
            i+=1
    elif 's' in match_type:
        to_be_replaced = input("Word to replace: ")
        to_be_replaced_letters = list(to_be_replaced)
        replace_with_letters = list(replacement_word)
        replacement_letters = []
        i=0
        while i<len(to_be_replaced_letters):
            replacement_letters.append((to_be_replaced_letters[i],replace_with_letters[i]))
            i+=1
        new_text, indexes = get_decypehred_text()
        clear()
        j=0
        while j<len(new_text):
            for (c,w) in replacement_letters:
                if new_text[j] == c:
                    contained_in_indexes = False
                    for a in indexes:
                        if a == j:
                            contained_in_indexes = True
                            break
                    if not contained_in_indexes:
                            new_text[j] = w
                            break
            j+=1
        clear()
        print("".join(new_text))
        ok = input("\n\nKeep changes? y/n: ")
        if 'y' in ok:
            for o in replacement_letters:
                matchings.append(o)
    main_loop()


# Shows letter counts and percentages
def letter_count():
    global cypher
    cypher_letters = list(cypher)
    letters = []
    letter_frequencies = []
    for a in cypher_letters:
        contained = False
        for b in letters:
            if a == b:
                contained = True
        if not contained and not a == " ":
            letters.append(a)
    for a in letters:
        count = 0
        for b in cypher_letters:
            if a == b:
                count+=1
        letter_frequencies.append((a,count))
    clear()
    print("Letter frequencies:\n")
    cypher_letters = "".join(cypher_letters)
    cypher_letters.replace(' ','')
    cypher_letters = list(cypher_letters)
    for (a,c) in letter_frequencies:
        print(a +": " + str(c) + " | percentage: " + str((c/len(cypher_letters)) * 100) + "%")
    main_loop()


# Print decyphered text
def print_decyphered():
    clear()
    decyphered_text, indexes = get_decypehred_text()
    print("".join(decyphered_text))
    main_loop()
    
    
# Json serialise the matchings list
def serialise_json():
    global matchings
    clear()
    file_name = input("Enter filename to export to: ")
    JSON_string = json.dumps(matchings)
    with open(file_name,'wb+') as f:
        f.write(bytes(JSON_string,'utf-8'))
        f.close()
    print("Exported file!")
    main_loop()
    
    
# Deserialise json from file
def deserialise_json():
    global matchings
    clear()
    file_name = input("Enter file name: ")
    JSON_string = []
    with open(file_name,'rb') as f:
        JSON_string = f.read().decode()
        f.close()
    matchings = json.loads(JSON_string)
    main_loop()


# Main loop
def main_loop():
    global matchings
    next_command = input("\n#>")
    if ('-h' or '--help') in next_command:
        help()
    elif ('-dm' or '--display-matchings') in next_command:
        clear()
        print("Current matchings:\n")
        for (c,w) in matchings:
            print("Cypher character: " + c + " | Decyphered Character: " + w)
        main_loop()
    elif ('-db' or '--decypher-brute') in next_command:
        brute_force()
    elif ('-d' or '--decypher') in next_command:
        decypher()
    elif ('-wm' or '--word-match') in next_command:
        word_match()
    elif ('-cm' or '--clear-matching') in next_command:
        mode = input("Clear sinlge matching/all? s/a: ")
        if 'a' in mode:
            matchings = []
            print("Cleared matchings!")
        elif 's' in mode:
            remove_me = input("Cypher letter whichs matching to remove: ")
            i = 0
            while i<len(matchings):
                (c,w) = matchings[i]
                if c == remove_me:
                    matchings.remove(matchings[i])
                    print("Removed matching for letter " + remove_me)
                    break
                i+=1
        main_loop()
    elif ('-lc' or '--letter-count') in next_command:
        letter_count()
    elif ('-p' or '--print') in next_command:
        print_decyphered()
    elif ('-s' or '--save') in next_command:
        serialise_json()
    elif ('-l' or '--load') in next_command:
        deserialise_json()
    elif '--exit' in next_command:
        exit()
    else:
        print("Incorrect command entered!")
        main_loop()
    
    
# Setup
def setup():
    global cypher, alphabet, lowercase, uppercase
    cypher = input("Enter cypher text: \n")
    if not len(cypher):
        return
    lc = input("\nAll lowercase? y/n: ")
    if not 'y' in lc:
        lowercase = False
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        uc = input("All uppercase? y/n: ")
        if not 'n' in uc:
            alphabet += "abcdefghijklmnopqrstuvwxyz"
    else:
        ca = input("\nCustom Alphabet? y/n: ")
        if 'y' in ca:
            alphabet = input("Custom alphabet: ")
            if not len(alphabet):
                return
        cypher = cypher.lower()
    clear()
    print("\n==================== Monoalphabetic Decypherer ====================")
    print("\nTo see a list of available commands, type -h or --help")
    print("To start decyphering, type -d or --decypher")
    print("\n===================================================================")
    main_loop()


setup()