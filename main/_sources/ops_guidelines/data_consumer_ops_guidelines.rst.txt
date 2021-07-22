Guidance for Data Consumers
===========================

.. note::

    This documented is primarily intended for technical and operations teams within organisations wishing
    to participate in Open Energy as Data Consumers.

.. include:: /rfc2119.txt

.. contents::
   :depth: 4
   :local:

Data Consumer Role and Responsibilities
#######################################

|DCs| are Open Energy members which can consume Shared Data (classes |OE-SA| and |OE-SB| in our
`Data Sensitivity Classes`) from |APIs| produced and maintained by |DPs|.

In the figure below, we expect |DCs| to occupy a number of roles from the lowest in the diagram upwards - they
are organisations able to configure their infrastructure (in terms of the consumer parts of the
`Common Security Requirements`, specifically `Token acquisition` and `Token usage - calling a shared data API`). This
is covered by the bottom two boxes.

Data Consumer vs Service Provider
---------------------------------

Open Energy does not differentiate between |DCs| that access data to solve a problem internal to their
organisation and those (known as |SPs|) which offer this as a service to other organisations. A |DC| may also be a |DP|
, the roles are not mutually exclusive.

In a similar vein, it would be entirely normal for a |DC| to also access :term:`Open Data`, and to use the |OEGS|
search system to locate data sets of interest, both open and shared.

.. figure:: images/consumer_abstraction_stack.svg
    :name: consumer_abstraction_stack_image

    Data Consumers in a typical problem solving context

Responsibility - Data consumption
---------------------------------

The definition of a |DC| is that it consumes data from :term:`shared data` |APIs|. To do this, the organisation **MUST**
create cryptographic key material, and maintain a record within the |OEGS| directory. It is responsible for the
integrity of this key material, and **MUST** put appropriate policies in place to ensure that this material is not
misused.

Responsibility - Data licensing
-------------------------------

|DCs| are responsible for honouring the licenses for any data obtained through :term:`shared data` |APIs|. Where the |OEGS|
provides technical measures such as cryptographically signed receipts binding data and license conditions together, the
|DC| is responsible for retaining and storing such receipts.

Problem Resolution (Data Consumers)
###################################

Effective resolution of problems (Data Consumers)
-------------------------------------------------

We encourage |DCs| to direct any problems with data |APIs| first to the |DP| concerned. In the event
that a |DC| is unable to resolve an issue with a |DP|, the issue MAY be flagged to the |OEGS| Dispute
Resolution function for independent support.

Dispute resolution for access control and capability grant policies
-------------------------------------------------------------------

In cases where a |DC| believes that access conditions or capability grant rules are being applied unfairly, the |OEGS|
will act as a mediating party.

OEGS support
------------

The |OEGS| Service Desk will provide participants with a supplementary ticket management process and supports |DCs|
in communicating problems to ecosystem participants via the noticeboard.