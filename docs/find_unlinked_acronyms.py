import os
import re
from typing import List, Tuple


def get_known_substitutions(sub_files: List[str]):
    """
    Retrieve substitution keys from a list of sphinx compatible substitution files
    """
    for sub_file in sub_files:
        with open(sub_file, 'r') as f:
            for line in f.readlines():
                chopped = line[4:]
                end = chopped.find('|')
                yield chopped[:end]


#: These are the acronyms defined in substitution files, the plurals one we maintain
#: manually, the other is automatically built from the glossary gdoc
KNOWN_ACRONYMS = list(get_known_substitutions(['common_substitutions.txt',
                                               'glossaries/substitutions.txt']))

#: Things that look like, but are not, acronyms. These are excluded from results
EXCLUSIONS = ['MUST', 'REQUIRED', 'SHALL', 'SHOULD', 'NOT', 'RECOMMENDED', 'MAY', 'OPTIONAL',
              'POST', 'GET', 'CLIENT', 'CONDITION', 'CAPABILITY', 'OBLIGATION', 'LHS', 'RHS']


def files_with_extension(extension='rst'):
    """
    Yields a list of all filenames ending with the specified extension (defaults to rst)
    """
    for dir_path, _, file_names in os.walk(os.path.dirname(os.path.realpath(__file__))):
        for filename in file_names:
            if filename.lower().endswith(extension.lower()):
                yield f'{dir_path}/{filename}'


def acronyms(s: str):
    """
    Returns generator over acronyms found within a string along with their positions as (str, int) tuples
    """
    for match in re.finditer(r'[^a-z0-9_|\W\s]([A-Z][0-9A-Z-]{1,})+', s):
        start, end = match.span()
        if start == 0 or s[start - 1] not in ['|', '<', '_', '/', '`']:
            if match.group() not in EXCLUSIONS:
                if (end + 1) < len(s) and s[end] == 's':
                    yield match.group() + 's', start
                else:
                    yield match.group(), start


def rewrite_line(s: str, acronyms: List[Tuple[str, int]]):
    if acronyms:
        positions = []
        for acronym, start in acronyms:
            positions.append(start)
            positions.append(start + len(acronym))
        positions = sorted(positions)
        for i, position in enumerate(positions):
            location = i + position
            s = s[:location] + '|' + s[location:]
        print(s)
    return s


#: Change this to True to enable automated file rewrites
REWRITE_FILES = False


def is_heading(s: str):
    """
    True if this line looks like the underlining for an RST heading, False otherwise
    """
    return re.match(r'^[-=_#]+$', s) is not None


# Iterate over all RST files, find acronyms that aren't already in | characters and print out the report
for file in files_with_extension(extension='rst'):
    auto_replace = {}
    lines = []
    in_code_block = False
    with open(file, 'r') as f:
        for line_number, line in enumerate(f.readlines()):
            lines.append(line)
            # Detect start of code block
            if line.startswith('.. code-block'):
                in_code_block = line_number
            # Detect end of code block
            if in_code_block and line == '' and line_number > (in_code_block + 1):
                in_code_block = False
            if not in_code_block:
                for acronym, start_position in acronyms(line):
                    if acronym in KNOWN_ACRONYMS:
                        # Candidate for auto-replace
                        if line_number not in auto_replace:
                            auto_replace[line_number] = []
                        auto_replace[line_number].append((acronym, start_position))
            if is_heading(line) and line_number > 0 and line_number - 1 in auto_replace:
                del auto_replace[line_number - 1]

    if auto_replace:
        for line_number in auto_replace:
            for acronym, start_position in auto_replace[line_number]:
                print(f'{file} - line {line_number + 1}:{start_position} : {acronym} '
                      f'{"" if acronym in KNOWN_ACRONYMS else "[unknown]"}')
    if auto_replace and REWRITE_FILES:
        with open(file, 'w') as f:
            for line_number, line in enumerate(lines):
                if line_number in auto_replace:
                    f.write(rewrite_line(line, auto_replace[line_number]))
                else:
                    f.write(line)
