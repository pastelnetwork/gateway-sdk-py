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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pastel_gateway_sdk.models.collection_registration_result_status_messages_inner import CollectionRegistrationResultStatusMessagesInner
from pastel_gateway_sdk.models.status import Status
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ResultRegistrationResult(BaseModel):
    """
    ResultRegistrationResult
    """ # noqa: E501
    result_status: Status
    file_name: Optional[StrictStr] = None
    file_type: Optional[StrictStr] = None
    file_id: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    last_updated_at: Optional[datetime] = None
    status_messages: Optional[List[CollectionRegistrationResultStatusMessagesInner]] = None
    retry_num: Optional[StrictInt] = None
    registration_ticket_txid: Optional[StrictStr] = None
    activation_ticket_txid: Optional[StrictStr] = None
    original_file_ipfs_link: Optional[StrictStr] = None
    stored_file_ipfs_link: Optional[StrictStr] = None
    stored_file_aws_link: Optional[StrictStr] = None
    stored_file_other_links: Optional[Dict[str, Any]] = None
    make_publicly_accessible: Optional[StrictBool] = None
    offer_ticket_txid: Optional[StrictStr] = None
    offer_ticket_intended_rcpt_pastel_id: Optional[StrictStr] = None
    error: Optional[StrictStr] = None
    result_id: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["result_status", "file_name", "file_type", "file_id", "created_at", "last_updated_at", "status_messages", "retry_num", "registration_ticket_txid", "activation_ticket_txid", "original_file_ipfs_link", "stored_file_ipfs_link", "stored_file_aws_link", "stored_file_other_links", "make_publicly_accessible", "offer_ticket_txid", "offer_ticket_intended_rcpt_pastel_id", "error", "result_id"]

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
        """Create an instance of ResultRegistrationResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in status_messages (list)
        _items = []
        if self.status_messages:
            for _item in self.status_messages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['status_messages'] = _items
        # set to None if file_name (nullable) is None
        # and model_fields_set contains the field
        if self.file_name is None and "file_name" in self.model_fields_set:
            _dict['file_name'] = None

        # set to None if file_type (nullable) is None
        # and model_fields_set contains the field
        if self.file_type is None and "file_type" in self.model_fields_set:
            _dict['file_type'] = None

        # set to None if file_id (nullable) is None
        # and model_fields_set contains the field
        if self.file_id is None and "file_id" in self.model_fields_set:
            _dict['file_id'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if last_updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.last_updated_at is None and "last_updated_at" in self.model_fields_set:
            _dict['last_updated_at'] = None

        # set to None if status_messages (nullable) is None
        # and model_fields_set contains the field
        if self.status_messages is None and "status_messages" in self.model_fields_set:
            _dict['status_messages'] = None

        # set to None if retry_num (nullable) is None
        # and model_fields_set contains the field
        if self.retry_num is None and "retry_num" in self.model_fields_set:
            _dict['retry_num'] = None

        # set to None if registration_ticket_txid (nullable) is None
        # and model_fields_set contains the field
        if self.registration_ticket_txid is None and "registration_ticket_txid" in self.model_fields_set:
            _dict['registration_ticket_txid'] = None

        # set to None if activation_ticket_txid (nullable) is None
        # and model_fields_set contains the field
        if self.activation_ticket_txid is None and "activation_ticket_txid" in self.model_fields_set:
            _dict['activation_ticket_txid'] = None

        # set to None if original_file_ipfs_link (nullable) is None
        # and model_fields_set contains the field
        if self.original_file_ipfs_link is None and "original_file_ipfs_link" in self.model_fields_set:
            _dict['original_file_ipfs_link'] = None

        # set to None if stored_file_ipfs_link (nullable) is None
        # and model_fields_set contains the field
        if self.stored_file_ipfs_link is None and "stored_file_ipfs_link" in self.model_fields_set:
            _dict['stored_file_ipfs_link'] = None

        # set to None if stored_file_aws_link (nullable) is None
        # and model_fields_set contains the field
        if self.stored_file_aws_link is None and "stored_file_aws_link" in self.model_fields_set:
            _dict['stored_file_aws_link'] = None

        # set to None if stored_file_other_links (nullable) is None
        # and model_fields_set contains the field
        if self.stored_file_other_links is None and "stored_file_other_links" in self.model_fields_set:
            _dict['stored_file_other_links'] = None

        # set to None if make_publicly_accessible (nullable) is None
        # and model_fields_set contains the field
        if self.make_publicly_accessible is None and "make_publicly_accessible" in self.model_fields_set:
            _dict['make_publicly_accessible'] = None

        # set to None if offer_ticket_txid (nullable) is None
        # and model_fields_set contains the field
        if self.offer_ticket_txid is None and "offer_ticket_txid" in self.model_fields_set:
            _dict['offer_ticket_txid'] = None

        # set to None if offer_ticket_intended_rcpt_pastel_id (nullable) is None
        # and model_fields_set contains the field
        if self.offer_ticket_intended_rcpt_pastel_id is None and "offer_ticket_intended_rcpt_pastel_id" in self.model_fields_set:
            _dict['offer_ticket_intended_rcpt_pastel_id'] = None

        # set to None if error (nullable) is None
        # and model_fields_set contains the field
        if self.error is None and "error" in self.model_fields_set:
            _dict['error'] = None

        # set to None if result_id (nullable) is None
        # and model_fields_set contains the field
        if self.result_id is None and "result_id" in self.model_fields_set:
            _dict['result_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ResultRegistrationResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "result_status": obj.get("result_status"),
            "file_name": obj.get("file_name"),
            "file_type": obj.get("file_type"),
            "file_id": obj.get("file_id"),
            "created_at": obj.get("created_at"),
            "last_updated_at": obj.get("last_updated_at"),
            "status_messages": [CollectionRegistrationResultStatusMessagesInner.from_dict(_item) for _item in obj.get("status_messages")] if obj.get("status_messages") is not None else None,
            "retry_num": obj.get("retry_num"),
            "registration_ticket_txid": obj.get("registration_ticket_txid"),
            "activation_ticket_txid": obj.get("activation_ticket_txid"),
            "original_file_ipfs_link": obj.get("original_file_ipfs_link"),
            "stored_file_ipfs_link": obj.get("stored_file_ipfs_link"),
            "stored_file_aws_link": obj.get("stored_file_aws_link"),
            "stored_file_other_links": obj.get("stored_file_other_links"),
            "make_publicly_accessible": obj.get("make_publicly_accessible"),
            "offer_ticket_txid": obj.get("offer_ticket_txid"),
            "offer_ticket_intended_rcpt_pastel_id": obj.get("offer_ticket_intended_rcpt_pastel_id"),
            "error": obj.get("error"),
            "result_id": obj.get("result_id")
        })
        return _obj


