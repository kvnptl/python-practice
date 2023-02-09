
# take argument from terminal using argparse
import argparse

print("Hello, World!")

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="your name")
parser.add_argument("--age", help="your age")
args = parser.parse_args()

print("Hello, " + args.name + "!")
print("You are " + args.age + " years old.")

# run this file in terminal with:
# python test_argument_with_vscode_debug.py --name "John" --age 30