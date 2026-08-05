# FacetBucketStatus

Facet bucket availability marker returned when `facet_filter_mode` is `auto` or `max`. `selected` means the bucket value is already present in a same-facet value filter. `available` means selecting the bucket can produce results. `unavailable` means the bucket exists in the broad max count scope but selecting it would produce no results. 

## Enum

* `SELECTED` (value: `'selected'`)

* `AVAILABLE` (value: `'available'`)

* `UNAVAILABLE` (value: `'unavailable'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


