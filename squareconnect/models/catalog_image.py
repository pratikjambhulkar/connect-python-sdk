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


class CatalogImage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, url=None, caption=None):
        """
        CatalogImage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'url': 'str',
            'caption': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'url': 'url',
            'caption': 'caption'
        }

        self._name = name
        self._url = url
        self._caption = caption

    @property
    def name(self):
        """
        Gets the name of this CatalogImage.
        The internal name of this image. Identifies this image in calls to the Connect APIs.

        :return: The name of this CatalogImage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CatalogImage.
        The internal name of this image. Identifies this image in calls to the Connect APIs.

        :param name: The name of this CatalogImage.
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """
        Gets the url of this CatalogImage.
        The URL of this image. Generated by Square after an image is uploaded to the CreateCatalogImage endpoint.

        :return: The url of this CatalogImage.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this CatalogImage.
        The URL of this image. Generated by Square after an image is uploaded to the CreateCatalogImage endpoint.

        :param url: The url of this CatalogImage.
        :type: str
        """

        self._url = url

    @property
    def caption(self):
        """
        Gets the caption of this CatalogImage.
        A caption that describes what is shown in the image. Displayed in the Square Online Store.

        :return: The caption of this CatalogImage.
        :rtype: str
        """
        return self._caption

    @caption.setter
    def caption(self, caption):
        """
        Sets the caption of this CatalogImage.
        A caption that describes what is shown in the image. Displayed in the Square Online Store.

        :param caption: The caption of this CatalogImage.
        :type: str
        """

        self._caption = caption

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
