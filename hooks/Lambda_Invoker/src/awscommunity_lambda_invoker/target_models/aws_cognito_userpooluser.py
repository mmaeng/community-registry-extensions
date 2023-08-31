# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass

from cloudformation_cli_python_lib.interface import BaseModel
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

import sys
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class AwsCognitoUserpooluser(BaseModel):
    ValidationData: Optional[Sequence["_AttributeType"]]
    UserPoolId: Optional[str]
    Username: Optional[str]
    MessageAction: Optional[str]
    ClientMetadata: Optional[MutableMapping[str, Any]]
    Id: Optional[str]
    DesiredDeliveryMediums: Optional[Sequence[str]]
    ForceAliasCreation: Optional[bool]
    UserAttributes: Optional[Sequence["_AttributeType"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCognitoUserpooluser"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCognitoUserpooluser"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ValidationData=deserialize_list(json_data.get("ValidationData"), AttributeType),
            UserPoolId=json_data.get("UserPoolId"),
            Username=json_data.get("Username"),
            MessageAction=json_data.get("MessageAction"),
            ClientMetadata=json_data.get("ClientMetadata"),
            Id=json_data.get("Id"),
            DesiredDeliveryMediums=json_data.get("DesiredDeliveryMediums"),
            ForceAliasCreation=json_data.get("ForceAliasCreation"),
            UserAttributes=deserialize_list(json_data.get("UserAttributes"), AttributeType),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCognitoUserpooluser = AwsCognitoUserpooluser


@dataclass
class AttributeType(BaseModel):
    Value: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttributeType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttributeType"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttributeType = AttributeType


