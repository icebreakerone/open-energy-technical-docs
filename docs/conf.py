# General information about the project, including links to IB1s open corporate entry
project = u'Open Energy Technical Documentation'
copyright = u'Icebreaker One Limited'
copyright_link = 'https://opencorporates.com/companies/gb/12156788'
# Change this if you like, it doesn't appear on the final site
author = u'Tom Oinn'

# If provided, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
html_use_opensearch = 'https://icebreakerone.github.io/open-energy-technical-docs'

# Configures links into the main Python language docs, if you're using any libraries in your
# project and need them to link automatically add them here. Doesn't really apply to non-code
# projects, but you might want to be able to link to our published Open Energy repositories here
intersphinx_mapping = {'python': ('https://docs.python.org/3.8', None),
                       'flask': ('https://flask.palletsprojects.com/en/1.1.x/', None),
                       'cryptography': ('https://cryptography.io/en/stable/', None),
                       'requests': ('https://docs.python-requests.org/en/master/', None)}

# Configuration for multi-version build, shouldn't need to change this.

# Whitelist pattern for tags (set to None to ignore all tags)
smv_tag_whitelist = r'^.*$'
# Whitelist pattern for branches (set to None to ignore all branches)
smv_branch_whitelist = 'main'
# Whitelist pattern for remotes (set to None to use local branches only)
smv_remote_whitelist = r'^.*$'
# Pattern for released versions - this is the refs, not the ref names! In this case
# we only allow 'released' status for tags of the form vNN.NN.NN... (any number of periods)
# This means that by default there is exactly one build, 'main', that is not released.
smv_released_pattern = r'^refs/tags/[0-9.]*$'
# Format for versioned output directories inside the build directory
smv_outputdir_format = '{ref.name}'
# Determines whether remote or local git branches/tags are preferred if their output dirs conflict
smv_prefer_remote_refs = False

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.graphviz',
    'sphinx.ext.mathjax',
    'sphinx.ext.inheritance_diagram',
    'sphinx_rtd_theme',
    'sphinx.ext.autosectionlabel',
    'sphinx_multiversion',
    'sphinx.ext.githubpages'
]

# Configure graphviz to generate PNG and set up some default colours and graph styling. We were using SVGs here, but
# it seems that pythonhosted.org isn't setting their MIME type correctly and is therefore failing to display.
graphviz_output_format = 'png'
graphviz_dark_colour = '#343131'
graphviz_background_colour = 'linen'
graphviz_dot_args = ['-Gbgcolor=transparent', '-Nshape=rectangle', '-Nfontname=courier', '-Nfontsize=12', '-Nheight=0',
                     '-Nwidth=0', '-Nfillcolor={}'.format(graphviz_background_colour),
                     '-Ncolor={}'.format(graphviz_dark_colour), '-Nstyle=filled',
                     '-Nfontcolor={}'.format(graphviz_dark_colour), '-Efontcolor={}'.format(graphviz_dark_colour),
                     '-Ecolor={}'.format(graphviz_dark_colour)]


# Use this to point to the current version, this is used to check whether a user
# is looking at the current version and show a banner if not. If this doesn't
# correspond to a released tag it'll fail silently. Well, maybe not silently. It'll
# fail though, and no banners will be shown.

def get_latest_release():
    import subprocess
    import semver
    result = subprocess.run(['git', 'tag', '-l'], stdout=subprocess.PIPE)

    def parse_tag(s):
        try:
            return semver.VersionInfo.parse(s)
        except ValueError:
            return ''

    tags = sorted([tag for tag in [parse_tag(s) for s in str(result.stdout, 'utf-8').split('\n')] if tag])
    if tags:
        latest = str(tags[-1])
        print(f'Latest tag is {latest}')
        return latest
    else:
        print('No latest tag found')
        return ''


smv_latest_version = get_latest_release()

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Static HTML, used to override style sheets in themes
html_static_path = ['_static']
html_context = {
    'css_files': [
        '_static/theme_overrides.css'
    ],
    'copyright_link': copyright_link,
}
html_favicon = 'images/favicon.png'

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# Enable warnings for missing references
nitpicky = True

# Pull in substitutions to each file as epilog
rst_epilog = """
.. include:: glossaries/substitutions.txt
"""

# Configure auto section labelling
autosectionlabel_prefix_document = False
autosectionlabel_maxdepth = 4

# Enable numbering of figures in HTML output
numfig = True


# Define skip rules to exclude some functions and other members from autodoc
def skip(app, what, name, obj, skip, options):
    if name == "__init__":
        return False
    if name == "as_dict" or name == "from_dict":
        return True
    return skip


def setup(app):
    app.connect("autodoc-skip-member", skip)


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = 'any'

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `to do` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

html_theme = "sphinx_rtd_theme"
# Use IB1 colour for search and banner background
html_theme_options = {
    'style_nav_header_background': '#0C3945',
}

html_logo = 'images/logo.png'

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
html_extra_path = ['_html_extra/.htaccess']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True


# This is the file name suffix for HTML files (e.g. ".xhtml").
html_file_suffix = '.html'

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
html_search_language = 'en'

# Monkey patch to prevent sphinx going and looking for ivar references

from docutils import nodes
from sphinx.util.docfields import TypedField
from sphinx import addnodes


def patched_make_field(self, types, domain, items, env=None):
    def handle_item(fieldarg, content):
        par = nodes.paragraph()
        par += addnodes.literal_strong('', fieldarg)  # Patch: this line added
        # par.extend(self.make_xrefs(self.rolename, domain, fieldarg,
        #                           addnodes.literal_strong))
        if fieldarg in types:
            par += nodes.Text(' (')
            # NOTE: using .pop() here to prevent a single type node to be
            # inserted twice into the doctree, which leads to
            # inconsistencies later when references are resolved
            fieldtype = types.pop(fieldarg)
            if len(fieldtype) == 1 and isinstance(fieldtype[0], nodes.Text):
                typename = u''.join(n.astext() for n in fieldtype)
                par.extend(self.make_xrefs(self.typerolename, domain, typename,
                                           addnodes.literal_emphasis))
            else:
                par += fieldtype
            par += nodes.Text(')')
        par += nodes.Text(' -- ')
        par += content
        return par

    fieldname = nodes.field_name('', self.label)
    if len(items) == 1 and self.can_collapse:
        fieldarg, content = items[0]
        bodynode = handle_item(fieldarg, content)
    else:
        bodynode = self.list_type()
        for fieldarg, content in items:
            bodynode += nodes.list_item('', handle_item(fieldarg, content))
    fieldbody = nodes.field_body('', bodynode)
    return nodes.field('', fieldname, fieldbody)


TypedField.make_field = patched_make_field
