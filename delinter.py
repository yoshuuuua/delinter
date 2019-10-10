import click
import os
import re
import random
from random import choice
from string import ascii_uppercase
from pathlib import Path

@click.command()
@click.option('--file', default='.', help='Location of files to delint.')

def delint(file):
    """Simple program delints python code"""
    lint_dir = os.path.join(os.getcwd(), file)

    for (dirpath, dirnames, filenames) in os.walk(lint_dir):
        for filename in filenames:
            if filename.endswith('.py'):
                contents = Path(os.path.join(dirpath, filename)).read_text()
                variables_to_replace = get_next_variables(contents)
                for to_replace in variables_to_replace:
                    var = get_replacement_variable()
                    print(var)
                    contents = contents.replace(to_replace, var)
                    print(to_replace)
                    with open(Path(os.path.join(dirpath, filename)), "r+") as f:
                        data = f.read()
                        f.seek(0)
                        f.write(contents)
                        f.truncate()
    


def get_next_variables(contents):
    variables_to_return = []
    to_replace = re.findall('([a-zA-Z_]*)\s*?=', contents)
    if to_replace:
        for group in to_replace:
            if group and group not in used_variables:
                used_variables.append(group)
                variables_to_return.append(group)
    print (variables_to_return)
    return variables_to_return


def get_replacement_variable():
    while True:
        variable = ''.join(choice(ascii_uppercase) for i in range(random.randint(4,12)))
        if variable not in used_variables:
            used_variables.append(variable)
            return variable

used_variables = ["and","except","lambda","with","as","finally","nonlocal","while","assert","false","None","yield","break","for","not","class","from","or","continue","global","pass","def","if","raise","del","import","return","elif","in","True","else","is","try","default","help"]
if __name__ == '__main__':
    delint()







