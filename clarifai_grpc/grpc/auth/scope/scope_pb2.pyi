# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FieldDescriptor as google___protobuf___descriptor___FieldDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    List as typing___List,
    NewType as typing___NewType,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    Union as typing___Union,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
builtin___str = str
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

SValue = typing___NewType('SValue', builtin___int)
type___SValue = SValue
class S(object):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: builtin___int) -> builtin___str: ...
    @classmethod
    def Value(cls, name: builtin___str) -> SValue: ...
    @classmethod
    def keys(cls) -> typing___List[builtin___str]: ...
    @classmethod
    def values(cls) -> typing___List[SValue]: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[builtin___str, SValue]]: ...
    undef = typing___cast(SValue, 0)
    All = typing___cast(SValue, 1)
    Predict = typing___cast(SValue, 2)
    Search = typing___cast(SValue, 3)
    Inputs_Add = typing___cast(SValue, 4)
    Inputs_Get = typing___cast(SValue, 5)
    Inputs_Patch = typing___cast(SValue, 7)
    Inputs_Delete = typing___cast(SValue, 8)
    Outputs_Patch = typing___cast(SValue, 9)
    Concepts_Add = typing___cast(SValue, 10)
    Concepts_Get = typing___cast(SValue, 11)
    Concepts_Patch = typing___cast(SValue, 12)
    Concepts_Delete = typing___cast(SValue, 13)
    Models_Add = typing___cast(SValue, 14)
    Models_Get = typing___cast(SValue, 15)
    Models_Patch = typing___cast(SValue, 16)
    Models_Delete = typing___cast(SValue, 17)
    Models_Train = typing___cast(SValue, 26)
    Models_Sync = typing___cast(SValue, 27)
    Workflows_Add = typing___cast(SValue, 18)
    Workflows_Get = typing___cast(SValue, 19)
    Workflows_Patch = typing___cast(SValue, 20)
    Workflows_Delete = typing___cast(SValue, 21)
    WorkflowMetrics_Get = typing___cast(SValue, 96)
    WorkflowMetrics_Add = typing___cast(SValue, 97)
    WorkflowMetrics_Delete = typing___cast(SValue, 98)
    TSNEVisualizations_Add = typing___cast(SValue, 24)
    TSNEVisualizations_Get = typing___cast(SValue, 25)
    Annotations_Add = typing___cast(SValue, 37)
    Annotations_Get = typing___cast(SValue, 38)
    Annotations_Patch = typing___cast(SValue, 39)
    Annotations_Delete = typing___cast(SValue, 40)
    Collectors_Add = typing___cast(SValue, 41)
    Collectors_Get = typing___cast(SValue, 42)
    Collectors_Delete = typing___cast(SValue, 43)
    Apps_Add = typing___cast(SValue, 44)
    Apps_Get = typing___cast(SValue, 45)
    Apps_Delete = typing___cast(SValue, 46)
    Keys_Add = typing___cast(SValue, 47)
    Keys_Get = typing___cast(SValue, 48)
    Keys_Delete = typing___cast(SValue, 49)
    Collaborators_Add = typing___cast(SValue, 51)
    Collaborators_Get = typing___cast(SValue, 50)
    Collaborators_Delete = typing___cast(SValue, 52)
    Metrics_Add = typing___cast(SValue, 54)
    Metrics_Get = typing___cast(SValue, 53)
    Metrics_Delete = typing___cast(SValue, 63)
    Tasks_Add = typing___cast(SValue, 55)
    Tasks_Get = typing___cast(SValue, 56)
    Tasks_Delete = typing___cast(SValue, 70)
    PasswordPolicies_Add = typing___cast(SValue, 57)
    PasswordPolicies_Get = typing___cast(SValue, 58)
    PasswordPolicies_Delete = typing___cast(SValue, 59)
    LabelOrders_Get = typing___cast(SValue, 67)
    LabelOrders_Add = typing___cast(SValue, 68)
    LabelOrders_Delete = typing___cast(SValue, 69)
    UserFeatureConfigs_Get = typing___cast(SValue, 71)
    FindDuplicateAnnotationsJobs_Add = typing___cast(SValue, 102)
    FindDuplicateAnnotationsJobs_Get = typing___cast(SValue, 103)
    FindDuplicateAnnotationsJobs_Delete = typing___cast(SValue, 104)
    Modules_Add = typing___cast(SValue, 108)
    Modules_Get = typing___cast(SValue, 109)
    Modules_Delete = typing___cast(SValue, 110)
    InstalledModuleVersions_Add = typing___cast(SValue, 111)
    InstalledModuleVersions_Get = typing___cast(SValue, 112)
    InstalledModuleVersions_Delete = typing___cast(SValue, 113)
undef = typing___cast(SValue, 0)
All = typing___cast(SValue, 1)
Predict = typing___cast(SValue, 2)
Search = typing___cast(SValue, 3)
Inputs_Add = typing___cast(SValue, 4)
Inputs_Get = typing___cast(SValue, 5)
Inputs_Patch = typing___cast(SValue, 7)
Inputs_Delete = typing___cast(SValue, 8)
Outputs_Patch = typing___cast(SValue, 9)
Concepts_Add = typing___cast(SValue, 10)
Concepts_Get = typing___cast(SValue, 11)
Concepts_Patch = typing___cast(SValue, 12)
Concepts_Delete = typing___cast(SValue, 13)
Models_Add = typing___cast(SValue, 14)
Models_Get = typing___cast(SValue, 15)
Models_Patch = typing___cast(SValue, 16)
Models_Delete = typing___cast(SValue, 17)
Models_Train = typing___cast(SValue, 26)
Models_Sync = typing___cast(SValue, 27)
Workflows_Add = typing___cast(SValue, 18)
Workflows_Get = typing___cast(SValue, 19)
Workflows_Patch = typing___cast(SValue, 20)
Workflows_Delete = typing___cast(SValue, 21)
WorkflowMetrics_Get = typing___cast(SValue, 96)
WorkflowMetrics_Add = typing___cast(SValue, 97)
WorkflowMetrics_Delete = typing___cast(SValue, 98)
TSNEVisualizations_Add = typing___cast(SValue, 24)
TSNEVisualizations_Get = typing___cast(SValue, 25)
Annotations_Add = typing___cast(SValue, 37)
Annotations_Get = typing___cast(SValue, 38)
Annotations_Patch = typing___cast(SValue, 39)
Annotations_Delete = typing___cast(SValue, 40)
Collectors_Add = typing___cast(SValue, 41)
Collectors_Get = typing___cast(SValue, 42)
Collectors_Delete = typing___cast(SValue, 43)
Apps_Add = typing___cast(SValue, 44)
Apps_Get = typing___cast(SValue, 45)
Apps_Delete = typing___cast(SValue, 46)
Keys_Add = typing___cast(SValue, 47)
Keys_Get = typing___cast(SValue, 48)
Keys_Delete = typing___cast(SValue, 49)
Collaborators_Add = typing___cast(SValue, 51)
Collaborators_Get = typing___cast(SValue, 50)
Collaborators_Delete = typing___cast(SValue, 52)
Metrics_Add = typing___cast(SValue, 54)
Metrics_Get = typing___cast(SValue, 53)
Metrics_Delete = typing___cast(SValue, 63)
Tasks_Add = typing___cast(SValue, 55)
Tasks_Get = typing___cast(SValue, 56)
Tasks_Delete = typing___cast(SValue, 70)
PasswordPolicies_Add = typing___cast(SValue, 57)
PasswordPolicies_Get = typing___cast(SValue, 58)
PasswordPolicies_Delete = typing___cast(SValue, 59)
LabelOrders_Get = typing___cast(SValue, 67)
LabelOrders_Add = typing___cast(SValue, 68)
LabelOrders_Delete = typing___cast(SValue, 69)
UserFeatureConfigs_Get = typing___cast(SValue, 71)
FindDuplicateAnnotationsJobs_Add = typing___cast(SValue, 102)
FindDuplicateAnnotationsJobs_Get = typing___cast(SValue, 103)
FindDuplicateAnnotationsJobs_Delete = typing___cast(SValue, 104)
Modules_Add = typing___cast(SValue, 108)
Modules_Get = typing___cast(SValue, 109)
Modules_Delete = typing___cast(SValue, 110)
InstalledModuleVersions_Add = typing___cast(SValue, 111)
InstalledModuleVersions_Get = typing___cast(SValue, 112)
InstalledModuleVersions_Delete = typing___cast(SValue, 113)
type___S = S

class ScopeList(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    scopes: google___protobuf___internal___containers___RepeatedScalarFieldContainer[type___SValue] = ...
    endpoints: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...

    def __init__(self,
        *,
        scopes : typing___Optional[typing___Iterable[type___SValue]] = None,
        endpoints : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ScopeList: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ScopeList: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"endpoints",b"endpoints",u"scopes",b"scopes"]) -> None: ...
type___ScopeList = ScopeList

clarfai_exposed: google___protobuf___descriptor___FieldDescriptor = ...

clarifai_depending_scopes: google___protobuf___descriptor___FieldDescriptor = ...
