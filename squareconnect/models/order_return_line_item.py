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


class OrderReturnLineItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, uid=None, source_line_item_uid=None, name=None, quantity=None, quantity_unit=None, note=None, catalog_object_id=None, variation_name=None, return_modifiers=None, return_taxes=None, return_discounts=None, base_price_money=None, variation_total_price_money=None, gross_return_money=None, total_tax_money=None, total_discount_money=None, total_money=None):
        """
        OrderReturnLineItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'uid': 'str',
            'source_line_item_uid': 'str',
            'name': 'str',
            'quantity': 'str',
            'quantity_unit': 'OrderQuantityUnit',
            'note': 'str',
            'catalog_object_id': 'str',
            'variation_name': 'str',
            'return_modifiers': 'list[OrderReturnLineItemModifier]',
            'return_taxes': 'list[OrderReturnTax]',
            'return_discounts': 'list[OrderReturnDiscount]',
            'base_price_money': 'Money',
            'variation_total_price_money': 'Money',
            'gross_return_money': 'Money',
            'total_tax_money': 'Money',
            'total_discount_money': 'Money',
            'total_money': 'Money'
        }

        self.attribute_map = {
            'uid': 'uid',
            'source_line_item_uid': 'source_line_item_uid',
            'name': 'name',
            'quantity': 'quantity',
            'quantity_unit': 'quantity_unit',
            'note': 'note',
            'catalog_object_id': 'catalog_object_id',
            'variation_name': 'variation_name',
            'return_modifiers': 'return_modifiers',
            'return_taxes': 'return_taxes',
            'return_discounts': 'return_discounts',
            'base_price_money': 'base_price_money',
            'variation_total_price_money': 'variation_total_price_money',
            'gross_return_money': 'gross_return_money',
            'total_tax_money': 'total_tax_money',
            'total_discount_money': 'total_discount_money',
            'total_money': 'total_money'
        }

        self._uid = uid
        self._source_line_item_uid = source_line_item_uid
        self._name = name
        self._quantity = quantity
        self._quantity_unit = quantity_unit
        self._note = note
        self._catalog_object_id = catalog_object_id
        self._variation_name = variation_name
        self._return_modifiers = return_modifiers
        self._return_taxes = return_taxes
        self._return_discounts = return_discounts
        self._base_price_money = base_price_money
        self._variation_total_price_money = variation_total_price_money
        self._gross_return_money = gross_return_money
        self._total_tax_money = total_tax_money
        self._total_discount_money = total_discount_money
        self._total_money = total_money

    @property
    def uid(self):
        """
        Gets the uid of this OrderReturnLineItem.
        Unique identifier for this return line item entry. This is a read-only field.

        :return: The uid of this OrderReturnLineItem.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """
        Sets the uid of this OrderReturnLineItem.
        Unique identifier for this return line item entry. This is a read-only field.

        :param uid: The uid of this OrderReturnLineItem.
        :type: str
        """

        if uid is None:
            raise ValueError("Invalid value for `uid`, must not be `None`")
        if len(uid) > 60:
            raise ValueError("Invalid value for `uid`, length must be less than `60`")

        self._uid = uid

    @property
    def source_line_item_uid(self):
        """
        Gets the source_line_item_uid of this OrderReturnLineItem.
        `uid` of the LineItem in the original sale Order.

        :return: The source_line_item_uid of this OrderReturnLineItem.
        :rtype: str
        """
        return self._source_line_item_uid

    @source_line_item_uid.setter
    def source_line_item_uid(self, source_line_item_uid):
        """
        Sets the source_line_item_uid of this OrderReturnLineItem.
        `uid` of the LineItem in the original sale Order.

        :param source_line_item_uid: The source_line_item_uid of this OrderReturnLineItem.
        :type: str
        """

        if source_line_item_uid is None:
            raise ValueError("Invalid value for `source_line_item_uid`, must not be `None`")
        if len(source_line_item_uid) > 60:
            raise ValueError("Invalid value for `source_line_item_uid`, length must be less than `60`")

        self._source_line_item_uid = source_line_item_uid

    @property
    def name(self):
        """
        Gets the name of this OrderReturnLineItem.
        The name of the line item.

        :return: The name of this OrderReturnLineItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OrderReturnLineItem.
        The name of the line item.

        :param name: The name of this OrderReturnLineItem.
        :type: str
        """

        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if len(name) > 500:
            raise ValueError("Invalid value for `name`, length must be less than `500`")

        self._name = name

    @property
    def quantity(self):
        """
        Gets the quantity of this OrderReturnLineItem.
        The quantity returned, formatted as a decimal number. For example: `\"3\"`.  Line items with a `quantity_unit` can have non-integer quantities. For example: `\"1.70000\"`.

        :return: The quantity of this OrderReturnLineItem.
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this OrderReturnLineItem.
        The quantity returned, formatted as a decimal number. For example: `\"3\"`.  Line items with a `quantity_unit` can have non-integer quantities. For example: `\"1.70000\"`.

        :param quantity: The quantity of this OrderReturnLineItem.
        :type: str
        """

        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")
        if len(quantity) > 12:
            raise ValueError("Invalid value for `quantity`, length must be less than `12`")
        if len(quantity) < 1:
            raise ValueError("Invalid value for `quantity`, length must be greater than or equal to `1`")

        self._quantity = quantity

    @property
    def quantity_unit(self):
        """
        Gets the quantity_unit of this OrderReturnLineItem.
        The unit and precision that this return line item's quantity is measured in.

        :return: The quantity_unit of this OrderReturnLineItem.
        :rtype: OrderQuantityUnit
        """
        return self._quantity_unit

    @quantity_unit.setter
    def quantity_unit(self, quantity_unit):
        """
        Sets the quantity_unit of this OrderReturnLineItem.
        The unit and precision that this return line item's quantity is measured in.

        :param quantity_unit: The quantity_unit of this OrderReturnLineItem.
        :type: OrderQuantityUnit
        """

        self._quantity_unit = quantity_unit

    @property
    def note(self):
        """
        Gets the note of this OrderReturnLineItem.
        The note of the returned line item.

        :return: The note of this OrderReturnLineItem.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """
        Sets the note of this OrderReturnLineItem.
        The note of the returned line item.

        :param note: The note of this OrderReturnLineItem.
        :type: str
        """

        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")
        if len(note) > 500:
            raise ValueError("Invalid value for `note`, length must be less than `500`")

        self._note = note

    @property
    def catalog_object_id(self):
        """
        Gets the catalog_object_id of this OrderReturnLineItem.
        The [CatalogItemVariation](#type-catalogitemvariation) id applied to this returned line item.

        :return: The catalog_object_id of this OrderReturnLineItem.
        :rtype: str
        """
        return self._catalog_object_id

    @catalog_object_id.setter
    def catalog_object_id(self, catalog_object_id):
        """
        Sets the catalog_object_id of this OrderReturnLineItem.
        The [CatalogItemVariation](#type-catalogitemvariation) id applied to this returned line item.

        :param catalog_object_id: The catalog_object_id of this OrderReturnLineItem.
        :type: str
        """

        if catalog_object_id is None:
            raise ValueError("Invalid value for `catalog_object_id`, must not be `None`")
        if len(catalog_object_id) > 192:
            raise ValueError("Invalid value for `catalog_object_id`, length must be less than `192`")

        self._catalog_object_id = catalog_object_id

    @property
    def variation_name(self):
        """
        Gets the variation_name of this OrderReturnLineItem.
        The name of the variation applied to this returned line item.

        :return: The variation_name of this OrderReturnLineItem.
        :rtype: str
        """
        return self._variation_name

    @variation_name.setter
    def variation_name(self, variation_name):
        """
        Sets the variation_name of this OrderReturnLineItem.
        The name of the variation applied to this returned line item.

        :param variation_name: The variation_name of this OrderReturnLineItem.
        :type: str
        """

        if variation_name is None:
            raise ValueError("Invalid value for `variation_name`, must not be `None`")
        if len(variation_name) > 255:
            raise ValueError("Invalid value for `variation_name`, length must be less than `255`")

        self._variation_name = variation_name

    @property
    def return_modifiers(self):
        """
        Gets the return_modifiers of this OrderReturnLineItem.
        The [CatalogModifier](#type-catalogmodifier)s applied to this line item.

        :return: The return_modifiers of this OrderReturnLineItem.
        :rtype: list[OrderReturnLineItemModifier]
        """
        return self._return_modifiers

    @return_modifiers.setter
    def return_modifiers(self, return_modifiers):
        """
        Sets the return_modifiers of this OrderReturnLineItem.
        The [CatalogModifier](#type-catalogmodifier)s applied to this line item.

        :param return_modifiers: The return_modifiers of this OrderReturnLineItem.
        :type: list[OrderReturnLineItemModifier]
        """

        self._return_modifiers = return_modifiers

    @property
    def return_taxes(self):
        """
        Gets the return_taxes of this OrderReturnLineItem.
        A list of taxes applied to this line item. On read or retrieve, this list includes both item-level taxes and any return-level taxes apportioned to this item.

        :return: The return_taxes of this OrderReturnLineItem.
        :rtype: list[OrderReturnTax]
        """
        return self._return_taxes

    @return_taxes.setter
    def return_taxes(self, return_taxes):
        """
        Sets the return_taxes of this OrderReturnLineItem.
        A list of taxes applied to this line item. On read or retrieve, this list includes both item-level taxes and any return-level taxes apportioned to this item.

        :param return_taxes: The return_taxes of this OrderReturnLineItem.
        :type: list[OrderReturnTax]
        """

        self._return_taxes = return_taxes

    @property
    def return_discounts(self):
        """
        Gets the return_discounts of this OrderReturnLineItem.
        A list of discounts applied to this line item. On read or retrieve, this list includes both item-level discounts and any return-level discounts apportioned to this item.

        :return: The return_discounts of this OrderReturnLineItem.
        :rtype: list[OrderReturnDiscount]
        """
        return self._return_discounts

    @return_discounts.setter
    def return_discounts(self, return_discounts):
        """
        Sets the return_discounts of this OrderReturnLineItem.
        A list of discounts applied to this line item. On read or retrieve, this list includes both item-level discounts and any return-level discounts apportioned to this item.

        :param return_discounts: The return_discounts of this OrderReturnLineItem.
        :type: list[OrderReturnDiscount]
        """

        self._return_discounts = return_discounts

    @property
    def base_price_money(self):
        """
        Gets the base_price_money of this OrderReturnLineItem.
        The base price for a single unit of the line item.

        :return: The base_price_money of this OrderReturnLineItem.
        :rtype: Money
        """
        return self._base_price_money

    @base_price_money.setter
    def base_price_money(self, base_price_money):
        """
        Sets the base_price_money of this OrderReturnLineItem.
        The base price for a single unit of the line item.

        :param base_price_money: The base_price_money of this OrderReturnLineItem.
        :type: Money
        """

        self._base_price_money = base_price_money

    @property
    def variation_total_price_money(self):
        """
        Gets the variation_total_price_money of this OrderReturnLineItem.
        The total price of all item variations returned in this line item. Calculated as `base_price_money` multiplied by `quantity`. Does not include modifiers.

        :return: The variation_total_price_money of this OrderReturnLineItem.
        :rtype: Money
        """
        return self._variation_total_price_money

    @variation_total_price_money.setter
    def variation_total_price_money(self, variation_total_price_money):
        """
        Sets the variation_total_price_money of this OrderReturnLineItem.
        The total price of all item variations returned in this line item. Calculated as `base_price_money` multiplied by `quantity`. Does not include modifiers.

        :param variation_total_price_money: The variation_total_price_money of this OrderReturnLineItem.
        :type: Money
        """

        self._variation_total_price_money = variation_total_price_money

    @property
    def gross_return_money(self):
        """
        Gets the gross_return_money of this OrderReturnLineItem.
        The gross return amount of money calculated as (item base price + modifiers price) * quantity.

        :return: The gross_return_money of this OrderReturnLineItem.
        :rtype: Money
        """
        return self._gross_return_money

    @gross_return_money.setter
    def gross_return_money(self, gross_return_money):
        """
        Sets the gross_return_money of this OrderReturnLineItem.
        The gross return amount of money calculated as (item base price + modifiers price) * quantity.

        :param gross_return_money: The gross_return_money of this OrderReturnLineItem.
        :type: Money
        """

        self._gross_return_money = gross_return_money

    @property
    def total_tax_money(self):
        """
        Gets the total_tax_money of this OrderReturnLineItem.
        The total tax amount of money to return for the line item.

        :return: The total_tax_money of this OrderReturnLineItem.
        :rtype: Money
        """
        return self._total_tax_money

    @total_tax_money.setter
    def total_tax_money(self, total_tax_money):
        """
        Sets the total_tax_money of this OrderReturnLineItem.
        The total tax amount of money to return for the line item.

        :param total_tax_money: The total_tax_money of this OrderReturnLineItem.
        :type: Money
        """

        self._total_tax_money = total_tax_money

    @property
    def total_discount_money(self):
        """
        Gets the total_discount_money of this OrderReturnLineItem.
        The total discount amount of money to return for the line item.

        :return: The total_discount_money of this OrderReturnLineItem.
        :rtype: Money
        """
        return self._total_discount_money

    @total_discount_money.setter
    def total_discount_money(self, total_discount_money):
        """
        Sets the total_discount_money of this OrderReturnLineItem.
        The total discount amount of money to return for the line item.

        :param total_discount_money: The total_discount_money of this OrderReturnLineItem.
        :type: Money
        """

        self._total_discount_money = total_discount_money

    @property
    def total_money(self):
        """
        Gets the total_money of this OrderReturnLineItem.
        The total amount of money to return for this line item.

        :return: The total_money of this OrderReturnLineItem.
        :rtype: Money
        """
        return self._total_money

    @total_money.setter
    def total_money(self, total_money):
        """
        Sets the total_money of this OrderReturnLineItem.
        The total amount of money to return for this line item.

        :param total_money: The total_money of this OrderReturnLineItem.
        :type: Money
        """

        self._total_money = total_money

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
