Access Control and Capability Grant Language
============================================

.. contents::
   :depth: 4
   :local:

Access rules, capability grants, and obligations are explained in `Data Access Conditions`, this document specifies the
precise syntax and values that can be used.

An access rule contains:

1. Zero or more conditions for access
2. One or more capability grants to the data consumer if access is granted
3. Zero or more obligations falling on the data consumer if access is granted

They are applied to properties of a :term:`Data Consumer` while processing a request for data from a
:term:`Data Provider`. These properties can be modelled as a map of names to values; some values may be inferred by
joining on the |ID| of the data consumer, some may be directly provided in the `token introspection` response.

Syntax
######

Names
-----

**Names** consist of a namespace (``[a-z0-9_]+``), a ``:`` character, and a suffix (``[a-z0-9_.]+``). For example,
``oe:some_value``. Values asserted by Open Energy will always have a namespace ``oe``. The suffix may contain ``.``
characters, the namespace may not.

Rule syntax
-----------

An access rule is represented as a single line string containing a comma separated list of zero or more `Conditions`,
the literal string ``grants``, and then a comma separated list of one or more `Capabilities`. Optionally, this may
be followed by the literal ``requires`` and one or more `Obligations` in a comma separated list.

.. code-block::

   [CONDITION]? ["," CONDITION]* "grants" CAPABILITY ["," CAPABILITY]* ["requires" OBLIGATION+ ["," OBLIGATION]

.. note::

   * A rule with no conditions is valid, and is satisfied by all requests
   * All rules must grant at least one capability
   * Rules may have zero or more obligations

See the following sections for specification of conditions and capabilities.


Conditions
##########

Conditions are unary or binary clauses.

All conditions must be satisfied within a rule for that rule to be applied. There are no explicit boolean operators
such as ``or`` or similar. For cases where alternative sets of rules could be applied the expectation is that data
providers will specify multiple, potentially overlapping, rules to express this.

Unary clauses
-------------

Unary clauses consist of a single **named** condition. The clause is satisfied if that condition is ``true``.
This is typically used to denote a particular property such as *Open Energy current membership* or similar where the
existence of the property is sufficient to accept the data consumer.

.. code-block:: json
   :caption: the condition ``oe:member`` passes if used with this context

    {"oe:member" : true}

Binary clauses
--------------

Binary clauses consist of a **name** on the left hand side, an **operator**, and a **value** on the right hand side.
The valid **operators** are shown in the table below. LHS, operator, and RHS are separated with at least one
space character.

**Values** can be numerals, dates, quoted strings, or homogeneous lists of these three types. Dates are specified as
``dd/mm/yyyy``, we do not need a higher level of precision in any of our envisaged use cases, but if this is needed
a datetime must be specified as a string compliant with `RFC3339 <https://datatracker.ietf.org/doc/html/rfc3339>`_. To
simplify expression in |JSON|, quoted strings should be enclosed in single quote ``'`` characters. Lists are written as a
comma separated list of strings surrounded by ``[`` and ``]`` characters. Lists are only valid RHS values for the
``in`` operator.

.. list-table:: Operators
   :widths: 15 15 70
   :header-rows: 1

   * - Operator
     - Range
     - Description
   * - ``is``
     - Any
     - The condition passes if the value of the property on the LHS is exactly equal to the value in the RHS
   * - ``before``
     - date or datetime
     - The condition passes if the value of the property on the LHS is before the date or datetime specifed as the
       RHS. Where a date needs to be coerced to a datetime, it is done by setting it to 00:00.00 with the same date
   * - ``after``
     - date or datetime
     - As above, but passes if the value of the property on the LHS is after the date or datetime specified on the RHS.
   * - ``max_age_days``
     - date or datetime
     - The condition passes if the value on the LHS corresponds to a date at most X days in the past compared to the
       current date, where X is integer numeral specified as the RHS
   * - ``<``, ``<=``, ``>=``, ``>``, ``==``
     - number
     - Conditions pass if the LHS is, respectively, less than, less than or equal, greater than or equal, greater than,
       or strictly equal, to the number on the RHS. Note that ``==`` and ``is`` are equivalent for numeric quantities
   * - ``in``
     - number or string
     - Conditions pass if there is at least one item in the list specified in the RHS which would match the ``is``
       condition with respect to the LHS value

Example conditions
------------------

.. note::

   The conditions shown below are examples, and should not be taken as indicative of standard properties of data
   consumers in the final system.

.. list-table:: Example condition clauses
   :widths: 15 85
   :header-rows: 1

   * - Condition
     - Interpretation
   * - ``oe:status is 'active'``
     - passes if the value of ``oe:status`` is set, and is equal under string comparison to ``active``
   * - ``oe:membership_expires after 24/10/2022``
     - passes if the value of ``oe:membership_expires`` is either a date or a datetime, and is after the 24th October
       2022
   * - ``oe:terms_signed max_age_days 20``
     - passes if the value of ``oe:terms_signed`` is either a date or a datetime, and is at most 20 days from the
       current datetime. Note that dates with no time component are equivalent to 00:00.00 on the specified date for
       comparison purposes
   * - ``some_group:membership_level >= 2``
     - passes if the value of ``some_group:membership_level`` is a number and is greater to or equal to two.
   * - ``oe:org_type in ['council', 'academic']``
     - passes if the value of ``oe:org_type`` would be considered equal to either ``'council'`` or ``'academic'``
       as if compared with ``is``.
   * - ``oe:member``
     - passes if the value of ``oe:member`` is ``true``.

Specifying multiple conditions
------------------------------

Multiple conditions are separated with ``,`` characters. All conditions must be satisfied for the rule to pass, there
are no sub-clauses or boolean operators. Any number of space characters are allowed before and after the ``,`` in a
condition list.

For example, ``oe:status is 'active', some_group:membership_level >=2`` is the union of those two example conditions
from the previous section and will only be satisfied if both conditions are individually satisfiable.

Capabilities
############

Capability grants for a given set of access conditions are specified as a comma (``,``) separated list of **names**.
There **MUST** be at least one **name** in this list, an empty capability grant list is not considered valid.

Standard capabilities
---------------------

These are capabilities where the namespace part of the **name** is ``oe``, indicating that they are defined as part
of the open energy project. Data providers **SHOULD NOT**, create their own capabilities unless absolutely
necessary as doing so acts against the aim of easy interoperability and comprehension of access and licensing rules.

Any additional capabilities designed **MUST** be prefixed with the organisation ID of the data provider responsible
for their definition, and any such data provider **MUST** publish a clear, legally valid, definition of any such
capabilities. In addition, data providers creating custom capabilities **MUST** inform the |OEGS| of this, providing
links to the aforementioned documentation.

.. warning::

   This section is provisional, the exact final set of base capabilities has yet to be determined. Those shown below
   are a plausible first cut but should not be considered definitive.

.. list-table:: Standard capabilities
   :header-rows: 1
   :widths: 15 15 70

   * - Category
     - Capability name
     - Meaning
   * - **Use**
     -
     - **Use the artefact internally**
   * -
     - ``oe:use_any``
     - For any purpose
   * -
     - ``oe:use_dev``
     - For development purposes only (i.e. private or limited development of new works, products or services)
   * -
     - ``oe:use_noncom``
     - For non-commercial purposes only (e.g. education, research, charity work etc.)
   * - **Adapt**
     -
     - **Adapt the artefact for internal use**
   * -
     - ``oe:adapt_any``
     - For any purpose
   * -
     - ``oe:adapt_dev``
     - For development purposes only (i.e. private or limited development of new works, products or services)
   * -
     - ``oe:adapt_noncom``
     - For non-commercial purposes only (e.g. education, research, charity work etc.)
   * - **Combine**
     -
     - **Combine ('remix') the artefact**
   * -
     - ``oe:combine_any``
     - With any other artefacts
   * -
     - ``oe:combine_external``
     - With other external artefacts
   * -
     - ``oe:combine_internal``
     - With the Data Consumer’s own products or services
   * - **Redistribute**
     -
     - **Redistribute (‘onward share’ - including to any customers of the Service Provider)**
   * -
     - ``oe:redistribute_original``
     - The original artefact
   * -
     - ``oe:redistribute_derived``
     - Derivatives of the original artefact not produced from other data sets, i.e. filtered or cleaned data
   * -
     - ``oe:redistribute_combined``
     - Derivatives of the artefact produced through artefact combination or use in the Data Consumer’s own products or
       services

Expressing Open Data licenses with capabilities
-----------------------------------------------

The capabilities defined above in `Standard capabilities` are intended for :term:`shared data`, but data providers may
also publish :term:`open data`. An open data set by definition has no access conditions, so any access rules for such
data sets **MUST** have an empty access condition list, and must use one of the following capabilities to declare that
the data are licensed under a known OSI approved open license

Rules **MUST NOT** grant a mix of capabilities in the ``open`` namespace and capabilities in other namespaces, as the
semantics of this are not well defined.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Capability name
     - Corresponding open data license
   * - ``open:cc_by_1.0`` ``open:cc_by_2.0`` ``open:cc_by_2.5`` ``open:cc_by_3.0`` ``open:cc_by_4.0``
     - `Creative Commons Attribution <https://creativecommons.org/licenses/by/4.0/>`_ (v1.0, v2.0, v2.5, v3.0, v4.0
       respectively)
   * - ``open:cc_by_sa_1.0`` ``open:cc_by_sa_2.0`` ``open:cc_by_sa_2.5`` ``open:cc_by_sa_3.0`` ``open:cc_by_sa_4.0``
     - `Creative Commons Attribution ShareAlike <https://creativecommons.org/licenses/by-sa/4.0/>`_ (v1.0, v2.0, v2.5,
       v3.0, v4.0 respectively)
   * - ``open:cc0``
     - `Public Domain Dedication <https://creativecommons.org/publicdomain/zero/1.0/>`_ v1.0
   * - ``open:gfdl_1.1`` ``open:gfdl_1.2`` ``open:gfdl_1.3``
     - `GNU Free Documentation License <http://www.gnu.org/copyleft/fdl.html>`_ (v1.1, 1.2, 1.3 respectively)
   * - ``open:fal_1.2`` ``open:fal1.3``
     - `Free Art License <http://artlibre.org/licence/lal/en/>`_ (v1.2, v1.3 respectively)

Open data sets **SHOULD** be released under the latest version of any given license.

Obligations
###########

Obligations are constraints on what the data consumer can do with the data, restricting or specialising the capabilities
granted. They are specified as a single **name**.

Standard obligations
--------------------

.. warning::

   This set of standard obligations is provisional and may be subject to change

.. list-table:: Standard obligations
   :header-rows: 1
   :widths: 10 10 80

   * - Obligation
     - Name
     - Explanation
   * - Fulltext
     - ``oe:ft``
     - Re-users must display the full text of the license every time they use the work
   * - Attribution
     - ``oe:by``
     - Re-users must attribute the work to the original source when they use it
   * - ShareAlike
     - ``oe:sa``
     - Re-users who create derivatives of the work must release the derivatives under the same license as the original
       work, if they choose to distribute the derivatives

.. note::

   Two additional common constraints in existing (mostly open) licenses are NonCommercial and NoDerivatives. These are
   explicitly not included here as it is possible to express this through the access conditions (i.e. rather than
   declaring that a data set is only available for non-commercial usage it is better to say that only non-commercial
   entities may access it). This is not quite equivalent, but simpler and better defined than the relative minefield
   of defining 'non commercial use'.
