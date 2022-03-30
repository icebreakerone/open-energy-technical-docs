Data Set Metadata
=================

.. contents::
   :depth: 4
   :local:

Each :term:`Data Provider` (|DP|) maintains a set of one or more metadata files, each of which can describe one or more
distinct data sets. These descriptions serve several purposes:

#. They drive discovery descriptions are ingested into our search system and made available to a :term:`Data Consumer`
   searching for particular kinds of data.

#. They inform consumption of that data, providing information on:

   #. The |API| required to access the data set
   #. Any access constraints which may need to be satisfied
   #. Licenses for any accessed data
   #. Representation and internal semantics of expressions of the data

Metadata File Structure
-----------------------

.. note::

    The examples below use |YAML| format for compactness and increased readability. Data providers may present this
    information either in |YAML| or in |JSON| form.

The overall structure of the metadata file is a list of objects, each of which has the following structure:

.. code-block:: yaml

    - content:
        # Discovery information
      access:
        # Access control and licensing information
      transport:
        # |API| information
      representation:
        # Data format information

Content Block
-------------

The ``content`` key contains a block of |JSON-LD| compatible information describing the conceptual content of the dataset.
A simple example is shown below:

.. code-block:: yaml

    - content:
        "@type": "dcat:Dataset"
        "@context":
           dcat: http://www.w3.org/ns/dcat#
           dct: http://purl.org/dc/terms/
           oe: http://energydata.org.uk/oe/terms/
        dct:title: My amazing data set
        dct:description: This is a free text description of the data set
        dcat:version: 0.1.2
        dcat:versionNotes: This is a note on this particular version of the dataset
        oe:sensitivityClass: OE-SA
        oe:dataSetStableIdentifier: myData

These are the minimum properties every data set must define, they include terms from the
`Dublic Core <https://dublincore.org/>`_ (``dct``) and `Data Catalog <https://www.w3.org/TR/vocab-dcat-2/>`_ (``dcat``)
vocabularies, as well as from the Open Energy core ontology. Prefixes are defined in the |JSON-LD| ``@context`` object
as in the example above.

.. list-table:: Mandatory data content metadata fields
   :widths: 25 75
   :header-rows: 1

   * - Key
     - Value
   * - `dct:title <https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/title/>`_
     - Short title for this data set
   * - `dct:description <https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/description/>`_
     - Longer form description of this data set. This is used in combination with the title and tags when people search for data sets, so aim to include probably search words in the description.
   * - `dcat:version <https://www.w3.org/TR/vocab-dcat-3/#Property:resource_version>`_
     - Version number of the data set, this should preferably follow `semantic versioning <https://semver.org/>`_ if
       possible. Versioning of the data set should be used to indicate changes in delivery mechanism, or in
       representation, rather than for changes in the underlying data. For example, this should not be used to differentiate
       between data sets from different years, rather it should be used to indicate whether a potential data consumer
       might need to alter how it processes any returned data.
   * - `dcat:versionNotes <https://www.w3.org/TR/vocab-dcat-3/#Property:resource_version_notes>`_
     - Notes used to explain any changes to this version
   * - ``oe:sensitivityClass``
     - The :term:`data sensitivity class` of this data set. In the current Open Energy system this should always be one of
       |OE-O|, |OE-SA|, or |OE-SB|, no other classes are permitted. The value of this property also determines the
       level of |API| security imposed, with |OE-O| data sets being open data with no additional security, and the two
       shared data classes mandating |FAPI| security using the Open Energy trust services.
   * - ``oe:dataSetStableIdentifier``
     - An identifier, unique to this :term:`Data Provider`, which will not be changed, and which will be used along with
       the data provider's own ID to create a unique identifier for this data set within the Open Energy search system.

Additional metadata
###################

The information above is the minimum needed to ensure that a data set is visible in the Open Energy search system. There
are, however, other properties of a data set which may be useful to potential data consumers. Where such information can
be provided, it should be provided in as standard a form as possible - in practice this translates to making use of
existing ontologies such as DCAT and Dublin Core by preference, then shared, industry-specific, ontologies, and only
using internal or custom representation when absolutely necessary.

Of particular note, and something we would like to ultimately expose in our search interface, is information about the
geospatial and temporal ranges of entries within a data set. This is a complex subject, but one that has already been
handled by DCAT. If you need to express this kind of information, please do so according to the standards laid out
`here <https://www.w3.org/TR/vocab-dcat-2/#time-and-space>`_.

We encourage use of the ``dcat:keyword`` list for data sets. These translate to "tags" in our web interface and are useful to group data sets around specific topics.

.. code-block:: yaml

  dcat:keyword: 
    solar
    electricity
    retrofit

Access Block
------------

This section describes the kinds of licensing, expressed as sets of capabilities, and what, if any, conditions must be
satisfied before a :term:`data consumer` can acquire these data.

Each item within this section contains:

1. A statement describing a set of conditions which must be satisfied to grant access, and the set of capabilities
   granted should access be provided by this set of conditions. The exact specification for these statements can be
   found at `Access Control and Capability Grant Language`
2. A boolean property indicating whether the access conditions in [1] are sufficient (``true``), or simply indicative
   (``false``). In the former case, a :term:`data consumer` which satisfies all the conditions *will* be granted access,
   in the latter they *may* be granted access, but there may be additional requirements not fully described here
3. A pair of dates indicating the time range for which this access condition is valid. Data providers are encouraged to
   commit to access and license conditions with a reasonable timeframe to allow potential consumers to plan their own
   activities

.. code-block:: yaml

   access:
     # Access constraint to licensing predicates
     - rule: oe:verified, oe:last_update max_age_days 60 grants oe:use_any
       sufficient: true
       appliesFrom: 2021-04-22
       appliesTo: 2022-04-22
     - rule: group:some_group grants oe:use_any, oe:adapt_any
       sufficient: false
       appliesFrom: 2021-04-22
       appliesTo: 2022-04-22

Transport Block
---------------

This section describes the on the wire transport protocol, normally HTTP, but with scope to describe out-of-band
transports with an initial HTTP negotiation process. It contains at least a single ``http`` key, the value of which
must be valid `Open|API| <https://swagger.io/specification/>`_

For example:

.. code-block:: yaml

   transport:
     http:
       # This block is mandatory, and contains the Open|API| spec for the secured or open
       # HTTP endpoints (depending on data class)
       openapi: 3.0.0
       info:
         title: Sample |API|
         description: CSV format data
         version: 0.1.0
       servers:
         - url: http://data-provider-example.com
           description: Describe this particular server if needed
       paths:
         "/data":
           get:
             summary: Returns a CSV containing all the data
             description: If we had any more to describe, we'd do it here
             responses:
               '200':
                 description: CSV data stream

.. note::

   Because |API| security is defined in relation to the data sensitivity class of the data set, it is not necessary to
   define the security of any presented |API| in this section. Data sets in class |OE-O| must expose an |API| with no extra
   security measures, and those in |OE-SA| and |OE-SB| must be secured by |FAPI| using the Open Energy trust services.

Heartbeat URL
#############

Data providers **SHOULD** create a secured endpoint to act as a heartbeat - if this is specifed then the |OEGS| will
periodically call it to assertain liveness and optionally gather metrics as described in
`Heartbeat and monitoring endpoint`

A hearbeat URL can be specified as a single key ``heartbeat_url`` with the value being the fully qualified URL at which
the hearbeat response is exposed.

Representation Block
--------------------

This section describes the format of any data received by a :term:`data consumer` from this data set. Open Energy does
not mandate particular formats, so this section is guidance rather than specification.

The only required element in this section is a key ``mime`` which should contain the
`media type <https://en.wikipedia.org/wiki/Media_type>`_ of the returned data. At a bare minimum this allows a client to
load data into some kind of tooling. Depending on this value, other objects may be present.

text/csv
########

This type indicates that data is presented in CSV format. In this case, an optional key ``csvw`` may be defined, and
should contain valid |JSON-LD| following the `CSV for the Web <https://www.w3.org/TR/tabular-data-primer/>`_ guidelines:

.. code-block:: yaml

   representation:
     mime: text/csv
     csvw:
       # This is only applicable if the mime type is text/csv
       "@context": http://www.w3.org/ns/csvw
       tableSchema:
         columns:
           - titles: country
           - titles: country group
           - titles: name (en)
           - titles: name (fr)
           - titles: name (de)
           - titles: latitude
           - titles: longitude

Other types
###########

This is currently open for consultation, we would like to be able to guide data providers towards particular
representation types for particular kinds of information, and make use of any existing ontologies or standards such as
the `Common Information Model <https://en.wikipedia.org/wiki/Common_Information_Model_(electricity)>`_ where such
standards will aid interoperability between Open Energy participants and the wider community.

Full Example
------------

Putting together all the fragments from previous sections produces the following - this represents a single data set,
in the full metadata file this would be contained within a list. |YAML| form:

.. code-block:: yaml

   - content:
       "@type": "dcat:Dataset"
       "@context":
         dcat: http://www.w3.org/ns/dcat#
         dct: http://purl.org/dc/terms/
         oe: http://energydata.org.uk/oe/terms/
       dct:title: My amazing data set
       dct:description: This is a free text description of the data set
       dcat:version: 0.1.2
       dcat:versionNotes: This is a note on this particular version of the dataset
       oe:sensitivityClass: OE-SA
       oe:dataSetStableIdentifier: myData
     access:
       # Access constraint to licensing predicates
       - rule: oe:verified, oe:last_update max_age_days 60 grants oe:use_any
         sufficient: true
         appliesFrom: 2021-04-22
         appliesTo: 2022-04-22
       - rule: group:some_group grants oe:use_any, oe:adapt_any
         sufficient: false
         appliesFrom: 2021-04-22
         appliesTo: 2022-04-22
     transport:
       http:
         # This block is mandatory, and contains the Open|API| spec for the secured or open
         # HTTP endpoints (depending on data class)
         openapi: 3.0.0
         info:
           title: Sample |API|
           description: CSV format data
           version: 0.1.0
         servers:
           - url: http://data-provider-example.com
             description: Describe this particular server if needed
         paths:
           "/data":
             get:
               summary: Returns a CSV containing all the data
               description: If we had any more to describe, we'd do it here
             responses:
               '200':
                 description: CSV data stream
     representation:
       mime: text/csv
       csvw:
         # This is only applicable if the mime type is text/csv
         "@context": http://www.w3.org/ns/csvw
         tableSchema:
           columns:
             - titles: country
             - titles: country group
             - titles: name (en)
             - titles: name (fr)
             - titles: name (de)
             - titles: latitude
             - titles: longitude


Or, in |JSON| form:

.. code-block:: json

    [
      {
        "content": {
          "@type": "dcat:Dataset",
          "@context": {
            "dcat": "http://www.w3.org/ns/dcat#",
            "dct": "http://purl.org/dc/terms/",
            "oe": "http://energydata.org.uk/oe/terms/"
          },
          "dct:title": "My amazing data set",
          "dct:description": "This is a free text description of the data set",
          "dcat:version": "0.1.2",
          "dcat:versionNotes": "This is a note on this particular version of the dataset",
          "oe:sensitivityClass": "|OE-SA|",
          "oe:dataSetStableIdentifier": "myData"
        },
        "access": [
          {
            "rule": "oe:verified, oe:last_update max_age_days 60 grants oe:use_any",
            "sufficient": true,
            "appliesFrom": "2021-04-22T00:00:00.000Z",
            "appliesTo": "2022-04-22T00:00:00.000Z"
          },
          {
            "rule": "group:some_group grants oe:use_any, oe:adapt_any",
            "sufficient": false,
            "appliesFrom": "2021-04-22T00:00:00.000Z",
            "appliesTo": "2022-04-22T00:00:00.000Z"
          }
        ],
        "transport": {
          "http": {
            "openapi": "3.0.0",
            "info": {
              "title": "Sample |API|",
              "description": "CSV format data",
              "version": "0.1.0"
            },
            "servers": [
              {
                "url": "http://data-provider-example.com",
                "description": "Describe this particular server if needed"
              }
            ],
            "paths": {
              "/data": {
                "get": {
                  "summary": "Returns a CSV containing all the data",
                  "description": "If we had any more to describe, we'd do it here"
                },
                "responses": {
                  "200": {
                    "description": "CSV data stream"
                  }
                }
              }
            }
          }
        },
        "representation": {
          "mime": "text/csv",
          "csvw": {
            "@context": "http://www.w3.org/ns/csvw",
            "tableSchema": {
              "columns": [
                {
                  "titles": "country"
                },
                {
                  "titles": "country group"
                },
                {
                  "titles": "name (en)"
                },
                {
                  "titles": "name (fr)"
                },
                {
                  "titles": "name (de)"
                },
                {
                  "titles": "latitude"
                },
                {
                  "titles": "longitude"
                }
              ]
            }
          }
        }
      }
    ]