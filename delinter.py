import click
import os
import re
import random
import shutil
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
                file_path = Path(os.path.join(dirpath, filename))
                contents = file_path.read_text()
                variables_to_replace = get_next_variables(contents)
                for to_replace in variables_to_replace:
                    var = get_replacement_variable()
                    contents = contents.replace(to_replace, var)
                    with open(file_path, "r+") as f:
                        data = f.read()
                        f.seek(0)
                        f.write(contents)
                        f.truncate()
                add_afterline_effects(file_path)

    


def get_next_variables(contents):
    variables_to_return = []
    to_replace = re.findall('([a-zA-Z_]*)\s*?=', contents)
    if to_replace:
        for group in to_replace:
            if group and group not in used_variables:
                used_variables.append(group)
                variables_to_return.append(group)
    return variables_to_return

def get_replacement_variable():
    while True:
        variable = ''.join(choice(ascii_uppercase) for i in range(random.randint(4,12)))
        if variable not in used_variables:
            used_variables.append(variable)
            return variable

def add_afterline_effects(file_path):
    with open(file_path) as old, open('new_file', 'w') as new:
        for line in old:
            new.write(line + ''.join(['\n' for _ in range(random.randint(0,4))]))
    shutil.move('new_file', file_path)

used_variables = ["__name__","and","except","lambda","with","as","finally","nonlocal","while","assert","false","None","yield","break","for","not","class","from","or","continue","global","pass","def","if","raise","del","import","return","elif","in","True","else","is","try","default","help"]
if __name__ == '__main__':
    delint()