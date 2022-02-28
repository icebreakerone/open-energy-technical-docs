# Open Energy Technical Docs
Open Energy technical documentation. This repository contains the sources for a sphinx-based build of our
technical documentation, including operational guidelines, for the Open Energy project.

## Viewing the docs

This documentation is rendered at https://icebreakerone.github.io/open-energy-technical-docs/, which is
linked to automatically from https://docs.openenergy.org.uk 

## MacOS Homebrew installation
```
> brew install sphinx cairo
```
Then continue to Sphinx installation...

## Sphinx installation

Using whichever version of Python 3 makes you happiest, and install sphinx and the necessary extra plugins for
themes and other tooling:

```
> pip install -r requirements.txt
```

## MacOS LaTeX installation - required for PDF output
1. Download and install XCode command line tools from: https://developer.apple.com/download/all/ (requires Apple ID login)
2. Download and install BasicTeX from MacTeX: https://tug.org/mactex/morepackages.html
3. Add `/Library/TeX/textbin` to your path
```
> export PATH=$PATH:/Library/TeX/texbin
```
4. Update the TeX Live Manager
```
> sudo tlmgr update --self
```
5. Install the additional packages required by Sphinx
Current for sphinx-build v4.4.0 and TeX Live 2021 - this may change over time
```
> sudo tlmgr install `cat tlmgr_packages.txt`
```

Users of other Linux systems may use the above as the basis for installation using their relevant package manager.

## Building the docs

Run these commands from within the `docs` folder:

1. `make local` to build doc website locally. This will use the current checked out version, including
   any local changes, and build the website in `../build/localhtml`. Use this when you have just made a change
   and want to see whether it did the right thing before pushing to version control.
2. `make html` to build the doc website locally, but does not incorporate local changes. Instead, this pulls
   release and head versions from version control and builds the entire site, as it would appear on the final
   public location, and including all versions.
3. `make pdf` to build all docs to a single PDF file which can then be found in `../build/openenergytechnical.pdf`
4. `make ghpages` to build in the same way as `make html` but also push a new version to the public site. This
   requires setup, specifically it expects a parallel checkout of the docs repository with the `ghpages` branch
   called `open-energy-technical-docs-pages`. This can be created as follows:
   
   ```shell
   cd ../..
   mkdir open-energy-technical-docs-pages
   cd open-energy-technical-docs-pages
   git clone git@github.com:icebreakerone/open-energy-technical-docs --branch gh-pages html 
   ```
   
   Once this is set up, `make ghpages` should work, and will push a new build to the public website

## Releasing a version of the docs

Our public doc website handles multiple versions. There is always a version `main` corresponding to the latest
state of that same named branch in version control. In addition, release builds are indicated with tags within
the repository of the form `a.b.c`, where `a` is the major version number, `b` the minor, and `c` the patch. This
is a scheme known as semantic versioning, and in general we should increment the patch number to indicate minor
tweaks, spelling and layout corrections, leaving the minor and major numbers to indicate substantive changes
to the contents. Minor numbers should be incremented for additive changes which won't break anything, and any
substantial changes of the kind that would require a *read from the start again* approach should be indicated
with major version number increments. The release build at the end of phase 3 is version `1.0.0`.

To perform a release, create and push a tag with the corresponding release number. Alternatively, use the release
mechanism within github, naming the release in the same fashion. https://github.com/icebreakerone/open-energy-technical-docs/releases
shows the current releases, and allows you to create new ones.

Part of the build is to produce a redirect such that e.g. https://docs.openenergy.org.uk redirects to the latest
release build. Release builds are ones with the `a.b.c` naming convention described above, but it is perfectly
possible to have non-release builds simply by using any other tag format. These will be listed in the versions
panel in the generated site but will not automatically be linked from the base address.

## Updating the glossaries

The python script `build_glossary.py` will retrieve the glossary from our gdrive and rebuild it from scratch, this
will result in changes which will need to be committed to version control before they can be made visible on the
public site.

This will also create the substitution rules which allow e.g. `|DC|` to expand to `Data Consumer` with links -
at present any two letter acronyms will be expanded and linked to the full name, whereas acronyms longer than
this will be linked to the glossary entry but not expanded.

## Finding and re-writing acronyms

The python script `find_unlinked_acronyms` will traverse all `.rst` files and hunt for anything that looks like
an acronym, excluding those which are part of titles. It will find any that are not already marked as substitutions
and, optionally (depending on whether the `REWRITE_FILES` property in the script is True or False) rewrite any
such cases. If there are acronym-like things that do not correspond to substitutions in the glossary it will
complain about them. Run this periodically to check that you've not introduced acronyms and not referenced them
out to the glossary, we should aim for having no acronyms that are not properly referenced.