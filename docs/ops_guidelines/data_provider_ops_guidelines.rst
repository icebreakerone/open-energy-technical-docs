Guidance for Data Providers
===========================

.. note::

    This documented is primarily intended for technical and operations teams within organisations wishing
    to participate in Open Energy as Data Providers.

.. note::

    The key words **"MUST"**, **"MUST NOT"**, **"REQUIRED"**, **"SHALL"**, **"SHALL NOT"**, **"SHOULD"**,
    **"SHOULD NOT"**, **"RECOMMENDED"**, **"MAY"**, and **"OPTIONAL"** in this document are to be interpreted
    as described in `RFC 2119 <https://www.ietf.org/rfc/rfc2119.txt>`_.

.. contents::
   :depth: 4
   :local:

Data Provider Role and Responsibilities
---------------------------------------

:term:`Data Providers <Data Provider>` (|DP|) are Open Energy members which make data sets available to:

* :term:`Data Consumers <Data Consumer>` (|DC|) within the Open Energy ecosystem

  * Applies to shared data sets
  * Data APIs secured using Financial-grade API security (|FAPI|)

* Any third party, in the case of open data

  * Open data sets are made available through publicly accessible APIs
  * Data are made available under an appropriate open license agreement

In this context, Data APIs can be anything from a simple link to a CSV or other file (for open data) to a complex
query system returning custom output on demand.

To support this role, DPs have certain responsibilities:

Responsibility - Data classification
####################################

Data providers are responsible for classification of their data sets by data sensitivity class, and for ensuring that
data are shared, or not shared, as appropriate.

* Any data classed as |OE-C| (Closed) or |OE-SP| (Personal) **MUST NOT** be shared within the Open Energy ecosystem
  at present.
* Data in |OE-O|, |OE-SA|, and |OE-SB| **MAY** be shared within the Open Energy ecosystem as described in the
  following sections

Responsibility - Access and licensing specification
###################################################

DPs are responsible for creating access rules for each dataset shared via Open Energy. For each data set, the DP must
create a set of one or more access rules as defined in `Data Set Metadata`. These rules specify the conditions under which access will be
granted, along with the capabilities forming the license grant should those conditions be satisfied.

* DPs **MUST** ensure that access conditions and capability grants are non-discriminatory and fair to Data Consumers
* DPs **SHOULD** ensure that the validity time bounds of any published capability grants are sufficient for
  reasonable commercial operation of a data consumer

Responsibility - Data provision
###############################

DPs are responsible for providing a data API for each data set, and for configuring and securing each API in accordance
with the kinds of data it exposes (along with any other access conditions deemed necessary and appropriate by the DP
on a per-data-set basis)

* Open data **MUST** be made available with no authentication or authorization requirements
* Shared data **MUST** made available through a FAPI compliant resource server connected to the OEGSs authorization
  service

Data formats
____________

Open Energy does not define or mandate individual data formats to be returned from data APIs - the diversity of kinds
of information in the sector renders this impractical, and the additional overhead imposed on data providers would be
undesirable.

With this said, we would encourage data providers to consider likely automated consumption of data when designing their
data APIs - this implies using machine readable formats such as CSV, JSON and similar, with a preference for those
formats compatible with existing software tools and libraries.

Responsibility - Data integrity and correctness
###############################################

DPs are responsible for the correctness of data returned by their published data APIs. The OEGS will provide a
mechanism by which DCs can report any data quality issues, and will convey any such reports to a nominated contact
within the DP.

Responsibility - Metadata provision
###################################

DPs are responsible for creating, and publishing, metadata for each exposed data set. This provides visibility of each
data set within the Open Energy Governance Platform (OEGS) Registry.

The metadata file covers, for each provided data set, whether shared or open:

* Semantic content
* Access rules and licensing of the data set
* Transport mechanism specification
* Syntactic content

The content and format of the metadata file can be found at `Data Set Metadata`.

The DP is responsible for the accuracy and completeness of this metadata.

Responsibility - API availability
#################################

DPs are responsible for availability of their published data APIs. Availability will be monitored automatically by the
OEGS, availability information will form part of the metadata for each data set record in the OEGS Registry.

The OEGS will provide a mechanism for DPs to announce scheduled downtime when planned, and to report unscheduled
downtime when necessary.

Responsibility - API stability and change management
####################################################

DPs are responsible for managing any change to the data APIs such that disruption to DCs is minimised. This is handled
through:

* Semantic versioning of all API methods
* Publication of anticipated changes and retirement of API versions through the OEGS
* Changeover periods where new and prior API versions are run in parallel

Data API Requirements
---------------------

Unlike open banking, open energy does not mandate particular APIs for data provision - it is expected that there will
be a variety of mechanisms to expose data, with varying inputs (from a single data set ID to a complex query object)
and varying kinds of output dependent on the information exposed.

With that said, there are certain properties that all data APIs must satisfy to interoperate successfully with other
parties within the open energy ecosystem.

We refer to endpoints used to retrieve energy data as data endpoints, and others as infrastructure endpoints.

Date and time formats
#####################

Whenever date or time quantities are accepted or returned from a data API, these values MUST conform to
`RFC 3339 <https://tools.ietf.org/html/rfc3339>`_. This is referenced elsewhere in this document as **date/time**

Endpoint security
#################

Open data endpoints
___________________

Data endpoints which provide access to open data (in class |OE-O|) **MUST NOT** require any form of authentication
prior to access. This includes allowing access to entities which are not members of the open energy ecosystem.

Shared data endpoints
_____________________

Data endpoints which provide access to shared data (in classes |OE-SA| and |OE-SB|) **MUST** implement the subset
of the resource server part of the FAPI specification used within Open Energy as described in
`Common Security Requirements`, and authorize against the OEGS authorization service.

Protected data endpoints **MAY** use the token introspection mechanism provided by |FAPI| to gather additional
information about the client making the request prior to any access decision.

Heartbeat and monitoring endpoint
#################################

All data APIs SHOULD include a |FAPI| protected heartbeat infrastructure endpoint. This serves two purposes:

* It allows the OEGS to monitor the liveness of the data API
* It provides some level of verification that the resource server has been correctly configured

The heartbeat endpoint location is defined within the data set metadata file, if specified it **MUST** respond to
``GET`` requests from the OEGS monitoring system with a ``200`` status code.

If the heartbeat response contains a body, the body will be interpreted by the OEGS monitoring system as a JSON
dictionary containing statistics for the period between the most recent two successful calls to the heartbeat
endpoint (including the call to which this is a response). This response is **RECOMMENDED** as it provides oversight
of API usage to the OEGS.

Legal keys, and the semantics of their associated values, are as follows:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Name
     - Content
   * - ``period_start``
     - **date/time** of the start of the period for which statistics are reported
   * - ``period_end``
     - **date/time** of the end of the period for which statistics are reported, this will typically be the date and
       time of the heartbeat request
   * - ``api_call_response_[CODE]_count``
     - integer number of requests to non-heartbeat endpoints within this data API which resulted in a response of type
       CODE. A distinct key:value pair is sent in the response for each distinct HTTP status code returned.

API documentation
#################

Data APIs **MUST** be described within the transport section of the data set metadata file.

Versioning
##########

All data APIs **MUST** include a version number in the path of each data endpoint. This version SHOULD use semantic
versioning to differentiate between breaking and backwards compatible changes. This **MUST** be documented within the
OpenAPI transport section of the metadata file.

Problem Resolution (Data Providers)
-----------------------------------

Effective resolution of problems (Data Providers)
#################################################

A DP **MUST** create documentation to clearly outline the policies, processes and systems it has in place for problem
resolution and its respective service level objectives. This framework should enable the effective resolution of DC
issues and therefore cater for problems that relate specifically to a DC’s use of a DP’s data APIs. In the event that a
DC is unable to resolve an issue with a DP, the issue **MAY** be flagged to the OEGS Dispute Resolution function for
independent support.

Online support
##############

DPs **SHOULD** provide FAQs, which address areas that may be specific to DCs such as technical advice or test facility
guidance. They should also consider a means of identifying recurring questions or user-error issues so these can be
collated into FAQs to support the early resolution of problems.

Problem resolution documentation, FAQs, contact details, opening times and out of hours support **SHOULD** be published
and easily accessible in one collective area on the DP’s website.

Ticket management process
#########################

DPs **MUST** ensure they have a functioning ticket management system which enables them to respond to issues and
problems raised within clearly defined service level targets. A successful problem resolution framework will enable the
efficient identification and resolution of problems which specifically impact DCs. The system for raising and reporting
on tickets should be transparent in order to fully inform users and engender trust across the ecosystem.

Dispute resolution for access control and capability grant policies (Data Providers)
####################################################################################

In cases where a DC believes that access conditions or capability grant rules are being applied unfairly, the OEGS
will act as a mediating party.

OEGS support (Data Providers)
#############################

The OEGS Service Desk will provide participants with a supplementary ticket management process and supports DPs in
communicating problems to ecosystem participants via the noticeboard.

Change Management
-----------------

This section outlines various change scenarios that may impact DCs, and provides guidance for a DP to consider when
implementing a change and communicating to DCs.

Downtime
########

Planned downtime, by definition, is something that a DP anticipates and therefore is able to give advance notice to DCs.
It is not generally possible to give advance notice of unplanned downtime, but DPs should give notice as soon as they
are aware of the downtime.

When providing notifications, DPs **SHOULD** provide a specific time period, so DCs are aware that the data API will be
unavailable for that time, or upon a subsequent notification to confirm that the service has been reinstated sooner
than anticipated.

OEGS Support Services can assist DPs with the dissemination of downtime information to the wider Open Energy ecosystem
via its central noticeboard facility.

Planned downtime should be given at least five business days before the event. Apart from cancelling the planned
downtime, no changes should be made to the planned downtime notification within the five business day period. Where
practical, DPs should give advance notice via their own website, developer portal or OEGS of any planned downtime one
calendar month in advance.

Licensing and access control changes
####################################

DPs **MUST** provide advance notice of any changes to access control and capability grant policies. This is normally
covered by the time-bounded nature of these grants, but DPs MAY also use any notification services provided by the OEGS
to publish additional information about changes.

Data API changes
################

Data providers may periodically wish to upgrade and / or to deprecate versions of their data APIs. The following
mitigation measures will reduce the impact on service providers of these changes.

Dual running and deprecation
____________________________

DPs **SHOULD** support a minimum of two non-compatible API versions in a production context, providing both versions
were previously supported by the DP, for a period of time long enough to ensure that DCs have had sufficient time to
successfully test the new version and migrate their applications and customers. OEGS recommends dual running for at
least six months for a major version, and three months for a minor version. Where a DP implements a data API for the
first time, they will only need to support this one version to start with.

The deprecation of unsupported versions is at the DP’s discretion – based on usage metrics. However, the OEGS may
recommend that any specific version (major, minor, or patch) should be deprecated at any time, and this should be
implemented within three months of notification by the OEGS. This is to cater for critical defects, especially those
relating to security. In exceptional circumstances it may be agreed by OEGS that support for a specific version is
terminated earlier.

DPs must not apply any measures to induce DCs to adopt a new version of the APIs (e.g. rate limiting the older version
while providing better performance on a newer version).

API credentials, consent and authorisation
__________________________________________

API Credentials associated with an API should be version agnostic. Therefore, a DC accessing v1.0, v1.1 or v2.0 should
be able to use the same API Credentials across all available API endpoints.
