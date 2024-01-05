# coding: utf-8

"""
    Pastel Network API Gateway

    Pastel Network’s Gateway provides Web3 developers with easy, robust, and reliable access to the Pastel Network and its underlying protocols via a lightweight, centralized service.<br/> For more information on Pastel Network, review our <a href=https://docs.pastel.network/introduction/pastel-overview>documentation</a>.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UserCreate(BaseModel):
    """
    UserCreate
    """ # noqa: E501
    email: StrictStr
    is_active: Optional[StrictBool] = None
    is_superuser: Optional[StrictBool] = False
    full_name: Optional[StrictStr] = None
    password: StrictStr
    balance_limit: Optional[Union[StrictFloat, StrictInt]] = 0.0
    __properties: ClassVar[List[str]] = ["email", "is_active", "is_superuser", "full_name", "password", "balance_limit"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UserCreate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if is_active (nullable) is None
        # and model_fields_set contains the field
        if self.is_active is None and "is_active" in self.model_fields_set:
            _dict['is_active'] = None

        # set to None if full_name (nullable) is None
        # and model_fields_set contains the field
        if self.full_name is None and "full_name" in self.model_fields_set:
            _dict['full_name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UserCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "email": obj.get("email"),
            "is_active": obj.get("is_active"),
            "is_superuser": obj.get("is_superuser") if obj.get("is_superuser") is not None else False,
            "full_name": obj.get("full_name"),
            "password": obj.get("password"),
            "balance_limit": obj.get("balance_limit") if obj.get("balance_limit") is not None else 0.0
        })
        return _obj

