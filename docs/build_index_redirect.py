"""
Builds a top level index.html file that redirects immediately to the most interesting looking version. Orders
by semantic version, defaulting to 'main' if there aren't any semantic-version-like directories available.

Run automatically if you use 'make html' or 'make ghpages'
"""
import os
from argparse import ArgumentParser
import semver

# Get build root, look for subdirectories within it
parser = ArgumentParser()
parser.add_argument('-b', '--build', type=str, help=f'HTML build root')
options = parser.parse_args()
folders = [f.name for f in os.scandir(options.build) if f.is_dir()]


# Look for semantic version names within this and find the latest one, or
# default to 'main' if none available
def best_version():
    def parse(f):
        try:
            return semver.VersionInfo.parse(f)
        except ValueError:
            return ''

    semantic_versions = sorted([item for item in [parse(f) for f in folders] if item])

    if semantic_versions:
        # Return the highest semantic version if available
        return str(semantic_versions[-1])
    # If not, fall back to main
    return 'main'


# Write out a tiny fragment of HTML to redirect to the current best version
with open(f'{options.build}/index.html', 'w') as f:
    f.write(f'<html><head>'
            f'<meta http-equiv="refresh" content="0; URL={best_version()}/index.html" />'
            f'<meta http-equiv="Cache-Control" content="no-store" />'
            f'</head></html>')
