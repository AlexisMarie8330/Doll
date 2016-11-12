"""Generated message classes for runtimeconfig version v1beta1.

Provides capabilities for dynamic configuration and coordination for
applications running on Google Cloud Platform.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'runtimeconfig'


class Cardinality(_messages.Message):
  """A Cardinality condition for the Waiter resource. A cardinality condition
  is met when the number of variables under a specified path prefix reaches a
  predefined number. For example, if you set a Cardinality condition where the
  `path` is set to `/foo` and the number of paths is set to 2, the following
  variables would meet the condition in a RuntimeConfig resource:  +
  `/foo/variable1 = "value1"` + `/foo/variable2 = "value2"` + `/bar/variable3
  = "value3"`  It would not would not satisify the same condition with the
  `number` set to 3, however, because there is only 2 paths that start with
  `/foo`. Cardinality conditions are recursive; all subtrees under the
  specific path prefix are counted.

  Fields:
    number: The number variables under the `path` that must exist to meet this
      condition. Defaults to 1 if not specified.
    path: The root of the variable subtree to monitor. For example, `/foo`.
  """

  number = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  path = _messages.StringField(2)


class Empty(_messages.Message):
  """A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance:      service Foo {
  rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);     }  The
  JSON representation for `Empty` is empty JSON object `{}`.
  """



class EndCondition(_messages.Message):
  """The condition that a Waiter resource is waiting for.

  Fields:
    cardinality: The cardinality of the `EndCondition`.
  """

  cardinality = _messages.MessageField('Cardinality', 1)


class ListConfigsResponse(_messages.Message):
  """`ListConfigs()` returns the following response. The order of returned
  objects is arbitrary; that is, it is not ordered in any particular way.

  Fields:
    configs: A list of the configurations in the project. The order of
      returned objects is arbitrary; that is, it is not ordered in any
      particular way.
    nextPageToken: This token allows you to get the next page of results for
      list requests. If the number of results is larger than `pageSize`, use
      the `nextPageToken` as a value for the query parameter `pageToken` in
      the next list request. Subsequent list requests will have their own
      `nextPageToken` to continue paging through the results
  """

  configs = _messages.MessageField('RuntimeConfig', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListVariablesResponse(_messages.Message):
  """Response for the `ListVariables()` method.

  Fields:
    nextPageToken: This token allows you to get the next page of results for
      list requests. If the number of results is larger than `pageSize`, use
      the `nextPageToken` as a value for the query parameter `pageToken` in
      the next list request. Subsequent list requests will have their own
      `nextPageToken` to continue paging through the results
    variables: A list of variables and their values. The order of returned
      variable objects is arbitrary.
  """

  nextPageToken = _messages.StringField(1)
  variables = _messages.MessageField('Variable', 2, repeated=True)


class ListWaitersResponse(_messages.Message):
  """Response for the `ListWaiters()` method. Order of returned waiter objects
  is arbitrary.

  Fields:
    nextPageToken: This token allows you to get the next page of results for
      list requests. If the number of results is larger than `pageSize`, use
      the `nextPageToken` as a value for the query parameter `pageToken` in
      the next list request. Subsequent list requests will have their own
      `nextPageToken` to continue paging through the results
    waiters: Found waiters in the project.
  """

  nextPageToken = _messages.StringField(1)
  waiters = _messages.MessageField('Waiter', 2, repeated=True)


class Operation(_messages.Message):
  """This resource represents a long-running operation that is the result of a
  network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation.
      It typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal response of the operation in case of success.
      If the original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If true, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation.  It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should have the format of `operations/some/unique/name`.
    response: The normal response of the operation in case of success.  If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    """Service-specific metadata associated with the operation.  It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata.  Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    """The normal response of the operation in case of success.  If the
    original method returns no data on success, such as `Delete`, the response
    is `google.protobuf.Empty`.  If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource.  For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name.  For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('Status', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class RuntimeConfig(_messages.Message):
  """A RuntimeConfig resource is the primary resource in the Cloud
  RuntimeConfig service. A RuntimeConfig resource consists of metadata and a
  hierarchy of variables.

  Fields:
    description: An optional description of the RuntimeConfig object. The
      length of the description must be less than 256 bytes.
    name: The resource name of a runtime config. The name must have the
      format:      projects/[PROJECT_ID]/configs/[CONFIG_NAME]  The
      `[PROJECT_ID]` must be a valid project ID, and `[CONFIG_NAME]` is an
      arbitrary name that matches RFC 1035 segment specification. The length
      of `[CONFIG_NAME]` must be less than 64 bytes.  You pick the
      RuntimeConfig resource name, but the server will validate that the name
      adheres to this format. After you create the resource, you cannot change
      the resource's name.
  """

  description = _messages.StringField(1)
  name = _messages.StringField(2)


class RuntimeconfigProjectsConfigsCreateRequest(_messages.Message):
  """A RuntimeconfigProjectsConfigsCreateRequest object.

  Fields:
    projectsId: Part of `parent`. The [project ID](https://support.google.com/
      cloud/answer/6158840?hl=en&ref_topic=6158848) for this request, in the
      format `projects/[PROJECT_ID]`.
    requestId: An optional unique request_id. If server receives two Create
      requests with the same request_id then second request will be ignored
      and the resource stored in the backend will be returned. Empty
      request_id fields are ignored. It is responsibility of the client to
      ensure uniqueness of the request_id strings. The strings are limited to
      64 characters.
    runtimeConfig: A RuntimeConfig resource to be passed as the request body.
  """

  projectsId = _messages.StringField(1, required=True)
  requestId = _messages.StringField(2)
  runtimeConfig = _messages.MessageField('RuntimeConfig', 3)


class RuntimeconfigProjectsConfigsDeleteRequest(_messages.Message):
  """A RuntimeconfigProjectsConfigsDeleteRequest object.

  Fields:
    configsId: Part of `name`. See documentation of `projectsId`.
    projectsId: Part of `name`. The RuntimeConfig resource to delete, in the
      format:  `projects/[PROJECT_ID]/configs/[CONFIG_NAME]`
  """

  configsId = _messages.StringField(1, required=True)
  projectsId = _messages.StringField(2, required=True)


class RuntimeconfigProjectsConfigsGetRequest(_messages.Message):
  """A RuntimeconfigProjectsConfigsGetRequest object.

  Fields:
    configsId: Part of `name`. See documentation of `projectsId`.
    projectsId: Part of `name`. The name of the RuntimeConfig resource to
      retrieve, in the format:  `projects/[PROJECT_ID]/configs/[CONFIG_NAME]`
  """

  configsId = _messages.StringField(1, required=True)
  projectsId = _messages.StringField(2, required=True)


class RuntimeconfigProjectsConfigsListRequest(_messages.Message):
  """A RuntimeconfigProjectsConfigsListRequest object.

  Fields:
    pageSize: Specifies the number of results to return per page. If there are
      fewer elements than the specified number, returns all elements.
    pageToken: Specifies a page token to use. Set `pageToken` to a
      `nextPageToken` returned by a previous list request to get the next page
      of results.
    projectsId: Part of `parent`. The [project ID](https://support.google.com/
      cloud/answer/6158840?hl=en&ref_topic=6158848) for this request, in the
      format `projects/[PROJECT_ID]`.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  projectsId = _messages.StringField(3, required=True)


class RuntimeconfigProjectsConfigsOperationsGetRequest(_messages.Message):
  """A RuntimeconfigProjectsConfigsOperationsGetRequest object.

  Fields:
    configsId: Part of `name`. See documentation of `projectsId`.
    operationsId: Part of `name`. See documentation of `projectsId`.
    projectsId: Part of `name`. The name of the operation resource.
  """

  configsId = _messages.StringField(1, required=True)
  operationsId = _messages.StringField(2, required=True)
  projectsId = _messages.StringField(3, required=True)


class RuntimeconfigProjectsConfigsUpdateRequest(_messages.Message):
  """A RuntimeconfigProjectsConfigsUpdateRequest object.

  Fields:
    configsId: Part of `name`. See documentation of `projectsId`.
    projectsId: Part of `name`. The name of the RuntimeConfig resource to
      update, in the format:  `projects/[PROJECT_ID]/configs/[CONFIG_NAME]`
    runtimeConfig: A RuntimeConfig resource to be passed as the request body.
  """

  configsId = _messages.StringField(1, required=True)
  projectsId = _messages.StringField(2, required=True)
  runtimeConfig = _messages.MessageField('RuntimeConfig', 3)


class RuntimeconfigProjectsConfigsVariablesCreateRequest(_messages.Message):
  """A RuntimeconfigProjectsConfigsVariablesCreateRequest object.

  Fields:
    configsId: Part of `parent`. See documentation of `projectsId`.
    projectsId: Part of `parent`. The path to the RutimeConfig resource that
      this variable should belong to. The configuration must exist beforehand;
      the path must by in the format:
      `projects/[PROJECT_ID]/configs/[CONFIG_NAME]`
    requestId: An optional unique request_id. If server receives two Create
      requests with the same request_id then second request will be ignored
      and the resource stored in the backend will be returned. Empty
      request_id fields are ignored. It is responsibility of the client to
      ensure uniqueness of the request_id strings. The strings are limited to
      64 characters.
    variable: A Variable resource to be passed as the request body.
  """

  configsId = _messages.StringField(1, required=True)
  projectsId = _messages.StringField(2, required=True)
  requestId = _messages.StringField(3)
  variable = _messages.MessageField('Variable', 4)


class RuntimeconfigProjectsConfigsVariablesDeleteRequest(_messages.Message):
  """A RuntimeconfigProjectsConfigsVariablesDeleteRequest object.

  Fields:
    configsId: Part of `name`. See documentation of `projectsId`.
    projectsId: Part of `name`. The name of the variable to delete, in the
      format:
      `projects/[PROJECT_ID]/configs/[CONFIG_NAME]/variables/[VARIABLE_NAME]`
    recursive: Set to `true` to recursively delete multiple variables with the
      same prefix.
    variablesId: Part of `name`. See documentation of `projectsId`.
  """

  configsId = _messages.StringField(1, required=True)
  projectsId = _messages.StringField(2, required=True)
  recursive = _messages.BooleanField(3)
  variablesId = _messages.StringField(4, required=True)


class RuntimeconfigProjectsConfigsVariablesGetRequest(_messages.Message):
  """A RuntimeconfigProjectsConfigsVariablesGetRequest object.

  Fields:
    configsId: Part of `name`. See documentation of `projectsId`.
    projectsId: Part of `name`. The name of the variable to return, in the
      format:
      `projects/[PROJECT_ID]/configs/[CONFIG_NAME]/variables/[VARIBLE_NAME]`
    variablesId: Part of `name`. See documentation of `projectsId`.
  """

  configsId = _messages.StringField(1, required=True)
  projectsId = _messages.StringField(2, required=True)
  variablesId = _messages.StringField(3, required=True)


class RuntimeconfigProjectsConfigsVariablesListRequest(_messages.Message):
  """A RuntimeconfigProjectsConfigsVariablesListRequest object.

  Fields:
    configsId: Part of `parent`. See documentation of `projectsId`.
    filter: Filters variables by matching the specified filter. For example:
      `projects/example-project/config/[CONFIG_NAME]/variables/example-
      variable`.
    pageSize: Specifies the number of results to return per page. If there are
      fewer elements than the specified number, returns all elements.
    pageToken: Specifies a page token to use. Set `pageToken` to a
      `nextPageToken` returned by a previous list request to get the next page
      of results.
    projectsId: Part of `parent`. The path to the RuntimeConfig resource for
      which you want to list variables. The configuration must exist
      beforehand; the path must by in the format:
      `projects/[PROJECT_ID]/configs/[CONFIG_NAME]`
  """

  configsId = _messages.StringField(1, required=True)
  filter = _messages.StringField(2)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)
  projectsId = _messages.StringField(5, required=True)


class RuntimeconfigProjectsConfigsVariablesUpdateRequest(_messages.Message):
  """A RuntimeconfigProjectsConfigsVariablesUpdateRequest object.

  Fields:
    configsId: Part of `name`. See documentation of `projectsId`.
    projectsId: Part of `name`. The name of the variable to update, in the
      format:
      `projects/[PROJECT_ID]/configs/[CONFIG_NAME]/variables/[VARIABLE_NAME]`
    variable: A Variable resource to be passed as the request body.
    variablesId: Part of `name`. See documentation of `projectsId`.
  """

  configsId = _messages.StringField(1, required=True)
  projectsId = _messages.StringField(2, required=True)
  variable = _messages.MessageField('Variable', 3)
  variablesId = _messages.StringField(4, required=True)


class RuntimeconfigProjectsConfigsVariablesWatchRequest(_messages.Message):
  """A RuntimeconfigProjectsConfigsVariablesWatchRequest object.

  Fields:
    configsId: Part of `name`. See documentation of `projectsId`.
    projectsId: Part of `name`. The name of the variable to watch, in the
      format:  `projects/[PROJECT_ID]/configs/[CONFIG_NAME]`
    variablesId: Part of `name`. See documentation of `projectsId`.
    watchVariableRequest: A WatchVariableRequest resource to be passed as the
      request body.
  """

  configsId = _messages.StringField(1, required=True)
  projectsId = _messages.StringField(2, required=True)
  variablesId = _messages.StringField(3, required=True)
  watchVariableRequest = _messages.MessageField('WatchVariableRequest', 4)


class RuntimeconfigProjectsConfigsWaitersCreateRequest(_messages.Message):
  """A RuntimeconfigProjectsConfigsWaitersCreateRequest object.

  Fields:
    configsId: Part of `parent`. See documentation of `projectsId`.
    projectsId: Part of `parent`. The path to the configuration that will own
      the waiter. The configuration must exist beforehand; the path must by in
      the format:  `projects/[PROJECT_ID]/configs/[CONFIG_NAME]`.
    requestId: An optional unique request_id. If server receives two Create
      requests with the same request_id then second request will be ignored
      and information stored in the backend will be returned. Empty request_id
      fields are ignored. It is responsibility of the client to ensure
      uniqueness of the request_id strings. The strings are limited to 64
      characters.
    waiter: A Waiter resource to be passed as the request body.
  """

  configsId = _messages.StringField(1, required=True)
  projectsId = _messages.StringField(2, required=True)
  requestId = _messages.StringField(3)
  waiter = _messages.MessageField('Waiter', 4)


class RuntimeconfigProjectsConfigsWaitersDeleteRequest(_messages.Message):
  """A RuntimeconfigProjectsConfigsWaitersDeleteRequest object.

  Fields:
    configsId: Part of `name`. See documentation of `projectsId`.
    projectsId: Part of `name`. The Waiter resource to delete, in the format:
      `projects/[PROJECT_ID]/configs/[CONFIG_NAME]/waiters/[WAITER_NAME]`
    waitersId: Part of `name`. See documentation of `projectsId`.
  """

  configsId = _messages.StringField(1, required=True)
  projectsId = _messages.StringField(2, required=True)
  waitersId = _messages.StringField(3, required=True)


class RuntimeconfigProjectsConfigsWaitersGetRequest(_messages.Message):
  """A RuntimeconfigProjectsConfigsWaitersGetRequest object.

  Fields:
    configsId: Part of `name`. See documentation of `projectsId`.
    projectsId: Part of `name`. The fully-qualified name of the Waiter
      resource object to retrieve, in the format:
      `projects/[PROJECT_ID]/configs/[CONFIG_NAME]/waiters/[WAITER_NAME]`
    waitersId: Part of `name`. See documentation of `projectsId`.
  """

  configsId = _messages.StringField(1, required=True)
  projectsId = _messages.StringField(2, required=True)
  waitersId = _messages.StringField(3, required=True)


class RuntimeconfigProjectsConfigsWaitersListRequest(_messages.Message):
  """A RuntimeconfigProjectsConfigsWaitersListRequest object.

  Fields:
    configsId: Part of `parent`. See documentation of `projectsId`.
    pageSize: Specifies the number of results to return per page. If there are
      fewer elements than the specified number, returns all elements.
    pageToken: Specifies a page token to use. Set `pageToken` to a
      `nextPageToken` returned by a previous list request to get the next page
      of results.
    projectsId: Part of `parent`. The path to the configuration for which you
      want to get a list of waiters. The configuration must exist beforehand;
      the path must by in the format:
      `projects/[PROJECT_ID]/configs/[CONFIG_NAME]`
  """

  configsId = _messages.StringField(1, required=True)
  pageSize = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(3)
  projectsId = _messages.StringField(4, required=True)


class StandardQueryParameters(_messages.Message):
  """Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    bearer_token: OAuth bearer token.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    pp: Pretty-print response.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    """Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    """V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  bearer_token = _messages.StringField(4)
  callback = _messages.StringField(5)
  fields = _messages.StringField(6)
  key = _messages.StringField(7)
  oauth_token = _messages.StringField(8)
  pp = _messages.BooleanField(9, default=True)
  prettyPrint = _messages.BooleanField(10, default=True)
  quotaUser = _messages.StringField(11)
  trace = _messages.StringField(12)
  uploadType = _messages.StringField(13)
  upload_protocol = _messages.StringField(14)


class Status(_messages.Message):
  """The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). The error model is designed to be:
  - Simple to use and understand for most users - Flexible enough to meet
  unexpected needs  # Overview  The `Status` message contains three pieces of
  data: error code, error message, and error details. The error code should be
  an enum value of google.rpc.Code, but it may accept additional error codes
  if needed.  The error message should be a developer-facing English message
  that helps developers *understand* and *resolve* the error. If a localized
  user-facing error message is needed, put the localized message in the error
  details or localize it in the client. The optional error details may contain
  arbitrary information about the error. There is a predefined set of error
  detail types in the package `google.rpc` which can be used for common error
  conditions.  # Language mapping  The `Status` message is the logical
  representation of the error model, but it is not necessarily the actual wire
  format. When the `Status` message is exposed in different client libraries
  and different wire protocols, it can be mapped differently. For example, it
  will likely be mapped to some exceptions in Java, but more likely mapped to
  some error codes in C.  # Other uses  The error model and the `Status`
  message can be used in a variety of environments, either with or without
  APIs, to provide a consistent developer experience across different
  environments.  Example uses of this error model include:  - Partial errors.
  If a service needs to return partial errors to the client,     it may embed
  the `Status` in the normal response to indicate the partial     errors.  -
  Workflow errors. A typical workflow has multiple steps. Each step may
  have a `Status` message for error reporting purpose.  - Batch operations. If
  a client uses batch request and batch response, the     `Status` message
  should be used directly inside batch response, one for     each error sub-
  response.  - Asynchronous operations. If an API call embeds asynchronous
  operation     results in its response, the status of those operations should
  be     represented directly using the `Status` message.  - Logging. If some
  API errors are stored in logs, the message `Status` could     be used
  directly after any stripping needed for security/privacy reasons.

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details.  There will be a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    """A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


class Variable(_messages.Message):
  """Describes a single variable within a RuntimeConfig resource. The name
  denotes the hierarchical variable name. For example, `ports/serving_port` is
  a valid variable name. The variable value is an opaque string and only leaf
  variables can have values (that is, variables that do not have any child
  variables).

  Enums:
    StateValueValuesEnum: [Ouput only] The current state of the variable. The
      variable state indicates the outcome of the `variables().watch` call and
      is visible through the `get` and `list` calls.

  Fields:
    name: The name of the variable resource, in the format:
      projects/[PROJECT_ID]/configs/[CONFIG_NAME]/variables/[VARIABLE_NAME]
      The `[PROJECT_ID]` must be a valid project ID, `[CONFIG_NAME]` must be a
      valid RuntimeConfig reource and `[VARIABLE_NAME]` follows Unix file
      system file path naming.  The `[VARIABLE_NAME]` can contain ASCII
      letters, numbers, slashes and dashes. Slashes are used as path element
      separators and are not part of the `[VARIABLE_NAME]` itself, so
      `[VARIABLE_NAME]` must contain at least one non-slash character.
      Multiple slashes are coalesced into single slash character. Each path
      segment should follow RFC 1035 segment specification. The length of a
      `[VARIABLE_NAME]` must be less than 256 bytes.  Once you create a
      variable, you cannot change the variable name.
    state: [Ouput only] The current state of the variable. The variable state
      indicates the outcome of the `variables().watch` call and is visible
      through the `get` and `list` calls.
    text: The textual value of the variable. The length of the value must be
      less than 4096 bytes. Empty values are also accepted. NB: Only one of
      value and string_value can be set at the same time.
    updateTime: [Output Only] The time of the last variable update.
    value: The binary value of the variable. The length of the value must be
      less than 4096 bytes. Empty values are also accepted. The value must be
      Base64 encoded. NB: Only one of value and string_value can be set at the
      same time.
  """

  class StateValueValuesEnum(_messages.Enum):
    """[Ouput only] The current state of the variable. The variable state
    indicates the outcome of the `variables().watch` call and is visible
    through the `get` and `list` calls.

    Values:
      VARIABLE_STATE_UNSPECIFIED: Default variable state.
      UPDATED: The variable was updated, while `variables().watch` was
        executing.
      DELETED: The variable was deleted, while `variables().watch` was
        executing.
    """
    VARIABLE_STATE_UNSPECIFIED = 0
    UPDATED = 1
    DELETED = 2

  name = _messages.StringField(1)
  state = _messages.EnumField('StateValueValuesEnum', 2)
  text = _messages.StringField(3)
  updateTime = _messages.StringField(4)
  value = _messages.BytesField(5)


class Waiter(_messages.Message):
  """A Waiter resource waits for some end condition within a RuntimeConfig
  resource to be met before it returns. For example, assume you have a
  distributed system where each node writes to a Variable resource
  indidicating the node's readiness as part of the startup process.  You then
  configure a Waiter resource with the success condition set to wait until
  some number of nodes have checked in. Afterwards, your application runs some
  arbitrary code after the condition has been met and the waiter returns
  successfully.  Once created, a Waiter resource is immutable.  To learn more
  about using waiters, read the [Creating a Waiter](/deployment-manager
  /runtime-configurator/creating-a-waiter) documentation.

  Fields:
    createTime: [Output Only] The instant at which this Waiter resource was
      created. Adding the value of `timeout` to this instant yields the
      timeout deadline for the waiter.
    done: [Output Only] If the value is `false`, it means the waiter is still
      waiting for one of its conditions to be met.  If true, the waiter has
      finished. If the waiter finished due to a timeout or failure, `error`
      will be set.
    error: [Output Only] If the waiter ended due to a failure or timeout, this
      value will be set.
    failure: [Optional] The failure condition of this waiter. If this
      condition is met, `done` will be set to `true` and the `error` code will
      be set to `ABORTED`. The failure condition takes precedence over the
      success condition. If both conditions are met, a failure will be
      indicated. This value is optional; if no failure condition is set, the
      only failure scenario will be a timeout.
    name: The name of the Waiter resource, in the format:
      projects/[PROJECT_ID]/configs/[CONFIG_NAME]/waiters/[WAITER_NAME]  The
      `[PROJECT_ID]` must be a valid Google Cloud project ID, the
      `[CONFIG_NAME]` must be a valid RuntimeConfig resource, the
      `[WAITER_NAME]` must match RFC 1035 segment specification, and the
      length of `[WAITER_NAME]` must be less than 64 bytes.  After you create
      a Waiter resource, you cannot change the resource name.
    success: [Required] The success condition. If this condition is met,
      `done` will be set to `true` and the `error` value will remain unset.
      The failure condition takes precedence over the success condition. If
      both conditions are met, a failure will be indicated.
    timeout: [Required] Specifies the timeout of the waiter in seconds,
      beginning from the instant that `waiters().create` method is called. If
      this time elapses before the success or failure conditions are met, the
      waiter fails and sets the `error` code to `DEADLINE_EXCEEDED`.
  """

  createTime = _messages.StringField(1)
  done = _messages.BooleanField(2)
  error = _messages.MessageField('Status', 3)
  failure = _messages.MessageField('EndCondition', 4)
  name = _messages.StringField(5)
  success = _messages.MessageField('EndCondition', 6)
  timeout = _messages.StringField(7)


class WatchVariableRequest(_messages.Message):
  """Request for the `WatchVariable()` method.

  Fields:
    newerThan: If specified, checks the current timestamp of the variable and
      if the current timestamp is newer than `newerThan` timestamp, the method
      returns immediately.  If not specified or the variable has an older
      timestamp, the watcher waits for a the value to change before returning.
  """

  newerThan = _messages.StringField(1)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv',
    package=u'runtimeconfig')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1',
    package=u'runtimeconfig')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2',
    package=u'runtimeconfig')
