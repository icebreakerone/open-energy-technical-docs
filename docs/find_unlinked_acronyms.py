import os
import re
from typing import List


def files_with_extension(extension='rst'):
    """
    Yields a list of all filenames ending with the specified extension (defaults to rst)

    :return:
        A generator over file paths
    """
    for dirpath, dirnames, filenames in os.walk(os.path.dirname(os.path.realpath(__file__))):
        for file in filenames:
            if file.lower().endswith(extension.lower()):
                yield f'{dirpath}/{file}'


def get_known_substitutions(sub_files: List[str]):
    for sub_file in sub_files:
        with open(sub_file, 'r') as f:
            for line in f.readlines():
                chopped = line[4:]
                end = chopped.find('|')
                yield chopped[:end]


KNOWN_ACRONYMS = list(get_known_substitutions(['common_substitutions.txt',
                                               'glossaries/substitutions.txt']))


def acronyms(s: str, known_acronyms: List[str]):
    """
    Returns all acronyms, multiple
    :param s:
    :return:
    """
    for match in re.finditer(r'[^a-z0-9_|\W\s]([A-Z][0-9A-Z-]{1,})+', s):
        start, end = match.span()
        if start == 0 or s[start - 1] not in ['|', '<', '_']:
            if match.group() not in ['MUST', 'REQUIRED', 'SHALL', 'SHOULD', 'NOT',
                                     'RECOMMENDED', 'MAY', 'OPTIONAL', 'POST', 'GET', 'CLIENT', 'CONDITION',
                                     'CAPABILITY', 'OBLIGATION', 'LHS', 'RHS']:
                if (end + 1) < len(s) and s[end] == 's':
                    yield match.group() + 's', start
                else:
                    yield match.group(), start


for file in files_with_extension(extension='rst'):
    with open(file, 'r') as f:
        for line_number, line in enumerate(f.readlines()):
            for acronym, start_position in acronyms(line, []):
                print(f'{file} - line {line_number + 1}:{start_position} : {acronym} {"" if acronym in KNOWN_ACRONYMS else "[unknown]"}')
