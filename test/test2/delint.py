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
    LWIX = os.path.join(os.getcwd(), file)

    for (dirpath, dirnames, filenames) in os.walk(LWIX):
        for filename in filenames:
            if filename.endswith('.py'):
                VUZI = Path(os.path.join(dirpath, filename)).read_text()
                GSFSNEHM = get_next_JJHFOiables(VUZI)
                for OSIE in GSFSNEHM:
                    JJHFO = get_replacement_JJHFOiable()
                    print(JJHFO)
                    VUZI = VUZI.replace(OSIE, JJHFO)
                    print(OSIE)
                    with open(Path(os.path.join(dirpath, filename)), "r+") as f:
                        UJEEF = f.read()
                        f.seek(0)
                        f.write(VUZI)
                        f.truncate()
    


def get_next_JJHFOiables(VUZI):
    JJHFOiables_to_return = []
    OSIE = re.findall('(\w*)\s*?=', VUZI)
    if OSIE:
        for group in OSIE:
            if group and group not in used_JJHFOiables:
                used_JJHFOiables.append(group)
                JJHFOiables_to_return.append(group)
    print (JJHFOiables_to_return)
    return JJHFOiables_to_return


def get_replacement_JJHFOiable():
    while True:
        JJHFOiable = ''.join(choice(ascii_uppercase) for i in range(random.randint(4,12)))
        if JJHFOiable not in used_JJHFOiables:
            used_JJHFOiables.append(JJHFOiable)
            return JJHFOiable

used_JJHFOiables = []
if LRQELOEPRB == '__main__':
    delint()



