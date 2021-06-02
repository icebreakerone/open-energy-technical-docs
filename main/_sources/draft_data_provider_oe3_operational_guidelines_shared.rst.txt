Data Provider Operational Guidelines
####################################

*Primary audience: Data provider technical operations teams*

.. note::

    Derived somewhat from `OB ops guidelines <https://docs.google.com/document/d/1g1-qJN92UwnaxgaS8yu_KBvoFfHDVH5kIYH_lTM9lec/edit?userstoinvite=timjohnson365@googlemail.com&ts=5f95f246&actionButton=1#>`_ but very little of the Open Banking guidelines apply to our use cases so it’s only very loosely based on the original document.

.. note::

    The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
    "SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be
    interpreted as described in :RFC:`2119`


Data Provider Role and Responsibilities
***************************************


Data Providers (DPs) are Open Energy members which make data sets available to:


* Service Providers (SPs) within the Open Energy ecosystem

  * Applies to shared data sets
  * Data APIs secured using Financial-grade API security (FAPI)
  * DP is responsible for access control determination
  * DP is responsible for licensing of any data returned

* Any third party, in the case of open data

  * Open data sets are made available through publicly accessible APIs
  * Data are made available under an appropriate open license agreement


* In this context, Data APIs can be anything from a simple link to a CSV or other file (for open data) to a complex query system returning custom output on demand.

To support this role, DPs have certain responsibilities:



Responsibility - Data classification
====================================


DPs are responsible for determining whether any given data set falls into the category of open data, shared data, or one of the data classes which must not be shared through the Open Energy ecosystem [see data sensitivity classification document]



Responsibility - Data provision
===============================


DPs are responsible for providing a data API for each data set, and for configuring and securing each API in accordance with the kinds of data it exposes (along with any other access conditions deemed necessary and appropriate by the DP on a per-data-set basis)


* Open data is made available with no authentication or authorization requirements
* Shared data is made available through a FAPI compliant resource server connected to the OEGPs authorization service



Responsibility - Data integrity and correctness
===============================================


DPs are responsible for the correctness of data returned by their published data APIs. The OEGP will provide a mechanism by which SPs can report any data quality issues, and will convey any such reports to a nominated contact within the DP.



Responsibility - Metadata provision
===================================


DPs are responsible for creating, and publishing, metadata for each exposed data set. This provides visibility of each data set within the Open Energy Governance Platform (OEGP) Registry.


Metadata for a data set include, but are not limited to:


* The kinds of data held within the data set

  * Varies from a high level description, down to semantics and typing for individual fields within data sets. 

* The means to query this data
* Any access or licensing constraints

  * See discussion and proposal `here <https://docs.google.com/document/d/1IE3nxELcVnQMiNmOvCL5geS_kFHAd7QE2jELjeqc5PI/edit?usp=sharing>`_


The DP is responsible for the accuracy and completeness of this metadata.



Consider whether time-based metadata / temporal “status” of data should be tied to the minimum standards for Data Providers to adhere to.




Responsibility - API availability
=================================


DPs are responsible for availability of their published data APIs. Availability will be monitored automatically by the OEGP, availability information will form part of the metadata for each data set record in the OEGP Registry.


The OEGP will provide a mechanism for DPs to announce scheduled downtime when planned, and to report unscheduled downtime when necessary.



Responsibility - API stability and change management
====================================================


DPs are responsible for managing any change to the data APIs such that disruption to SPs is minimised. This is handled through:


* `Semantic versioning <https://semver.org/>`_ of all API methods
* Publication of anticipated changes and retirement of API versions through the OEGP
* Changeover periods where new and prior API versions are run in parallel



Data API Requirements
*********************


Unlike open banking, open energy does not mandate particular APIs for data provision - it is expected that there will be a variety of mechanisms to expose data, with varying inputs (from a single data set ID to a complex query object) and varying kinds of output dependent on the information exposed. 


With that said, there are certain properties that all data APIs must satisfy to interoperate successfully with other parties within the open energy ecosystem.


In this context, a data API is a set of HTTP locations and methods below a root URL, we will use https://example.com/data/ as the root.


We refer to endpoints used to retrieve energy data as **data endpoints**, and others as **infrastructure endpoints**.



Date and time formats
=====================


Whenever date or time quantities are accepted or returned from a data API, these values MUST conform to `RFC 3339 <https://tools.ietf.org/html/rfc3339>`_. This is referenced elsewhere in this document as **date/time**




Endpoint security
=================

Open data endpoints
-------------------
Data endpoints which provide access to open data MUST NOT require any form of authentication prior to access. This includes allowing access to entities which are not members of the open energy ecosystem.

Shared data endpoints
---------------------
Data endpoints which provide access to shared data MUST implement the resource server part of the FAPI specification, and authorize against the OEGP authorization service.


Protected data endpoints MAY use the token introspection mechanism provided by FAPI to gather additional information about the client making the request prior to any access decision.



Heartbeat and monitoring endpoint
=================================


All data APIs MUST include a FAPI protected heartbeat infrastructure endpoint. This serves two purposes:


* It allows the OEGP to monitor the liveness of the data API
* It provides some level of verification that the resource server has been correctly configured


The heartbeat endpoint is located at https://example.com/data/heartbeat and MUST respond to GET requests from the OEGP monitoring system with a 200 status code.


If the heartbeat response contains a body, the body will be interpreted by the OEGP monitoring system as a JSON dictionary containing statistics for the period between the most recent two successful calls to the heartbeat endpoint (including the call to which this is a response). This response is RECOMMENDED as it provides oversight of API usage to the OEGP.


Legal keys, and the semantics of their associated values, are as follows:


+-----+----------------------------------------------------------------------------------------------------------------------------------------------------+
| per |**date/time** of the end of the period for which statistics are reported,                                                                           |
|     |this will typically be the date and time of the heartbeat request                                                                                   |
+-----+----------------------------------------------------------------------------------------------------------------------------------------------------+
| api |**integer** number of requests to non-heartbeat endpoints within this data API which resulted in a response of type **CODE**. A distinct key:value  |
| _ca |pair is sent in the response for each distinct HTTP status code returned.                                                                           |
+-----+----------------------------------------------------------------------------------------------------------------------------------------------------+


Self documenting
================


All data APIs MUST include an unsecured infrastructure endpoint at https://example.com/data/api which responds to GET requests with some kind of human readable API documentation, or a redirection to this documentation held elsewhere.



Versioning
==========


All data APIs MUST include a version number in the path of each data endpoint. This version SHOULD use `semantic versioning <https://semver.org/>`_ to differentiate between breaking and backwards compatible changes.

Version infrastructure endpoint
-------------------------------
A data API making use of semantic versioning SHOULD expose an unprotected infrastructure endpoint at https://example.com/data/versions which responds to GET requests with the following JSON structure:

.. code-block:: json

    {
        "semantic_version" : true,
        "versions" : [ "v1.0", "v1.1", "v2.0" ]
    }

The intent is to allow clients to dynamically call compatible versions of APIs as and when patch or back-compatible changes are made by the data provider.

*Example:*

Version 1.0 of a query API might be available at ``https://example.com/data/v1.0.0/solarpv``, the data provider creates and deploys version ``1.0.1`` to fix a minor performance issue, this is deployed at ``https://example.com/data/v1.0.1/solarpv``.


If the data API uses semantic versioning and is providing the version infrastructure endpoint, there is no need to run both APIs in parallel - a client can introspect and determine that version 1.0.1 is inherently compatible with 1.0.0.

Problem Resolution
******************
Note - sections lifted from open banking ops guidelines, for discussion! I’ve attempted to be selective in what I’ve copied across, not everything was applicable and much of it was excessively verbose.



Effective resolution of problems
================================


A DP should create documentation to clearly outline the policies, processes and systems it has in place for problem resolution and its respective service level objectives. This framework should enable the effective resolution of Service Provider (SP) issues and therefore cater for problems that relate specifically to a SP’s use of a DP’s data APIs.

Online support
==============
DPs should provide FAQs, which address areas that may be specific to SPs such as technical advice or test facility guidance. They should also consider a means of identifying recurring questions or user-error issues so these can be collated into FAQs to support the early resolution of problems.
Problem resolution documentation, FAQs, contact details, opening times and out of hours support should be published and easily accessible in one collective area on the DP’s website.

Ticket management process
=========================
DPs must ensure they have a functioning ticket management system which enables them to respond to issues and problems raised within clearly defined service level targets. A successful problem resolution framework will enable the efficient identification and resolution of problems which specifically impact SPs. The system for raising and reporting on tickets should be transparent in order to fully inform users and engender trust across the ecosystem.
[elided - a massively long section on precise ticket classifications and first response SLA expectations, do we need these?]

OEGP support
============
OEGP Service Desk provides participants with a supplementary ticket management process and supports DPs in communicating problems to ecosystem participants via the noticeboard. 


Change Management
*****************
This chapter outlines various change scenarios that may impact SPs, and provides guidance for a DP to consider when implementing a change and communicating to SPs.

Down time
=========
Planned downtime, by its nature, is something that a DP anticipates and therefore is able to give advance notice to SPs. It is not generally possible to give advance notice of unplanned downtime, but DPs should give notice as soon as they are aware of the downtime.
When providing notifications, DPs should provide a specific time period, so SPs are aware that the data API will be unavailable for that time, or upon a subsequent notification to confirm that the service has been reinstated sooner than anticipated.
OEGP Support Services can assist DPs with the dissemination of downtime information to the wider Open Energy ecosystem via its central noticeboard facility**.**Planned downtime should be given at least five business days before the event. Apart from cancelling the planned downtime, no changes should be made to the planned downtime notification within the five business day period. Where practical, DPs should give advance notice via their own website, developer portal or OEGP of any planned downtime one calendar month in advance.

Data API changes
================
Data providers may periodically wish to upgrade and / or to deprecate versions of their data APIs. The following mitigation measures will reduce the impact on service providers of these changes.

Dual running and deprecation
----------------------------
DPs should support a minimum of two non-compatible API versions in a production context, providing both versions were previously supported by the DP, for a period of time long enough to ensure that SPs have had sufficient time to successfully test the new version and migrate their applications and customers. OEGP recommends dual running for at least six months for a major version, and three months for a minor version. Where a DP implements a data API for the first time, they will only need to support this one version to start with.
The ability to support two data API versions allows SPs to maintain existing integrations with the older version, and benefit from features and enhancements offered by the new version. Over time, SPs will migrate all their applications to consume the new data API version. Once migrated, SPs should not access resources via the old API version.
The deprecation of unsupported versions is at the DP’s discretion – based on usage metrics. However, the OEGP may recommend that any specified version (major, minor, or patch) should be deprecated at any time, and this should be implemented within three months of notification by the OEGP. This is to cater for critical defects, especially those relating to security. In exceptional circumstances it may be agreed by OEGP that support for a specified version is terminated earlier.
DPs must not apply any measures to induce SPs to adopt a new version of the APIs (e.g. rate limiting the older version while providing better performance on a newer version).

API credentials, consent and authorisation
------------------------------------------
API Credentials associated with an API should be version agnostic. Therefore, a SP accessing v1.0, v1.1 or v2.0 should be able to use the same API Credentials across all available API endpoints.
[ elided another list of change management categories and SLAs that isn’t really appropriate for open energy ]
