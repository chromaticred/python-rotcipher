import argparse
import os

parser = argparse.ArgumentParser(description='Reads in your arguments')
parser.add_argument('-i', '-input', type=str,
                    help='Read in a file or string to be encoded/decoded. Must pass -e or -d to determine how to output the file.')
parser.add_argument('-o', '-output', type=str, help='Export text file from program.')
parser.add_argument('-r', '-rotation', type=str, help='Set rotation.')
parser.add_argument('-e', '-encode', action='store_true', help='Encode the file and save as output.')
parser.add_argument('-d', '-decode', action='store_true', help='Decode the file and save as output.')
args = parser.parse_args()

# Encryption/decryption thoroughly tested via rot13.com
def cipher_args():
    keylist = {}
    rotation = int(args.r)
    input_text = ""
    output_text = ""
    letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                   'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    rotated_list = letter_list[rotation:] + letter_list[:rotation]
    if args.i != None and os.path.isfile(args.i):
        print("Processing input file: " + args.i)
        file = open(args.i, "r")
        input_text = file.read()
        file.close()
    if args.e:
        for i in range(26):
            keylist[letter_list[i]] = rotated_list[i]
        for i in range(26):
            keylist[letter_list[i].upper()] = rotated_list[i].upper()
    elif args.d:
        for i in range(26):
            keylist[rotated_list[i]] = letter_list[i]
        for i in range(26):
            keylist[rotated_list[i].upper()] = letter_list[i].upper()

    for letter in input_text:
        output_text += keylist[letter] if letter in keylist else letter

    if args.o != None:
        print("Processing output file: " + args.o)
        file = open(args.o, "w")
        file.write(output_text)
        file.close()

    # If no output given, write to example_output.txt in current location.
    else:
        print("Processing default output file (default_output.txt) at current location.")
        file = open('default_output.txt', "w")
        file.write(output_text)
        file.close()

    # Print Debugging
    #print(input_text)
    #print(output_text)


cipher_args()
