# coding: utf-8
# Manticore Search Client
# Copyright (c) 2020-2021, Manticore Software LTD (https://manticoresearch.com)
#
# All rights reserved

from __future__ import absolute_import
from pprint import pprint
import unittest
import json
import manticoresearch
from manticoresearch.api.index_api import IndexApi  # noqa: E501
from manticoresearch.model import *
from manticoresearch.rest import ApiException
from parametrized_test_case import ParametrizedTestCase
from urllib.parse import quote
import sys

class TestManualApi(ParametrizedTestCase):

    def setUp(self):
        self.client = manticoresearch.ApiClient(self.settings['configuration'])
        
    def tearDown(self):
        pass
        
    def test_manual(self):
        client = self.client
        indexApi = manticoresearch.IndexApi(client)
        utilsApi = manticoresearch.UtilsApi(client)
        searchApi = manticoresearch.SearchApi(client)
        
        utilsApi.sql('DROP TABLE IF EXISTS movies')
        res = utilsApi.sql('CREATE TABLE IF NOT EXISTS movies (title text, plot text, year integer, rating float, code multi)')
        
        docs = [ \
            {"insert": {"index" : "movies", "id" : 1, "doc" : {"title" : "Star Trek 2: Nemesis", "plot": "The Enterprise is diverted to the Romulan homeworld Romulus, supposedly because they want to negotiate a peace treaty. Captain Picard and his crew discover a serious threat to the Federation once Praetor Shinzon plans to attack Earth.", "year": 2002, "rating": 6.4, "code": [1,2,3]}}}, \
            {"insert": {"index" : "movies", "id" : 2, "doc" : {"title" : "Star Trek 1: Nemesis", "plot": "The Enterprise is diverted to the Romulan homeworld Romulus, supposedly because they want to negotiate a peace treaty. Captain Picard and his crew discover a serious threat to the Federation once Praetor Shinzon plans to attack Earth.", "year": 2001, "rating": 6.5, "code": [1,12,3]}}},
            {"insert": {"index" : "movies", "id" : 3, "doc" : {"title" : "Star Trek 3: Nemesis", "plot": "The Enterprise is diverted to the Romulan homeworld Romulus, supposedly because they want to negotiate a peace treaty. Captain Picard and his crew discover a serious threat to the Federation once Praetor Shinzon plans to attack Earth.", "year": 2003, "rating": 6.6, "code": [11,2,3]}}}, \
            {"insert": {"index" : "movies", "id" : 4, "doc" : {"title" : "Star Trek 4: Nemesis", "plot": "The Enterprise is diverted to the Romulan homeworld Romulus, supposedly because they want to negotiate a peace treaty. Captain Picard and his crew discover a serious threat to the Federation once Praetor Shinzon plans to attack Earth.", "year": 2003, "rating": 6.5, "code": [1,2,4]}}},
        ]
        indexApi.bulk('\n'.join(map(json.dumps,docs)))
        
        search_request = SearchRequest(
            index="movies",
            query={"match_all": {}}
        ) 
        
        res = searchApi.search(search_request)

        search_request.index = 'movies'
        search_request.limit = 10
        search_request.track_scores = True
        search_request.options = {'cutoff': 5}
        search_request.options['ranker'] = 'bm25'
        search_request.source = 'title'

        res = searchApi.search(search_request)
        
        search_request.source = SourceByRules()
        search_request.source.includes = ['title', 'year']
        search_request.source.excludes = ['code']

        res = searchApi.search(search_request)

        search_request.sort = ['year']
        sort2 = manticoresearch.model.SortOrder('rating', 'asc')
        sort3 = manticoresearch.model.SortMVA('code', 'desc', 'max')
        search_request.sort += [sort2,sort3]
        
        res = searchApi.search(search_request)

        expr = {'expr': 'min(year,2900)'}
        search_request.expressions = [expr]
        search_request.expressions += [ {'expr2': 'max(year,2100)'} ]
        search_request.source.includes += ['expr2']
        
        res = searchApi.search(search_request)

        agg1 = Aggregation('agg1', 'year', 10)
        search_request.aggs = [agg1]
        search_request.aggs += [ Aggregation('agg2', 'rating') ]
        
        res = searchApi.search(search_request)

        highlight = manticoresearch.model.Highlight()
        highlight.fieldnames = ['title']
        highlight.post_tags = '</post_tag>'
        highlight.encoder = 'default'
        highlight.snippet_boundary = 'sentence'
        search_request.highlight = highlight 
        
        res = searchApi.search(search_request)

        highlightField = HighlightField('title')
        highlightField2 = HighlightField('plot', 5, 10)
        highlight.fields = [highlightField, highlightField2]
        search_request.highlight = highlight
        
        res = searchApi.search(search_request)

        highlight.highlight_query = {"match" : {"*": "Star"} };
        search_request.highlight = highlight

        res = searchApi.search(search_request)

        search_request.fulltext_filter = QueryFilter('Star Trek 2')

        res = searchApi.search(search_request)        

        search_request.fulltext_filter = MatchFilter('Nemesis', 'title')

        res = searchApi.search(search_request)

        search_request.fulltext_filter = MatchPhraseFilter('Star Trek 2', 'title')

        res = searchApi.search(search_request)

        search_request.fulltext_filter = MatchOpFilter('Enterprise test', 'title,plot', 'or') 
        
        res = searchApi.search(search_request)

        search_request.attr_filter = EqualsFilter('year', 2001)
        
        res = searchApi.search(search_request)

        inFilter = InFilter('year', [2001, 2002])
        inFilter.values += [10,11]
        search_request.attr_filter = inFilter
        
        res = searchApi.search(search_request)

        rangeFilter = RangeFilter('year', lte = 2002)
        rangeFilter.gte = 1000
        search_request.attr_filter = rangeFilter

        res = searchApi.search(search_request)
        
        rangeFilter = RangeFilter('rating')
        rangeFilter.gt = 2000.5
        rangeFilter.lt = 2002
        search_request.attr_filter = rangeFilter

        res = searchApi.search(search_request)

        geoFilter = GeoDistanceFilter(location_anchor={'lat':10,'lon':20.5}, location_source='year,rating')
        geoFilter.location_source='year,rating'
        geoFilter.distance_type='adaptive'
        geoFilter.distance='100 km'
        search_request.attr_filter = geoFilter
        
        res = searchApi.search(search_request)

        boolFilter = BoolFilter()
        boolFilter.must = [ EqualsFilter('year', 2001) ]
        boolFilter.must += [ RangeFilter('rating', lte = 20) ]
        search_request.attr_filter = boolFilter
        
        res = searchApi.search(search_request)

        boolFilter.must_not = [ EqualsFilter('year', 2001) ]
        
        res = searchApi.search(search_request)
        
        fulltext_filter = MatchFilter('Star', 'title')
        nestedBoolFilter = BoolFilter()
        nestedBoolFilter.should = [EqualsFilter('rating', 6.5), fulltext_filter]
        boolFilter.must = [nestedBoolFilter]
        
        res = searchApi.search(search_request)

        search_request.attr_filter = boolFilter
    
        res = searchApi.search(search_request)
        pprint(res)

        pprint("Search tests finished")
        
        utilsApi.sql('SHOW THREADS')
        utilsApi.sql('DROP TABLE IF EXISTS products')
        # example create_example request
        res = utilsApi.sql('CREATE TABLE IF NOT EXISTS products (title text, price float, sizes multi, meta json, coeff float, tags1 multi, tags2 multi)')
        pprint(res)
        # example not raw_response request
        res = utilsApi.sql('SELECT * FROM products', raw_response=False)
        pprint(res)
        res = utilsApi.sql('SELECT * FROM products', raw_response=True)
        pprint(res)
        res = utilsApi.sql('TRUNCATE TABLE products')
        # example create_example response
        #
        #
        #
        print(res)
        self.assertEqual(res[0]['error'],'')
        indexApi = api = manticoresearch.IndexApi(client)
        # example insert request
        indexApi.insert({"index" : "products", "id" : 1, "doc" : {"title" : "Crossbody Bag with Tassel", "price" : 19.85}})
        indexApi.insert({"index" : "products", "id" : 2, "doc" : {"title" : "Crossbody Bag with Tassel"}})
        indexApi.insert({"index" : "products", "id" : 0, "doc" : {"title" : "Yellow bag"}})
        # example autoid request
        indexApi.insert({"index" : "products", "id" : 0, "doc" : {"title" : "Yellow bag"}})
        # example bulk_insert request
        indexApi = api = manticoresearch.IndexApi(client)
        docs = [ \
            {"insert": {"index" : "products", "id" : 3, "doc" : {"title" : "Crossbody Bag with Tassel", "price" : 19.85}}}, \
            {"insert": {"index" : "products", "id" : 4, "doc" : {"title" : "microfiber sheet set", "price" : 19.99}}}, \
            {"insert": {"index" : "products", "id" : 5, "doc" : {"title" : "CPet Hair Remover Glove", "price" : 7.99}}}
        ]
        print('\n'.join(map(json.dumps,docs)))
        api_resp = indexApi.bulk('\n'.join(map(json.dumps,docs)))
        # example MVA_insert request
        indexApi = api = manticoresearch.IndexApi(client)
        indexApi.insert({"index" : "products", "id" : 0, "doc" : {"title" : "Yellow bag","sizes":[40,41,42,43]}})
        # example JSON_insert request
        indexApi = api = manticoresearch.IndexApi(client)
        indexApi.insert({"index" : "products", "id" : 0, "doc" : {"title" : "Yellow bag","meta":'{"size": 41, "color": "red"}'}})
        # example replace request
        api_resp = indexApi.replace({"index" : "products", "id" : 1, "doc" : {"title" : "document one","price":10}})

        # example replace response
        # {'created': False,
        # 'found': None,
        # 'id': 1,
        # 'index': 'products',
        # 'result': 'updated'}
        
        # example bulk_replace request
        docs = [ \
            {"replace": {"index" : "products", "id" : 1, "doc" : {"title" : "document one"}}}, \
            {"replace": {"index" : "products", "id" : 2, "doc" : {"title" : "document two"}}} ]
        api_resp = indexApi.bulk('\n'.join(map(json.dumps,docs)))
        
        # example bulk_replace response
        #{'error': None,
        #'items': [{u'replace': {u'_id': 1,
        #                 u'_index': u'products',
        #                 u'created': False,
        #                 u'result': u'updated',
        #                 u'status': 200}},
        #   {u'replace': {u'_id': 2,
        #                u'_index': u'products',
        #                 u'created': False,
        #                 u'result': u'updated',
        #                 u'status': 200}}]}
        
        # example update request
        api_resp = indexApi.update({"index" : "products", "id" : 1, "doc" : {"price":10}})
        pprint(api_resp)
        # example update respone
        # {'id': 1, 'index': 'products', 'result': 'updated', 'updated': None}
        
        # example update multiple attributes request
        api_resp = indexApi.update({"index" : "products", "id" : 1, "doc" : {
            "price": 100000000000,
            "coeff": 3465.23,
            "tags1": [3,6,4],
            "tags2": []}})
        pprint(api_resp)
        # example update multiple attributes respone
        # {'id': 1, 'index': 'products', 'result': 'updated', 'updated': None}
        
        
        
        # example partial JSON update request
        api_resp = indexApi.insert({"index" : "products", "id" : 100, "doc" : {"title" : "title", "meta" : {"tags":[1,2,3]}}})
        pprint(api_resp)
        api_resp = indexApi.update({"index" : "products", "id" : 100, "doc" : {
            "meta.tags[0]": 100}})
        pprint(api_resp)
        # example partial JSON update respone
        #{'created': True,
        #'found': None,
        #'id': 100,
        #'index': 'products',
        #'result': 'created'}
        #{'id': 100, 'index': 'products', 'result': 'updated', 'updated': None}      

        # example MVA empty update request
        api_resp = indexApi.update({"index" : "products", "id" : 1, "doc" : {"tags1": []}})
        pprint(api_resp)
        
        # example bulk by query request
        docs = [ \
            { "update" : { "index" : "products", "doc": { "coeff" : 1000 }, "query": { "range": { "price": { "gte": 1000 } } } } }, \
            { "update" : { "index" : "products", "doc": { "coeff" : 0 }, "query": { "range": { "price": { "lt": 1000 } } } } } ]
        api_resp = indexApi.bulk('\n'.join(map(json.dumps,docs)))
        pprint(api_resp)
        
        # example delete 2 request
        api_resp = indexApi.delete({"index" : "products", "query": { "match": { "*": "document" }}})
        pprint(api_resp)        
        
        # example delete 3 request
        api_resp = indexApi.delete({"index" : "products", "id" : 1})
        pprint(api_resp)      

        # example truncate request
        res = utilsApi.sql('TRUNCATE TABLE products')
        pprint(res)
        
        #
        
        res = utilsApi.sql('SHOW TABLES LIKE \'pro%\'')
        pprint(res)
        
        #
        res = utilsApi.sql('drop table if exists forum')
        utilsApi.sql('create table forum(title text, content text, author_id int, forum_id int, post_date timestamp) min_infix_len=\'3\'')
        # example filtered query request
        res = searchApi.search({"index":"forum","query":{"match_all":{},"bool":{"must":[{"equals":{"author_id":123}},{"in":{"forum_id":[1,3,7]}}]}},"sort":[{"post_date":"desc"}]})
        pprint(res)
        
        #
        print('HERE')
        indexApi.insert({"index" : "forum", "id" : 0, "doc" : {"title" : "i me"}})
        indexApi.insert({"index" : "forum", "id" : 0, "doc" : {"title" : "wayne","content":"hey"}})
        res = searchApi.search({"index":"forum","query":{"query_string":"i me"},"_source":{"excludes":["*"]},"limit":1,"profile":True})
        pprint(res)
        res = searchApi.search({"index":"forum","query":{"query_string":"@title way* @content hey"},"_source":{"excludes":["*"]},"limit":1,"profile":True})
        pprint(res)
        
        #
        utilsApi.sql('DROP TABLE products')
        res = utilsApi.sql('CREATE TABLE IF NOT EXISTS products (title text,product_codes multi)')
        
        res = indexApi.insert({"index":"products","id":1,"doc":{"title":"first","product_codes":[4,2,1,3]}})
        pprint(res)
        res = indexApi.insert({"index":"products","id":2,"doc":{"title":"second","product_codes":[5,6,8,7]}})
        res = searchApi.search({"index":"products","query":{"match_all":{}}})
        pprint(res)
        res = searchApi.search({"index":"products","query":{"match_all":{}}, "options":{"max_matches":1}})
        pprint(res)
        utilsApi.sql('DROP TABLE products')
        
        #
        
        res =  utilsApi.sql('SHOW AGENT STATUS')
        pprint(res)
        
        # example create percolate request
        
        #utilsApi.sql('create table products(title text, color string) type=\'pq\'')
        #res = indexApi.insert({"index" : "products", "doc" : {"query" : "@title bag" }})
        #pprint(res)
        #res = indexApi.insert({"index" : "products",  "doc" : {"query" : "@title shoes", "filters": "color='red'" }})
        #pprint(res)
        #res = indexApi.insert({"index" : "products",  "doc" : {"query" : "@title shoes","filters": "color in ('blue', 'green')" }})
        #pprint(res)
        
        #
        
        #res = searchApi.percolate('products',{"query":{"percolate":{"document":{"title":"What a nice bag"}}}})
        #pprint(res)
        #res = searchApi.percolate('products',{"query":{"percolate":{"documents":[{"title":"nice pair of shoes","color":"blue"},{"title":"beautiful bag"}]}}})
        #pprint(res)        
        #res = searchApi.search({"index":"products","query":{"match_all":{}}})
        #pprint(res)        
        #utilsApi.sql('DROP TABLE products')
        
        
        #res =  searchApi.search({"index":"books","query":{"match":{"*":"try"}},"highlight":{}})
        #pprint(res)
        
        pprint("Tests finished")
        
if __name__ == '__main__':
    unittest.main()
