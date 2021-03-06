Introduction to Open Energy
===========================

.. contents::
   :depth: 4
   :local:

Overview and purpose of the guidelines
######################################

The |OE| operational guidelines aim to provide practical advice to all types of actors participating in
the |OE| ecosystem. The guidelines are supplemented by links to more detailed technical and membership
documentation.

Overarching aims of these operational guidelines:

* To deliver a safe and effective Open Energy ecosystem that meets the needs of members and supports the broader
  sector transition to Net Zero by enabling better discovery and sharing of data via a robust trust framework.
* To support the operational requirements of |DPs| and |DCs|, stimulating an active Open Energy
  ecosystem. This includes ensuring that all members understand the sensitivity classes, access, and licensing models
  for data shared in the ecosystem.
* To encourage an active data sharing ecosystem in which transparency and interoperability are incentivised.
* To ensure positive member experiences that demonstrate the value of |OE| and encourage them to continue
  participating in the ecosystem.
* To minimise potential costs associated with insufficient |API| or other technical system testing, downtime, or
  other common faults.
* To reduce any reputational risks associated with individual members, incorrect application of core policies, or
  the |OE| ecosystem as a whole.

These guidelines are structured in six sections, outlining:

Introduction (this section): background to the Open Energy project, clarifications of the roles and responsibilities
of different types of actors operating in the Open Energy ecosystem.

`Open Energy Glossary`: definitions of common acronyms, terminology, and technical tools used in |OE|
documentation.

`Considerations Before You Start`: ‘at a glance’ list of items that all types of new members will need
to consider in order to meet operational requirements.

.. note::

    The *Considerations before you start* is still in review and so is not present in this version of the documentation

`Core Policies`: operational principles and policies central to Open Energy function. Includes policies
governing data sensitivity classification, access controls, and licensing.

`Guidance for Data Consumers` and `Guidance for Data Providers`: guidelines outlining how |DPs| can share data safely and
securely via the Open Energy ecosystem while retaining strong control, provide appropriate and timely metadata,
and design safe and effective |APIs| enabling data-sharing. Guidelines outlining how |DCs| can meet the
requirements for offering data services, access and licensing conditions for different data classes, and best
practice with regards to testing, security, ethics and dispute management.

`Additional Material`: links to other relevant documentation (e.g. technical, legal, etc.) sitting
outside the operational guidelines.

.. warning::

    **Disclaimer**: The contents of the Operational Guidelines do not constitute legal advice. While they have been
    drafted with regard to relevant regulatory provisions and best practice, they are not a complete list of the
    regulatory or legal obligations that apply to members and users of Open Energy. Although intended to be consistent
    with relevant regulations and laws, in the event of any conflict, those regulations and laws will take priority.
    Participants are responsible for their own compliance with all applicable regulations and laws, including but not
    limited to: data protection and privacy, consumer protection laws, and energy sector licences and codes
    (where applicable). The Open Energy operational guidelines will be revised in future in accordance with further
    development of services offered in the ecosystem, or changes to the regulatory and policy environment in which
    it operates. Please ensure that you are referring to the most current version of the guidelines prior to reading.

What is Open Energy, how was it made and who is it for?
#######################################################

Open Energy is an ambitious, non-profit project working with the energy industry, government and the regulator
to modernise access to energy data and break down barriers to data sharing. Open Energy makes it easier to
discover, share, access and use energy and related datasets, supporting the sector’s drive towards decarbonisation
and its related social and economic benefits.

Open Energy received initial development funding from the Modernising Energy Data Access competition, backed by
the Office for Gas and Electricity Markets (Ofgem), the Department for Business, Energy and Industrial Strategy
(|BEIS|), and `Innovate UK <https://www.gov.uk/government/organisations/innovate-uk>`_. The project has built on
learning from Open Banking - identifying which elements are
transferable to the energy sector, and which require adaptation or fresh thinking. Throughout this process, the
Open Energy team has engaged in extensive consultation with the energy sector, in order to ensure that the project
meets the widest possible variety of needs. The ethos of Open Energy will remain grounded in sector engagement
and a collaborative approach as the project moves forward.

Open Energy aims to serve all actors in the energy sector, and appropriate parts of allied sectors, who are looking
to share data, access data, or both. Membership is open to a wide range of organisations - from large corporations
through to charities, researchers, or community groups. Both :term:`Open <Open Data>`: and :term:`Shared Data` can
flow within the Open Energy ecosystem.

How is Open Energy Structured?
##############################

Open Energy consists of two core functions: dataset search and discovery, and the Open Energy Governance Service.
These functions are described below.

Dataset Search
--------------

Open Energy’s first core function - Open Energy Search - enables dataset search and discovery. Open Energy Search
empowers users to find out what datasets exist and who owns/controls them. Search results also outline the
`sensitivity class<Data Sensitivity Classes>`, `access rules<Data Access Conditions>`, and
`capability grants<Data Licensing>` associated with a certain dataset, meaning that access and
licensing details are transparent. This works through a search engine designed
specifically to search for datasets, with options to search by different parameters in order to refine results.
It can also be used to discover datasets adjacent to searches; helping users to build up a more rounded picture
of the energy data landscape in their sphere of interest. Open Energy search is free, available to all, and will
remain so. Access pathways to Open and Shared data are described in the following section.

Datasets provided by Open Energy members (|DPs|) and non-Open Energy members (e.g. web scraped Open Data)
may both be visible in Open Energy Search. Datasets provided by an Open Energy member will be demarcated with a
green tick to indicate that the provenance of the dataset has been verified, uptime is monitored, documentation
format is known, and users have a mechanism to provide feedback on the dataset if issues are detected. (Please
note that this does not indicate that Open Energy has carried out further, more extensive checks on data quality
within members’ datasets.)

Governance Service
------------------

Open Energy's second core function - our Governance Service (|OEGS|) - supports members to provide, share and
access different classes of Shared data (see `Data Sensitivity Classes`) on the basis of preemptive licensing
(see `Data Licensing`). Shared Data accessed via the |OEGS| will be provided by members only
(|DPs|). The Governance Service aims to provide a secure, trusted mechanism to improve data sharing
across the sector by reducing the time and financial costs currently associated with accessing Shared data.
For providers of Shared data, the Governance Service offers a secure and effective way to list datasets and
set appropriate access and licensing requirements. For actors wishing to access Shared data, the Governance
Service provides a mechanism to reduce friction and bilateral contract negotiation, even when requesting
access to multiple datasets from different providers.

Project Governance
------------------

During Phase 3, Open Energy was governed by two Advisory Groups (Membership and Delivery) and a Steering Group.
The groups met once a month and a brief description of each group’s activities is given below.

**Membership Advisory Group**: Consulted on the Membership contract, key policies, including conditions to participate,
roles, responsibilities and liabilities, draft preemptive licence, funding model, operational guidelines, and
ongoing governance.

**Delivery Advisory Group**: Consulted on the drafting of operational guidelines and understanding data production
and usage. Fed into the requirements for technical delivery of the Open Energy Governance Service and the Energy
Data Search to ensure they meet user needs. Alongside this, examined the day-to-day operational aspects of Open Energy including security and systems.

**Steering Group**: Supported the overarching strategy, ensured the delivery of our objectives, and helped
disseminate work.

The membership of these groups was designed to represent a range of different types of organisations in the
energy sector, and broader digital sector where relevant. Open Energy is guided by our principle of
‘by the sector, for the sector’ and we will review our governance beyond Phase 3 to ensure we continue to align
with this principle. Open Energy members can apply to join the Advisory and Steering Groups. However, membership
of these groups will not be restricted to members only and non-members may be invited to join in order to balance
representation. If you are interested in participating in future Open Energy governance mechanisms please contact
openenergy@icebreakerone.org.

What data can be found and used through Open Energy?
####################################################

Open Energy supports both Open and Shared datasets containing energy, and energy-related, data. Different classes
of data within the Open Energy ecosystem, assessed by their levels of sensitivity, are described in
`Data Sensitivity Classes`.

Open data
---------

Open data is defined in the Open Energy ecosystem as: ‘Data that anyone can use, for any purpose, for free and is
accessible under an Open data licence’. Examples of open datasets include (non-exhaustive): Lower Super Output
Layer |ID| (|LSOA|) data, Digest of |UK| Energy Statistics, and OpenStreetMap data.

Open data is visible via Open Energy Search, which is free and open to all users. Open datasets provided by Open
Energy members (|DPs|) and non-Open Energy members will both be visible. There are no barriers to accessing
Open data once it is discovered - users are directed to an appropriate |URL| or |API| to access the data themselves.
Open data access is not moderated via the |OEGS| as no additional access controls are required.

Shared data
-----------

Shared data is defined in the Open Energy ecosystem as: ‘Data that is neither open nor closed, but can be shared
under specific terms and conditions.’ Examples of datasets currently licensed as Shared data include
(non-exhaustive): primary substation capacity, network outage data, weather predictions, European space agency
data, Electralink daily smart meter installations, certain geolocation information for energy assets and building
typologies. As illustrated in these examples, Shared data is extremely diverse and can include datasets with a
range of different commercial, personal and security sensitivity levels. To provide nuance in this area, Open
Energy consultations have established a set of five data sensitivity classes, in which three classes describe
separate categories of Shared data.

Due to the sheer diversity of data types in the energy sector, Open Energy had to limit focus for Phase 3 development.
At present, the |OEGS| can facilitate the sharing of non-personal Shared data classes only. This means that currently,
sharing of non-aggregated personal data (including datasets using forms of anonymisation other than aggregation conforming
to |ICO| / |ONS| best practice) is not permitted in the Open Energy ecosystem. Functionality to share personal data
(class |OE-SP|), and data that has been anonymised using techniques other than aggregation, may be extensible
in future subject to further consultation.

The metadata and sensitivity class of Shared datasets are listed in Open Energy Search and are visible to any user.
Shared datasets provided by Open Energy members (|DPs|) and non-Open Energy members are both visible
(where the latter are known), as described later in this section. Access to Shared datasets provided by Open Energy
members is moderated through the Open Energy Governance Service, on the basis of preemptive licensing. Access to
Shared data listed on the Search that is not provided by an Open Energy member is not supported - users should
contact the non-member organisation directly to arrange access.

Closed data
-----------

Closed data is defined in the Open Energy ecosystem as: ‘Data that either cannot be shared or requires a per-use,
custom licence negotiated on a case-by-case basis’. Under our current model, closed data is never suitable to share
within the Open Energy ecosystem and is not visible through Open Energy Search. While we acknowledge industry
feedback flagging potential value in using Open Energy infrastructure to privately share Closed data not listed in
the Search or |OEGS| Directory, this is not a focus of project development in the present phase. Any extensibility of
this function in future will be subject to consultation.

What role does your organisation play in the Open Energy ecosystem?
###################################################################

Members of the Open Energy ecosystem have different roles: |DPs|, |DCs|, or both. This section
outlines the meaning of the different roles and outlines their basic responsibilities.

|DPs|
--------------

|DPs| are organisations that control datasets that they wish to make visible and/or accessible through the
Open Energy ecosystem. |DPs| can provide Open and/or Shared datasets. |DPs| are responsible for:
data sensitivity classification, creation of access rules, creation of capability grants, data provision, data
integrity and correctness, metadata provision, and |API| availability, stability and change management. Full guidance
regarding |DP| responsibilities can be found in `Guidance for Data Providers`.

Data Consumers
--------------

|DCs| are organisations that seek to find and access datasets through the Open Energy Governance Service
Service. |DCs| can be established to serve internal organisational needs, to serve external customers,
or both. |DCs| is a catch-all term referring to all parties accessing data via the |OEGS|. Full guidance can be found
in `Guidance for Data Consumers`

Service Providers
_________________

|DCs| who access data to serve external customers, potentially including customers outside the Open Energy
ecosystem, are categorised as a specific type of |DC| called a |SP|. See `Data Consumer vs Service Provider`.

Dual Roles
----------

Organisations wishing to both provide and access data through the Open Energy ecosystem are able to do so, so long
as they fulfill the responsibilities of both roles. |DPs| who do not want to register as |DCs|,
but who wish to access Open Energy datasets, are able to do so by using the services of a Service Provider (a
type of |DC| in the Open Energy ecosystem that provides services to customers, potentially including non
Open Energy members).

How does dataset access and licensing operate under Open Energy?
################################################################

Open Energy has consulted publicly and with industry on policies pertaining to: the types of conditions on which
data access controls can be based, the process by which |DPs| establish access rules for a dataset, and
the model for associating access rules with the grant of particular capabilities and obligations (licensing model).
These policies are outlined briefly below, and set out in full detail in Section 3 of the Operational Guidelines.

Types of Access Conditions
--------------------------

Open Energy has established a set of conditions which may be specified for |DCs| to meet in order to gain
access to datasets in different sensitivity classes. These include, but are not limited to: payment, security
compliance, regulatory compliance, standards compliance, group-based access, and use case-based access.

Creating Access Rules (Introduction)
------------------------------------

To operationalise Data Access conditions above, we propose a system whereby access grants are determined, for each
request to the |API| of a |DP|, on the basis of a set of rules defined and published by that |DP| in the
dataset metadata.

Data Licensing (Introduction)
-----------------------------

A data licence is a legal instrument setting out what a |DC| can do with a particular artefact (e.g.
dataset). This grants certain ‘capabilities’ to the |DC|, comprising a clear expression of things they
can do with the artefact. Capability grants are accompanied by any obligations that the |DC| must abide
by when exercising a capability. The capabilities and obligations associated with each |API| call will be converted
into a licence through the Open Energy Governance Service (|OEGS|).

|OE| operates through a range of standardised capability grants and obligations. Standardisation
includes legal text, ‘human readable’ text and summary notation. |DPs| must specify which capabilities
and obligations are associated with each access rule, and publish this transparently in the dataset metadata.

Future development of the guidelines
####################################

This version of the guidelines contains details of operational requirements defined within Phase 3
(ending 31 July 2021). The guidelines are designed as an iterative document that will develop in
accordance with future phases of Open Energy. If you have any suggestions regarding areas of the operational
guidelines that could benefit from further development, please contact openenergy@icebreakerone.org.