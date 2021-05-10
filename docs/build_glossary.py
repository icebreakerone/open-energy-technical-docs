# Builds a glossary.rst and substitutions.txt file from our glossary in google drive. Run this to produce the files
# used by sphinx before doing a full documentation build
import csv
import re
from argparse import ArgumentParser
from dataclasses import dataclass
from typing import List, Dict
from urllib.parse import urlparse

import requests

# Default document ID, points to the v0.2 OE3 Acronyms and terms sheet from our google drive.
GLOSSARY_ID = '1bFH57PWT6da4cqJyWn9JWIcEjGqrAupjjj3Ib9-66_c'


@dataclass(frozen=True)
class GlossaryEntry:
    """
    Holds information from a single row of the glossary CSV table
    """
    acronym: str
    expansion: str
    domain: str
    notes: str
    extra: str


def parse_glossary_sheet(sheet_id=GLOSSARY_ID, gid=0):
    """
    Get the CSV from the specified file, parsing it out into a list of `GlossaryEntry` objects

    :param sheet_id:
        ID of the google sheet to export
    :param gid:
        ID of the page within that sheet
    :return:
        List of GlossaryEntry corresponding to rows in the CSV
    """

    url = f'https://docs.google.com/spreadsheets/export?format=csv&id={sheet_id}&gid={gid}'

    reader = csv.reader(requests.get(url).content.decode('utf-8').splitlines(), delimiter=',')

    # Skip header row
    reader.__next__()

    def rewrite_urls(s):
        """
        Attempts to find URLs and rewrite them into a compact RST form showing the netloc and final
        element of the path (but linking back to the full URL)
        """

        def rewrite(m):
            if u := m.group(0):
                o = urlparse(u)
                return f'`{o.netloc}: {o.path.split("/")[-1:][0]} <{u}>`_'
            return ''

        return re.sub(pattern='http(s?):.*\\w',
                      repl=rewrite,
                      string=s)

    def pad_row(row):
        """
        Pads the row to 5 cells so we have the correct number of arguments for the GlossaryEntry init method, fills
        in any empty descriptions (with 'no definition') or missing expanded names (with the first acronym). Strips
        all leading and trailing whitespace in cells before calling the rewrite_urls function on each in turn.
        """
        row = [rewrite_urls(s.strip()) for s in row]
        if not row[1]:
            row[1] = row[0].split(',')[0]
        if not row[3]:
            row[3] = 'no definition'
        row[3] = f'*{row[0]}* - {row[3]}'.strip()
        if len(row) == 4:
            return row + ['']
        else:
            return row[:5]

    # Apply the pad_row function to each row, building a list of GlossaryEntry objects sorted by
    # acronym, case insensitive, from a-z
    return sorted([GlossaryEntry(*pad_row(row)) for row in reader], key=lambda g: g.acronym.lower())


def glossaries_by_domain(entries: List[GlossaryEntry]) -> Dict[str, str]:
    known_domains = set([entry.domain for entry in entries])
    return {domain: glossary(entries=entries, domain=domain) for domain in known_domains}


def master_glossary(entries: List[GlossaryEntry], prefix='glossaries/') -> str:
    known_domains = sorted(set([entry.domain for entry in entries]))
    g = ''
    for domain in known_domains:
        g += f'{domain}\n'
        g += '-' * len(domain) + '\n\n'
        g += f'.. include:: {prefix}{domain}_glossary.txt\n\n'
    return g


def substitutions(entries: List[GlossaryEntry]) -> str:
    """
    Build a string containing acronym substitions. This can then be added to the epilogue of every page to make
    substitions work from acronyms to their respective terms.
    :param entries:
        A list of GlossaryEntry objects
    :return:
        String containing RST substitution rules
    """
    s = ''
    for entry in entries:
        for acronym in entry.acronym.split(','):
            s += f'.. |{acronym}| replace:: :term:`{acronym}<{entry.expansion}>`\n'
    return s


def glossary(entries: List[GlossaryEntry], indent=' ' * 4, domain=None) -> str:
    """
    Build a string containing a valid glossary in RST form.

    :param List[GlossaryEntry] entries:
        Entries to use when building the glossary strings
    :param str indent:
        Indentation used by the RST file, defaults to four spaces
    :param domain:
        If specified, restrict glossary entries to only the specific domain
    :return:
        Pair of RST, substitutions strings
    """
    g = '.. glossary::\n\n'

    for entry in entries:
        if domain is None or entry.domain.lower() == domain.lower():
            g += indent + entry.expansion + '\n'
            g += indent * 2 + entry.notes + '\n'
            if entry.extra:
                g += indent * 2 + entry.extra + '\n'
            g += '\n'

    return g


def build_glossary_files():
    """
    Write out generated_glossary.txt containing the RST to be inlined into an actual glossary file, as well as
    substitutions.txt containing substitution directives which can then be used to reference acronyms directly.
    """
    entries = parse_glossary_sheet()

    s = substitutions(entries)
    g = glossaries_by_domain(entries)
    for domain in g:
        with open(f'glossaries/{domain}_glossary.txt', 'w') as f:
            f.write(g[domain])
    with open('glossaries/substitutions.txt', 'w') as f:
        f.write(s)
    with open('all_glossaries.txt', 'w') as f:
        f.write(master_glossary(entries))


parser = ArgumentParser()

parser.add_argument('-i', '--sheet', type=str, help=f'ID of google sheet to use',
                    default='1bFH57PWT6da4cqJyWn9JWIcEjGqrAupjjj3Ib9-66_c')
parser.add_argument('-g', '--gid', type=str, help='GID of page in google sheet', default='0')
parser.add_argument('-o', '--output-dir', type=str, help='Output directory', default='./glossaries')

build_glossary_files()
