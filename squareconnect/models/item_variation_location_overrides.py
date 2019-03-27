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


class ItemVariationLocationOverrides(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, location_id=None, price_money=None, pricing_type=None, track_inventory=None, inventory_alert_type=None, inventory_alert_threshold=None):
        """
        ItemVariationLocationOverrides - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'location_id': 'str',
            'price_money': 'Money',
            'pricing_type': 'str',
            'track_inventory': 'bool',
            'inventory_alert_type': 'str',
            'inventory_alert_threshold': 'int'
        }

        self.attribute_map = {
            'location_id': 'location_id',
            'price_money': 'price_money',
            'pricing_type': 'pricing_type',
            'track_inventory': 'track_inventory',
            'inventory_alert_type': 'inventory_alert_type',
            'inventory_alert_threshold': 'inventory_alert_threshold'
        }

        self._location_id = location_id
        self._price_money = price_money
        self._pricing_type = pricing_type
        self._track_inventory = track_inventory
        self._inventory_alert_type = inventory_alert_type
        self._inventory_alert_threshold = inventory_alert_threshold

    @property
    def location_id(self):
        """
        Gets the location_id of this ItemVariationLocationOverrides.
        The ID of the [location](#type-location).

        :return: The location_id of this ItemVariationLocationOverrides.
        :rtype: str
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """
        Sets the location_id of this ItemVariationLocationOverrides.
        The ID of the [location](#type-location).

        :param location_id: The location_id of this ItemVariationLocationOverrides.
        :type: str
        """

        self._location_id = location_id

    @property
    def price_money(self):
        """
        Gets the price_money of this ItemVariationLocationOverrides.
        The price of the [CatalogItemVariation](#type-catalogitemvariation) at the given [location](#type-location), or blank for variable pricing.

        :return: The price_money of this ItemVariationLocationOverrides.
        :rtype: Money
        """
        return self._price_money

    @price_money.setter
    def price_money(self, price_money):
        """
        Sets the price_money of this ItemVariationLocationOverrides.
        The price of the [CatalogItemVariation](#type-catalogitemvariation) at the given [location](#type-location), or blank for variable pricing.

        :param price_money: The price_money of this ItemVariationLocationOverrides.
        :type: Money
        """

        self._price_money = price_money

    @property
    def pricing_type(self):
        """
        Gets the pricing_type of this ItemVariationLocationOverrides.
        The pricing type (fixed or variable) for the [CatalogItemVariation](#type-catalogitemvariation) at the given [location](#type-location). See [CatalogPricingType](#type-catalogpricingtype) for possible values

        :return: The pricing_type of this ItemVariationLocationOverrides.
        :rtype: str
        """
        return self._pricing_type

    @pricing_type.setter
    def pricing_type(self, pricing_type):
        """
        Sets the pricing_type of this ItemVariationLocationOverrides.
        The pricing type (fixed or variable) for the [CatalogItemVariation](#type-catalogitemvariation) at the given [location](#type-location). See [CatalogPricingType](#type-catalogpricingtype) for possible values

        :param pricing_type: The pricing_type of this ItemVariationLocationOverrides.
        :type: str
        """

        self._pricing_type = pricing_type

    @property
    def track_inventory(self):
        """
        Gets the track_inventory of this ItemVariationLocationOverrides.
        If `true`, inventory tracking is active for the [CatalogItemVariation](#type-catalogitemvariation) at this [location](#type-location).

        :return: The track_inventory of this ItemVariationLocationOverrides.
        :rtype: bool
        """
        return self._track_inventory

    @track_inventory.setter
    def track_inventory(self, track_inventory):
        """
        Sets the track_inventory of this ItemVariationLocationOverrides.
        If `true`, inventory tracking is active for the [CatalogItemVariation](#type-catalogitemvariation) at this [location](#type-location).

        :param track_inventory: The track_inventory of this ItemVariationLocationOverrides.
        :type: bool
        """

        self._track_inventory = track_inventory

    @property
    def inventory_alert_type(self):
        """
        Gets the inventory_alert_type of this ItemVariationLocationOverrides.
        Indicates whether the [CatalogItemVariation](#type-catalogitemvariation) displays an alert when its inventory quantity is less than or equal to its `inventory_alert_threshold`. See [InventoryAlertType](#type-inventoryalerttype) for possible values

        :return: The inventory_alert_type of this ItemVariationLocationOverrides.
        :rtype: str
        """
        return self._inventory_alert_type

    @inventory_alert_type.setter
    def inventory_alert_type(self, inventory_alert_type):
        """
        Sets the inventory_alert_type of this ItemVariationLocationOverrides.
        Indicates whether the [CatalogItemVariation](#type-catalogitemvariation) displays an alert when its inventory quantity is less than or equal to its `inventory_alert_threshold`. See [InventoryAlertType](#type-inventoryalerttype) for possible values

        :param inventory_alert_type: The inventory_alert_type of this ItemVariationLocationOverrides.
        :type: str
        """

        self._inventory_alert_type = inventory_alert_type

    @property
    def inventory_alert_threshold(self):
        """
        Gets the inventory_alert_threshold of this ItemVariationLocationOverrides.
        If the inventory quantity for the variation is less than or equal to this value and `inventory_alert_type` is `LOW_QUANTITY`, the variation displays an alert in the merchant dashboard.  This value is always an integer.

        :return: The inventory_alert_threshold of this ItemVariationLocationOverrides.
        :rtype: int
        """
        return self._inventory_alert_threshold

    @inventory_alert_threshold.setter
    def inventory_alert_threshold(self, inventory_alert_threshold):
        """
        Sets the inventory_alert_threshold of this ItemVariationLocationOverrides.
        If the inventory quantity for the variation is less than or equal to this value and `inventory_alert_type` is `LOW_QUANTITY`, the variation displays an alert in the merchant dashboard.  This value is always an integer.

        :param inventory_alert_threshold: The inventory_alert_threshold of this ItemVariationLocationOverrides.
        :type: int
        """

        self._inventory_alert_threshold = inventory_alert_threshold

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
