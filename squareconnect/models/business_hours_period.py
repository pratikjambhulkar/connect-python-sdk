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


class BusinessHoursPeriod(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, day_of_week=None, start_local_time=None, end_local_time=None):
        """
        BusinessHoursPeriod - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'day_of_week': 'str',
            'start_local_time': 'str',
            'end_local_time': 'str'
        }

        self.attribute_map = {
            'day_of_week': 'day_of_week',
            'start_local_time': 'start_local_time',
            'end_local_time': 'end_local_time'
        }

        self._day_of_week = day_of_week
        self._start_local_time = start_local_time
        self._end_local_time = end_local_time

    @property
    def day_of_week(self):
        """
        Gets the day_of_week of this BusinessHoursPeriod.
        The day of week for this time period. See [DayOfWeek](#type-dayofweek) for possible values

        :return: The day_of_week of this BusinessHoursPeriod.
        :rtype: str
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """
        Sets the day_of_week of this BusinessHoursPeriod.
        The day of week for this time period. See [DayOfWeek](#type-dayofweek) for possible values

        :param day_of_week: The day_of_week of this BusinessHoursPeriod.
        :type: str
        """

        self._day_of_week = day_of_week

    @property
    def start_local_time(self):
        """
        Gets the start_local_time of this BusinessHoursPeriod.
        The start time of a business hours period, specified in local time using partial-time RFC3339 format.

        :return: The start_local_time of this BusinessHoursPeriod.
        :rtype: str
        """
        return self._start_local_time

    @start_local_time.setter
    def start_local_time(self, start_local_time):
        """
        Sets the start_local_time of this BusinessHoursPeriod.
        The start time of a business hours period, specified in local time using partial-time RFC3339 format.

        :param start_local_time: The start_local_time of this BusinessHoursPeriod.
        :type: str
        """

        self._start_local_time = start_local_time

    @property
    def end_local_time(self):
        """
        Gets the end_local_time of this BusinessHoursPeriod.
        The end time of a business hours period, specified in local time using partial-time RFC3339 format.

        :return: The end_local_time of this BusinessHoursPeriod.
        :rtype: str
        """
        return self._end_local_time

    @end_local_time.setter
    def end_local_time(self, end_local_time):
        """
        Sets the end_local_time of this BusinessHoursPeriod.
        The end time of a business hours period, specified in local time using partial-time RFC3339 format.

        :param end_local_time: The end_local_time of this BusinessHoursPeriod.
        :type: str
        """

        self._end_local_time = end_local_time

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