Considerations Before You Start
===============================

.. note::

    This section is designed primarily as a summary tool and should **not** be used in place of more
    detailed operational and technical documentation elsewhere in this site.

Introduction (Before you start)
###############################

This section provides ‘at a glance’ lists of items that new members will need to consider in order to meet
operational requirements. It may also be useful for existing members to revisit when they publish (|DPs|) or access
(|DCs|) a new dataset.

As |OE| evolves, this section will be updated to form a definitive checklist for compliance. At present however,
it is designed to outline general considerations regarding skills, capabilities and tasks that organisations will
require in order to take part in the |OE| ecosystem.

The tables below outline considerations for |DPs| and |DCs|. Each item includes a suggestion of its relevance
to different areas of readiness: commercial, operational, technical, and legal. It is suggested that prospective
members proactively engage teams or staff members with responsibilities for the above four areas of readiness
prior to joining Open Energy as members. Please note that this section is designed to support members to
prepare for data sharing. However, sharing of real data will not commence until the |OEGS| goes fully live.

Considerations for Data Providers
#################################

.. list-table::
    :header-rows: 1
    :widths: 20 60 20

    * - Consideration
      - Includes
      - Readiness area(s)
    * - Membership contract and fees
      - * Contract review by legal counsel
        * Contract signature by person with appropriate authority
        * Membership fees paid
      - Legal, commercial
    * - Onboarding to the Directory
      - * Generic contact email addresses and organisation details provided to Open Energy for publishing in the Directory
        * Software statement created (`instructions <https://docs.google.com/document/d/1sypYWTeLFSFyfO_zTW6xKCWnao9gKjAo2JHZZIPs2xI/edit?usp=sharing>`_)
        * Transport certificate created (`instructions <https://docs.google.com/document/d/1sypYWTeLFSFyfO_zTW6xKCWnao9gKjAo2JHZZIPs2xI/edit?usp=sharing>`_)
      - Operational, technical
    * - Metadata file creation
      - Applies to **all** datasets, both :term:`Open Data` and :term:`Shared Data`:

        * `Metadata` file created for each dataset
        * Metadata file published and available on a public web server (such as `public GitHub repo <https://github.com/icebreakerone/open-energy-metadata-demo/tree/main/metadata_files>`_)
        * Records of the metadata file location created (`instructions <https://docs.google.com/document/d/1sypYWTeLFSFyfO_zTW6xKCWnao9gKjAo2JHZZIPs2xI/edit?usp=sharing>`_)
        * Verification that Open Energy automated processes have picked up the file and surfaced contents in `Search <https://openenergy.org.uk>`_
      - Technical
    * - Secure |API| creation and deployment compliant with |OE| subset of |FAPI| specification
      - For example, using one of the following methods:

        1. Deploy a |DP| |API| to |EC2| using the walkthrough `here <https://icebreakerone.github.io/open-energy-python-infrastructure/ec2.html>`_
        2. Use our `Python Support Library <https://icebreakerone.github.io/open-energy-python-infrastructure/>`_ to build
           a |DP| |API| on your own infrastructure
        3. Create a |DP| based on the |FAPI| subset defined in `Common Security Requirements` using your choice of language
           and deployment infrastructure
      - Technical
    * - Creation of a rule, or rules, for each dataset and publication of rule(s) in the metadata file
      - * Dataset assigned to an Open Energy Sensitivity Class
        * `Access rule <Access Control and Capability Grant Language>` or rules created, for each of which:

          - `Data access conditions` are specified
          - A grant of `capabilities` is articulated
          - Any accompanying `obligations` are articulated
      - Operational, commercial, technical
    * - Internal legal sign-off for rules
      - * Internal legal advice sought on converting any existing :term:`Shared data` licenses into |OE|
          `capabilities` and `obligations`
        * Internal legal sign-off granted for the creation of all data ‘access rules <Access Control and Capability Grant Language>’
      - Legal
    * - Skills
      - * Technical personnel can use Python programming language, or adapt existing |OE| code and tooling to
          alternative language(s) that are used internally
        * Technical personnel understand the basics of the |FAPI| authorization process as described in `Common Security Requirements`
      - Technical

Considerations for Data Consumers
#################################

.. list-table::
    :header-rows: 1
    :widths: 20 60 20

    * - Consideration
      - Includes
      - Readiness area(s)
    * - Membership contract and fees
      - * Contract review by legal counsel
        * Contract signature by person with appropriate authority
        * Membership fees paid
      - Legal, commercial
    * - Onboarding to the Directory
      - * Generic contact email addresses and organisation details provided to Open Energy for publishing in the Directory
        * Software statement created (`instructions <https://docs.google.com/document/d/1sypYWTeLFSFyfO_zTW6xKCWnao9gKjAo2JHZZIPs2xI/edit?usp=sharing>`_)
        * Transport certificate created (`instructions <https://docs.google.com/document/d/1sypYWTeLFSFyfO_zTW6xKCWnao9gKjAo2JHZZIPs2xI/edit?usp=sharing>`_)
      - Operational, technical
    * - Locate Shared data sets
      - Use of `Open Energy Search <https://openenergy.org.uk>`_
      - Operational, technical
    * - Access :term:`Shared Data`
      - Methods including one of the following:

        1. Use a web-based Python integrated development environment of your choice (e.g. Jupyter-Lab, Google
           Collab, or similar) to access and display Shared data (`step-by-step video <https://www.youtube.com/watch?v=CMI2UVdIxFw>`_)
        2. Use |OE|’s Python library to access :term:`Shared data` from your own code
           (`example <https://icebreakerone.github.io/open-energy-python-infrastructure/service_provider.html>`_)
        3. Use tools or languages of your choice to access a :term:`Shared Data` |API|.
      - Technical
    * - Use :term:`Shared data` in compliance with the appropriate licence model
      - * Ensure your organisation - and any individuals handling the data - have a clear understanding of |OE|
          `capabilities` and `obligations` for the use of datasets
        * Gain internal legal sign-off for data use, if applicable
        * Payment of related fees to the |DP| if applicable

        For |DCs| which are also |SPs|:

        * Check your understanding of the onward sharing permissions for any data, or derivatives, you are passing
          onto your customers.
        * Before passing on data or derivatives to your customers, ensure your organisation - and any individuals
          handling the data - have a clear understanding of Open Energy capabilities and obligations associated with
          onward sharing of data, and of the data pyramid.
      - All
    * - Business planning
      - For |DCs| who are |SPs|:

        * Establish or review your business model for providing services based on, or linked to, data access via |OE|
          in alignment with the agreed capabilities and access controls for the datasets the service will rely on.
        * Where a service uses multiple datasets, including those beyond Open Energy, ensure that licences are
          compatible to the service being provided and that all licences are appropriately credited.
      - Commercial




