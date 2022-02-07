# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = ../build
PYTHON        = python3

# User-friendly check for sphinx-build
ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
$(error The '$(SPHINXBUILD)' command was not found. Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to point to the full path of the '$(SPHINXBUILD)' executable. Alternatively you can add the directory with the executable to your PATH. If you don't have Sphinx installed, grab it from http://sphinx-doc.org/)
endif

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help clean html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf text man changes linkcheck doctest coverage gettext

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  local      to make standalone HTML files, including local changes"
	@echo "  html       to make standalone HTML files, ignoring local changes"
	@echo "  pdf        to make standalone PDF files, ignoring local changes"
	@echo "  ghpages    to make HTML files and push to github pages - requires additional setup!"
	@echo "  clean      to clean the build directory"

clean:
	rm -rf $(BUILDDIR)/*

html:
	git tag -l | xargs git tag -d
	git fetch --tags
	sphinx-multiversion . $(BUILDDIR)/html
	touch $(BUILDDIR)/html/.nojekyll
	$(PYTHON) build_index_redirect.py -b $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

local:
	$(SPHINXBUILD) -E -b html $(ALLSPHINXOPTS) -D todo_include_todos=True $(BUILDDIR)/localhtml
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/localhtml."

ghpages:
	# This requires setup! Don't run it unless you know it'll work.
	git tag -l | xargs git tag -d
	git fetch --tags
	sphinx-multiversion . ../../open-energy-technical-docs-pages/html
	touch ../../open-energy-technical-docs-pages/html/.nojekyll
	$(PYTHON) build_index_redirect.py -b ../../open-energy-technical-docs-pages/html
	cd ../../open-energy-technical-docs-pages/html; git add . ; git commit -m "rebuilt docs"; git push origin gh-pages
	@echo
	@echo "Pushed docs to https://icebreakerone.github.io/open-energy-technical-docs/index.html"

pdf:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo "Running LaTeX files through pdflatex..."
	$(MAKE) -C $(BUILDDIR)/latex all-pdf
	mv $(BUILDDIR)/latex/openenergytechnical.pdf $(BUILDDIR)/
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)."

