This release includes:

- added support for KNN vector search 

- added support for search with joined tables

- updated sql request and error response formats to match changes in Manticore

- BREAKING CHANGES: updated the structure of client classes to strictly match the request/response formats specified by Manticore's JSON API 
  (Related Github issue: https://github.com/manticoresoftware/openapi/issues/16)

  - added classes:
    - [AggCompositeSource](./docs/AggCompositeSource.md), [AggCompositeTerm](./docs/AggCompositeTerm.md) - handle search aggregations
        [More on aggregation](https://manual.manticoresearch.com/dev/Searching/Grouping#GROUP-BY-multiple-fields-at-once)
    - [HighlightFieldOption](./docs/HighlightFieldOption.md) - handles highlighting per-field options
        [More on highlighting](https://manual.manticoresearch.com/dev/Searching/Highlighting#Highlighting-via-HTTP)
    - [Join](./docs/Join.md), [JoinOn](./docs/JoinOn.md), [JoinCond](./docs/JoinCond.md) - handle joining tables 
        [More on joining tables](https://manual.manticoresearch.com/dev/Searching/Joining#Joining-tables)
    - [KnnQuery](./docs/KnnQuery.md) - handles KNN search
        [More on KNN search](https://manual.manticoresearch.com/dev/Searching/KNN#KNN-vector-search)
    - [ResponseErrorDetails](./docs/ResponseErrorDetails.md), [ResponseError](./docs/ResponseError.md) - handle Manticore error responses
    - [SearchQuery](./docs/SearchQuery.md) - handles search queries
        [More on searching](https://manual.manticoresearch.com/dev/Searching/Intro#General-syntax)    
  
  - removed classes:
    - AggregationCompositeSourcesInnerValue
    - AggregationCompositeSourcesInnerValueTerms
    - AggregationSortInnerValue
    - AttrFilter
    - EqualsFilter
    - Facet
    - FilterBoolean
    - FilterNumber
    - FilterString
    - HighlightField
    - InFilter
    - MatchFilter
    - MatchOpFilter
    - MatchOp
    - MatchPhraseFilter
    - NotFilterBoolean
    - NotFilterNumber
    - NotFilterString
    - Option
    - RangeFilterLte
    - RangeFilter
    - SortMultiple
    - SortMva
    - SortOrder
    - SourceMultiple
    
  - renamed classes:
    - AggregationTerms -> [AggTerms](./docs/AggTerms.md)
        [More on aggregation](https://manual.manticoresearch.com/dev/Searching/Grouping#GROUP-BY-multiple-fields-at-once)
    - GeoDistanceFilterLocationAnchor -> [GeoDistanceLocationAnchor](./docs/GeoDistanceLocationAnchor.md)
    - GeoDistanceFilter -> [GeoDistance](./docs/GeoDistance.md)
        [More on geo filtering](https://manual.manticoresearch.com/dev/Searching/Filters#Geo-distance-filters)
    - SourceByRules -> [SourceRules](./docs/SourceRules.md)
        [More on the 'source' property](https://manual.manticoresearch.com/dev/Searching/Search_results#Source-selection)

- updated documentation