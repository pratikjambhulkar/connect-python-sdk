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


class CatalogItemVariation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, item_id=None, name=None, sku=None, upc=None, ordinal=None, pricing_type=None, price_money=None, location_overrides=None, track_inventory=None, inventory_alert_type=None, inventory_alert_threshold=None, user_data=None, service_duration=None):
        """
        CatalogItemVariation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'item_id': 'str',
            'name': 'str',
            'sku': 'str',
            'upc': 'str',
            'ordinal': 'int',
            'pricing_type': 'str',
            'price_money': 'Money',
            'location_overrides': 'list[ItemVariationLocationOverrides]',
            'track_inventory': 'bool',
            'inventory_alert_type': 'str',
            'inventory_alert_threshold': 'int',
            'user_data': 'str',
            'service_duration': 'int'
        }

        self.attribute_map = {
            'item_id': 'item_id',
            'name': 'name',
            'sku': 'sku',
            'upc': 'upc',
            'ordinal': 'ordinal',
            'pricing_type': 'pricing_type',
            'price_money': 'price_money',
            'location_overrides': 'location_overrides',
            'track_inventory': 'track_inventory',
            'inventory_alert_type': 'inventory_alert_type',
            'inventory_alert_threshold': 'inventory_alert_threshold',
            'user_data': 'user_data',
            'service_duration': 'service_duration'
        }

        self._item_id = item_id
        self._name = name
        self._sku = sku
        self._upc = upc
        self._ordinal = ordinal
        self._pricing_type = pricing_type
        self._price_money = price_money
        self._location_overrides = location_overrides
        self._track_inventory = track_inventory
        self._inventory_alert_type = inventory_alert_type
        self._inventory_alert_threshold = inventory_alert_threshold
        self._user_data = user_data
        self._service_duration = service_duration

    @property
    def item_id(self):
        """
        Gets the item_id of this CatalogItemVariation.
        The ID of the [CatalogItem](#type-catalogitem) associated with this item variation. Searchable.

        :return: The item_id of this CatalogItemVariation.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """
        Sets the item_id of this CatalogItemVariation.
        The ID of the [CatalogItem](#type-catalogitem) associated with this item variation. Searchable.

        :param item_id: The item_id of this CatalogItemVariation.
        :type: str
        """

        self._item_id = item_id

    @property
    def name(self):
        """
        Gets the name of this CatalogItemVariation.
        The item variation's name. Searchable. This field has max length of 255 Unicode code points.

        :return: The name of this CatalogItemVariation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CatalogItemVariation.
        The item variation's name. Searchable. This field has max length of 255 Unicode code points.

        :param name: The name of this CatalogItemVariation.
        :type: str
        """

        self._name = name

    @property
    def sku(self):
        """
        Gets the sku of this CatalogItemVariation.
        The item variation's SKU, if any. Searchable.

        :return: The sku of this CatalogItemVariation.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """
        Sets the sku of this CatalogItemVariation.
        The item variation's SKU, if any. Searchable.

        :param sku: The sku of this CatalogItemVariation.
        :type: str
        """

        self._sku = sku

    @property
    def upc(self):
        """
        Gets the upc of this CatalogItemVariation.
        The item variation's UPC, if any. Searchable in the Connect API. This field is only exposed in the Connect API. It is not exposed in Square's Dashboard, Square Point of Sale app or Retail Point of Sale app.

        :return: The upc of this CatalogItemVariation.
        :rtype: str
        """
        return self._upc

    @upc.setter
    def upc(self, upc):
        """
        Sets the upc of this CatalogItemVariation.
        The item variation's UPC, if any. Searchable in the Connect API. This field is only exposed in the Connect API. It is not exposed in Square's Dashboard, Square Point of Sale app or Retail Point of Sale app.

        :param upc: The upc of this CatalogItemVariation.
        :type: str
        """

        self._upc = upc

    @property
    def ordinal(self):
        """
        Gets the ordinal of this CatalogItemVariation.
        The order in which this item variation should be displayed. This value is read-only. On writes, the ordinal for each item variation within a parent [CatalogItem](#type-catalogitem) is set according to the item variations's position. On reads, the value is not guaranteed to be sequential or unique.

        :return: The ordinal of this CatalogItemVariation.
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        """
        Sets the ordinal of this CatalogItemVariation.
        The order in which this item variation should be displayed. This value is read-only. On writes, the ordinal for each item variation within a parent [CatalogItem](#type-catalogitem) is set according to the item variations's position. On reads, the value is not guaranteed to be sequential or unique.

        :param ordinal: The ordinal of this CatalogItemVariation.
        :type: int
        """

        self._ordinal = ordinal

    @property
    def pricing_type(self):
        """
        Gets the pricing_type of this CatalogItemVariation.
        Indicates whether the item variation's price is fixed or determined at the time of sale. See [CatalogPricingType](#type-catalogpricingtype) for possible values

        :return: The pricing_type of this CatalogItemVariation.
        :rtype: str
        """
        return self._pricing_type

    @pricing_type.setter
    def pricing_type(self, pricing_type):
        """
        Sets the pricing_type of this CatalogItemVariation.
        Indicates whether the item variation's price is fixed or determined at the time of sale. See [CatalogPricingType](#type-catalogpricingtype) for possible values

        :param pricing_type: The pricing_type of this CatalogItemVariation.
        :type: str
        """

        self._pricing_type = pricing_type

    @property
    def price_money(self):
        """
        Gets the price_money of this CatalogItemVariation.
        The item variation's price, if fixed pricing is used.

        :return: The price_money of this CatalogItemVariation.
        :rtype: Money
        """
        return self._price_money

    @price_money.setter
    def price_money(self, price_money):
        """
        Sets the price_money of this CatalogItemVariation.
        The item variation's price, if fixed pricing is used.

        :param price_money: The price_money of this CatalogItemVariation.
        :type: Money
        """

        self._price_money = price_money

    @property
    def location_overrides(self):
        """
        Gets the location_overrides of this CatalogItemVariation.
        Per-[location](#type-location) price and inventory overrides.

        :return: The location_overrides of this CatalogItemVariation.
        :rtype: list[ItemVariationLocationOverrides]
        """
        return self._location_overrides

    @location_overrides.setter
    def location_overrides(self, location_overrides):
        """
        Sets the location_overrides of this CatalogItemVariation.
        Per-[location](#type-location) price and inventory overrides.

        :param location_overrides: The location_overrides of this CatalogItemVariation.
        :type: list[ItemVariationLocationOverrides]
        """

        self._location_overrides = location_overrides

    @property
    def track_inventory(self):
        """
        Gets the track_inventory of this CatalogItemVariation.
        If `true`, inventory tracking is active for the variation.

        :return: The track_inventory of this CatalogItemVariation.
        :rtype: bool
        """
        return self._track_inventory

    @track_inventory.setter
    def track_inventory(self, track_inventory):
        """
        Sets the track_inventory of this CatalogItemVariation.
        If `true`, inventory tracking is active for the variation.

        :param track_inventory: The track_inventory of this CatalogItemVariation.
        :type: bool
        """

        self._track_inventory = track_inventory

    @property
    def inventory_alert_type(self):
        """
        Gets the inventory_alert_type of this CatalogItemVariation.
        Indicates whether the item variation displays an alert when its inventory quantity is less than or equal to its `inventory_alert_threshold`. See [InventoryAlertType](#type-inventoryalerttype) for possible values

        :return: The inventory_alert_type of this CatalogItemVariation.
        :rtype: str
        """
        return self._inventory_alert_type

    @inventory_alert_type.setter
    def inventory_alert_type(self, inventory_alert_type):
        """
        Sets the inventory_alert_type of this CatalogItemVariation.
        Indicates whether the item variation displays an alert when its inventory quantity is less than or equal to its `inventory_alert_threshold`. See [InventoryAlertType](#type-inventoryalerttype) for possible values

        :param inventory_alert_type: The inventory_alert_type of this CatalogItemVariation.
        :type: str
        """

        self._inventory_alert_type = inventory_alert_type

    @property
    def inventory_alert_threshold(self):
        """
        Gets the inventory_alert_threshold of this CatalogItemVariation.
        If the inventory quantity for the variation is less than or equal to this value and `inventory_alert_type` is `LOW_QUANTITY`, the variation displays an alert in the merchant dashboard.  This value is always an integer.

        :return: The inventory_alert_threshold of this CatalogItemVariation.
        :rtype: int
        """
        return self._inventory_alert_threshold

    @inventory_alert_threshold.setter
    def inventory_alert_threshold(self, inventory_alert_threshold):
        """
        Sets the inventory_alert_threshold of this CatalogItemVariation.
        If the inventory quantity for the variation is less than or equal to this value and `inventory_alert_type` is `LOW_QUANTITY`, the variation displays an alert in the merchant dashboard.  This value is always an integer.

        :param inventory_alert_threshold: The inventory_alert_threshold of this CatalogItemVariation.
        :type: int
        """

        self._inventory_alert_threshold = inventory_alert_threshold

    @property
    def user_data(self):
        """
        Gets the user_data of this CatalogItemVariation.
        Arbitrary user metadata to associate with the item variation. Cannot exceed 255 characters. Searchable.

        :return: The user_data of this CatalogItemVariation.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """
        Sets the user_data of this CatalogItemVariation.
        Arbitrary user metadata to associate with the item variation. Cannot exceed 255 characters. Searchable.

        :param user_data: The user_data of this CatalogItemVariation.
        :type: str
        """

        self._user_data = user_data

    @property
    def service_duration(self):
        """
        Gets the service_duration of this CatalogItemVariation.
        If the [CatalogItem](#type-catalogitem) that owns this item variation is of type `APPOINTMENTS_SERVICE`, then this is the duration of the service in milliseconds. For example, a 30 minute appointment would have the value `1800000`, which is equal to 30 (minutes) * 60 (seconds per minute) * 1000 (milliseconds per second).

        :return: The service_duration of this CatalogItemVariation.
        :rtype: int
        """
        return self._service_duration

    @service_duration.setter
    def service_duration(self, service_duration):
        """
        Sets the service_duration of this CatalogItemVariation.
        If the [CatalogItem](#type-catalogitem) that owns this item variation is of type `APPOINTMENTS_SERVICE`, then this is the duration of the service in milliseconds. For example, a 30 minute appointment would have the value `1800000`, which is equal to 30 (minutes) * 60 (seconds per minute) * 1000 (milliseconds per second).

        :param service_duration: The service_duration of this CatalogItemVariation.
        :type: int
        """

        self._service_duration = service_duration

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
