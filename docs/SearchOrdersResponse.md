# SearchOrdersResponse
> squareconnect.models.search_orders_response

### Description

Only one of `order_entries` or `orders` fields will be set, depending on whether `return_entries` was set on the [SearchOrdersRequest](#type-searchorderrequest).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_entries** | [**list[OrderEntry]**](OrderEntry.md) | List of [OrderEntries](#type-orderentry) that fit the query conditions.  Populated only if &#x60;order_entries&#x60; was set to &#x60;true&#x60; in the request. | [optional] 
**orders** | [**list[Order]**](Order.md) | List of [Orders](#type-order) that match query conditions. Populated only if &#x60;return_entries&#x60; in the request is set to &#x60;false&#x60;. | [optional] 
**cursor** | **str** | The pagination cursor to be used in a subsequent request. If unset, this is the final response. See [Pagination](/basics/api101/pagination) for more information. | [optional] 
**errors** | [**list[Error]**](Error.md) | [Errors](#type-error) encountered during the search. | [optional] 
**unconvertible_transaction_ids** | **list[str]** | List of transaction IDs identifying transactions that could not be converted to an &#x60;Order&#x60;. Empty if &#x60;return_entries&#x60; is true, however, attempts to retrieve those orders may encounter subsequent &#x60;unconvertible_transcation_ids&#x60; Note that this field will not be present after SearchOrders moves from BETA to GA. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


