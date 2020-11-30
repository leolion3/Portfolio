# Monoalphabetic Decypherer

Authored By: Leonard Haddad

## License

Access is hereby granted in accords with the MIT License. You may modify and change the provided script files however you like. Any damage caused however, will be your own problem.

## Usage

The provided decypherer has a wide variety of options.

- To get started, enter the cyphered text (without newline breaks, as these will be read in as commands - python input standards)

After doing so you can enter a custom alphabet and decide whether all the text should be in lowercase or not.

### Provided Tools

As mentioned above, the decypherer has a wide variety of options:

- Normal Letter Decypher Mode - Replaces a single manually provided letter with another single manually provided letter
- Brute-Force/Round-Robin Letter Mode - Replaces a single manually provided letter with every letter of the alphabet
- Word-Match Mode (random/specific) - Attemps to replace an entire word with a provided word, replacing all letters in the text with the ones of the provided word. The word that gets replaced is either random or specific based on your decision.
- Letter-Count - Displays letter counts + percentages
- Json-Serialise - Allows export of found matchings to a Json file
- Json-Deserialise - Allows import of matches from a Json file

Usage of these options is explained in the script. To view all available commands, type --help
