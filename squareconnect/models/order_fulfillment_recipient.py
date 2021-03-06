# coding: utf-8

"""
Copyright 2017 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from pprint import pformat
from six import iteritems
import re


class OrderFulfillmentRecipient(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, customer_id=None, display_name=None, email_address=None, phone_number=None):
        """
        OrderFulfillmentRecipient - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'customer_id': 'str',
            'display_name': 'str',
            'email_address': 'str',
            'phone_number': 'str'
        }

        self.attribute_map = {
            'customer_id': 'customer_id',
            'display_name': 'display_name',
            'email_address': 'email_address',
            'phone_number': 'phone_number'
        }

        self._customer_id = customer_id
        self._display_name = display_name
        self._email_address = email_address
        self._phone_number = phone_number

    @property
    def customer_id(self):
        """
        Gets the customer_id of this OrderFulfillmentRecipient.
        The Customer ID of the customer associated with the fulfillment.  If customer_id is provided, the corresponding recipient information fields (`display_name`, `email_address`, and `phone_number`) are automatically populated from the relevant customer profile. If the targeted profile information does not contain the necessary required information, the request will result in an error.

        :return: The customer_id of this OrderFulfillmentRecipient.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """
        Sets the customer_id of this OrderFulfillmentRecipient.
        The Customer ID of the customer associated with the fulfillment.  If customer_id is provided, the corresponding recipient information fields (`display_name`, `email_address`, and `phone_number`) are automatically populated from the relevant customer profile. If the targeted profile information does not contain the necessary required information, the request will result in an error.

        :param customer_id: The customer_id of this OrderFulfillmentRecipient.
        :type: str
        """

        self._customer_id = customer_id

    @property
    def display_name(self):
        """
        Gets the display_name of this OrderFulfillmentRecipient.
        The display name of the fulfillment recipient.  If provided, overrides the value from customer profile indicated by customer_id.

        :return: The display_name of this OrderFulfillmentRecipient.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this OrderFulfillmentRecipient.
        The display name of the fulfillment recipient.  If provided, overrides the value from customer profile indicated by customer_id.

        :param display_name: The display_name of this OrderFulfillmentRecipient.
        :type: str
        """

        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")
        if len(display_name) > 255:
            raise ValueError("Invalid value for `display_name`, length must be less than `255`")

        self._display_name = display_name

    @property
    def email_address(self):
        """
        Gets the email_address of this OrderFulfillmentRecipient.
        The email address of the fulfillment recipient.  If provided, overrides the value from customer profile indicated by customer_id.

        :return: The email_address of this OrderFulfillmentRecipient.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """
        Sets the email_address of this OrderFulfillmentRecipient.
        The email address of the fulfillment recipient.  If provided, overrides the value from customer profile indicated by customer_id.

        :param email_address: The email_address of this OrderFulfillmentRecipient.
        :type: str
        """

        if email_address is None:
            raise ValueError("Invalid value for `email_address`, must not be `None`")
        if len(email_address) > 255:
            raise ValueError("Invalid value for `email_address`, length must be less than `255`")

        self._email_address = email_address

    @property
    def phone_number(self):
        """
        Gets the phone_number of this OrderFulfillmentRecipient.
        The phone number of the fulfillment recipient.  If provided, overrides the value from customer profile indicated by customer_id.

        :return: The phone_number of this OrderFulfillmentRecipient.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this OrderFulfillmentRecipient.
        The phone number of the fulfillment recipient.  If provided, overrides the value from customer profile indicated by customer_id.

        :param phone_number: The phone_number of this OrderFulfillmentRecipient.
        :type: str
        """

        if phone_number is None:
            raise ValueError("Invalid value for `phone_number`, must not be `None`")
        if len(phone_number) > 16:
            raise ValueError("Invalid value for `phone_number`, length must be less than `16`")

        self._phone_number = phone_number

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
