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


class ShiftSort(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, field=None, order=None):
        """
        ShiftSort - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'field': 'str',
            'order': 'str'
        }

        self.attribute_map = {
            'field': 'field',
            'order': 'order'
        }

        self._field = field
        self._order = order

    @property
    def field(self):
        """
        Gets the field of this ShiftSort.
        The field to sort on. See [ShiftSortField](#type-shiftsortfield) for possible values

        :return: The field of this ShiftSort.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """
        Sets the field of this ShiftSort.
        The field to sort on. See [ShiftSortField](#type-shiftsortfield) for possible values

        :param field: The field of this ShiftSort.
        :type: str
        """

        self._field = field

    @property
    def order(self):
        """
        Gets the order of this ShiftSort.
        The order in which results are returned. Defaults to DESC. See [SortOrder](#type-sortorder) for possible values

        :return: The order of this ShiftSort.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this ShiftSort.
        The order in which results are returned. Defaults to DESC. See [SortOrder](#type-sortorder) for possible values

        :param order: The order of this ShiftSort.
        :type: str
        """

        self._order = order

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
