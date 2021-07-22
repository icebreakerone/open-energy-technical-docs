Common Security Requirements
============================

.. include:: /rfc2119.txt

.. contents::
   :depth: 4
   :local:

Open Energy defines a security and trust model for shared data APIs. Three
parties are involved in each shared data request:

1. The |DC| wishing to access the :term:`shared data` |API|
2. The :term:`authorization` server, as part of the governance service (|OEGS|), with knowledge about the
   |DC| as represented by an organisation account within the |OEGS|
3. The |DP| responsible for supplying shared data through its shared data API

The interactions are shown graphically below in the form of a sequence diagram.

.. figure:: images/FAPI_sequence_diagram.svg
    :name: fapi_interactions_image

    FAPI Sequence Diagram - client credentials flow

Applicable standards
--------------------

We use a strict sub-set of the |FAPI| specification for interactions between |DPs| and |DCs|. The
applicable standards are linked here for reference, we reference the precise elements of these standards in later
sections.

* `RFC6749 The OAuth 2.0 Authorization Framework <https://datatracker.ietf.org/doc/html/rfc6749>`_
* `RFC6750 The OAuth 2.0 Authorization Framework: Bearer Token Usage <https://datatracker.ietf.org/doc/html/rfc6750>`_
* `OpenID Connect Core 1.0 <https://openid.net/specs/openid-connect-core-1_0.html>`_
* `RFC8705 OAuth 2.0 Mutual-TLS Client Authentication and Certificate-Bound Access Tokens <https://www.rfc-editor.org/rfc/rfc8705.html>`_

Discovery of endpoint URLs
##########################

While not strictly necessary, the authorization server deployed as part of the |OEGS| implements the OpenID Connect
Discovery provider configuration information endpoint as described
`here <https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderConfig>`_, references in this document to
e.g. ``token_endpoint`` refer to properties discoverable in this fashion.

Token acquisition
-----------------

In order to access a shared data API, a |DC| must first acquire an access token. This is done by sending an
HTTP request to the authorization server (part of the |OEGS|). The |DC| **MUST**:

* Use Mutual TLS, presenting a client certificate when requested. This is the ``tls_client_auth`` authentication method
  described in section `2 of RFC8705 <https://www.rfc-editor.org/rfc/rfc8705.html#name-mutual-tls-for-oauth-client>`_

    * In our implementation, this certificate is acquired by creating a ``transport certificate`` in a
      ``software statement`` within the |OEGS| directory

* Use the ``client_credentials`` grant type

* Send a ``POST`` request to the ``token_endpoint`` of the authorization server containing the following properties
  as ``application/x-www-form-urlencoded`` key / value pairs::

    client_id : <CLIENT_ID>
    scope: <REQUESTED_SCOPES>
    grant_type: client_credentials

  Scope may be omitted, for most uses within Open Energy there is no requirement to specify a scope. ``CLIENT_ID`` can
  be obtained from the ``software statement`` within the directory corresponding to this client

A successful call to the ``token_endpoint`` is indicated by a ``200`` response code, in which case the body of the
response will contain a JSON object with at least two properties:

1. ``access_token`` is an opaque string to be used as a bearer token for requests to resource servers
   (a |DC| :term:`shared data` |API| in our context)
2. ``expires_in`` is an integer number of seconds from the current time, after which the token will no longer be valid
   - after this point the |DC| **MUST** request a new token in order to continue to access shared data resources

Token usage - calling a shared data API
---------------------------------------

To call a shared data API within a |DP|, the |DC| MUST:

* Use Mutual TLS as previously described
* Pass the previously acquired bearer token in an HTTP header::

    Authorization: Bearer <TOKEN>

In addition, the |DC| **SHOULD**:

* Specify an interaction ID for this call in an HTTP header::

    x-fapi-interaction-id: <UUID>

  This allows for tracking of transactions between clients and resource servers, aiding troubleshooting. We use a UUID4
  in our reference implementation

Request validation
------------------

To participate in the Open Energy ecosystem, a |DP| **MUST**:

* Expose an HTTPS API
* Perform validation on any requests to this API

  * Reject any requests which do not present a valid client certificate. Client certificates are validated in the
    context of the root CAs provided by the |OEGS| directory.
  * Reject any requests which do not provide an ``Authorization`` header containing a ``Bearer`` token as described
    above

If any of the above checks fail, the |DP| **MUST NOT** continue processing the request, and **SHOULD** respond with
an error response as defined in `this section <https://datatracker.ietf.org/doc/html/rfc6750#section-6.2>`_ of RFC6750

Token introspection
###################

If all the above checks pass, the |DP| **MUST** then validate the presented token. Tokens in our case are opaque
identifiers (as opposed to JWTs) and must be passed to the ``introspection_endpoint`` of the authorization server to
obtain additional information. To obtain this introspection response, the |DP| **MUST**:

* Make a ``POST`` request to the ``introspection_endpoint`` of the authorization server
* Use Mutual TLS, this means |DPs| must also have a provisioned client within the |OEGS| directory in the form
  of a ``software statement`` and corresponding transport certificate
* Send the bearer token and client ID of the |DP| as an ``application/x-www-form-urlencoded`` body with the
  following values::

    token: <BEARER_TOKEN>
    client_id: <CLIENT_ID>

Introspection response validation
#################################

The response body of this introspection call contains a JSON object with information about the entity which requested
the supplied token from the authorization server, as well as properties of the token itself. An example introspection
response is shown below:

.. code-block:: json

    {
      "active": true,
      "organisation_id": "8",
      "organisation_name": "A Demo Provider",
      "organisation_number": "8",
      "software_roles": [
        "EDSP_L1"
      ],
      "software_description": "Description: https://www.demo.org.uk/ is the location of our demo server",
      "additional_software_metadata": {
        "metadata": {
          "something": "something else"
        }
      },
      "client_id": "kZuAsn7UyZ98Wwh29hDpf",
      "exp": 1626279245,
      "iat": 1626278645,
      "iss": "https://auth.directory.energydata.org.uk",
      "scope": "directory:software",
      "cnf": {
        "x5t#S256": "rP_-9u3ZyVo4ryQxg-bn4rr6gJGNu1dTowEeppOuIt8"
      },
      "token_type": "Bearer"
    }


The following elements of the introspection response **MUST** be validated further before any Open Energy specific
processing is performed:

active
++++++

If the introspection response does not contain the key ``active``, or the value of this key is anything other than the
boolean ``true`` value, the |DP| **MUST** reject the request and cease further processing.

If the ``active`` key was not present, it **SHOULD** respond with ``400 invalid_request``

If the ``active`` key was present but not ``true`` it **SHOULD** respond with ``401 invalid_token``

time ranges
+++++++++++

If the introspection response contains ``iat`` this is interpreted as a number of seconds since the epoch at which the
token was issued. If this is in the future the |DP| **MUST** reject the request and cease further processing. It
SHOULD respond with a ``401 invalid_token``.

.. note::

    The |DP| **SHOULD** allow for a reasonable degree of clock skew when interpreting the ``iat`` timestamp, an
    allowance of no more than 10 seconds should cover all reasonable cases.

If the introspection response contains ``exp`` this is interpreted as a number of seconds since the epoch after which
the token should be considered invalid. If this is in the past, the |DP| **MUST** reject the request and cease
further processing. It **SHOULD** respond with a ``401 invalid_token``

certificate thumbprint
++++++++++++++++++++++

Open Energy uses certificate pinning combined with MTLS on all requests between |DCs| and |DPs|. This
ensures that a token issued to one client cannot be re-used by another client. |DPs| **MUST** check that the
thumbprint of the presented client certificate matches that provided within the introspection response.

The introspection response contains the SHA256 thumbprint of the certificate used to acquire the token as a nested
property ``['cnf']['x5t#S256']``. This **MUST** be equal to the SHA256 thumbprint of the client certificate, if this is
not the case the |DP| **MUST** reject the request and cease any further processing, responding with a
``401 invalid_token``

Interaction header
##################

If the ``x-fapi-interaction-id`` header is set in the request, it **MUST** be set to the same value in the response
header of the same name. If not set, a new ID **MUST** be generated and set in the response header.

Other validation
################

If all the above checks have passed, the |DP| can service the request and return whatever data were requested.
It **MAY**, however, apply additional checks based on information in the introspection response about the client. This
is where any Open Energy specific access control and licensing policies are applied.

To inform any additional processing, the |DP| **MAY** make use of the
``['additional_client_metadata']['metadata']`` key within the introspection response. This contains a JSON object with
properties asserted about the |DC|. The exact set of properties is not defined here, please see the access
control language specification for more information about what could be specified.

|DPs| **MAY** make use of the ``organisation_id`` field in the token introspection response to uniquely and consistently
identify the organisation of the |DC| where required, for example to reference a customer record within the |DP|.

More information on the Open Energy specific access control language can be found in
`Access Control and Capability Grant Language`, and its expression in the metadata file at `Data Set Metadata` in the
`Access Block` section.

