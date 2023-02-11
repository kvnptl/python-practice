
'''

JSON file content:

{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": true,
            "args": ["--name", "David", "--age", "10"],
            "purpose": ["debug-in-terminal"]
        }
    ]
}

'''


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