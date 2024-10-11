This release includes:

- added support for KNN search 

- added support for search with joined tables

- updated sql request and error response formats to match changes in Manticore

- BREAKING CHANGES: updated the structure of client classes to strictly match the request/response formats specified by Manticore's JSON API 
  (Related Github issue: https://github.com/manticoresoftware/openapi/issues/16)

  - added classes:
    - [AggCompositeSource](./docs/AggCompositeSource.md)
      More on aggregation: https://manual.manticoresearch.com/dev/Searching/Grouping#GROUP-BY-multiple-fields-at-once
    - [AggCompositeTerm](./docs/AggCompositeTerm.md)
      More on aggregation: https://manual.manticoresearch.com/dev/Searching/Grouping#GROUP-BY-multiple-fields-at-once
    - [HighlightFieldOption](./docs/HighlightFieldOption.md)
      More on highlighting: https://manual.manticoresearch.com/dev/Searching/Highlighting#Highlighting-via-HTTP
    - [Join](./docs/Join.md)
      More on joining tables: https://manual.manticoresearch.com/dev/Searching/Joining#Joining-tables
    - [JoinOn](./docs/JoinOn.md)
      More on joining tables: https://manual.manticoresearch.com/dev/Searching/Joining#Joining-tables
    - [JoinCond](./docs/JoinCond.md)
      More on joining tables: https://manual.manticoresearch.com/dev/Searching/Joining#Joining-tables
    - [KnnQuery](./docs/KnnQuery.md)
      More on KNN search: https://manual.manticoresearch.com/dev/Searching/KNN#KNN-vector-search
    - [ResponseErrorDetails](./docs/ResponseErrorDetails.md)
    - [ResponseError](./docs/ResponseError.md)
    - [SearchQuery](./docs/SearchQuery.md)
      More on searching: https://manual.manticoresearch.com/dev/Searching/Intro#General-syntax    
  
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
      More on aggregation: https://manual.manticoresearch.com/dev/Searching/Grouping#GROUP-BY-multiple-fields-at-once
    - GeoDistanceFilterLocationAnchor -> [GeoDistanceLocationAnchor](./docs/GeoDistanceLocationAnchor.md)
      More on geo filtering: https://manual.manticoresearch.com/dev/Searching/Filters#location_anchor
    - GeoDistanceFilter -> [GeoDistance](./docs/GeoDistance.md)
      More on geo filtering: https://manual.manticoresearch.com/dev/Searching/Filters#Geo-distance-filters
    - SourceByRules -> [SourceRules](./docs/SourceRules.md)
      More on the 'source' property:
      https://manual.manticoresearch.com/dev/Searching/Search_results#Source-selection

- updated documentation