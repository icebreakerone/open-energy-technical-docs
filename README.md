# oe-technical-docs
Open Energy technical docs

## Sphinx installation

Using whichever version of Python makes you happiest:

```
> pip install sphinx sphinx-rtd-theme
```

TODO - we probably want our own in-house sphinx theme here, but that's not something that currently exists so 
defaulting to the RTD theme for now.

## Building the docs

1. `make html` to build doc website locally
2. `make singlehtml` to build all docs into a single HTML file
3. `make pdf` to build all docs to a single PDF file

TODO - most of my builds have a `make push` to deploy the site when it's built, we probably want something similar
here at some point.