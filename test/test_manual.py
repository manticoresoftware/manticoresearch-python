# coding: utf-8
from __future__ import absolute_import
from pprint import pprint
import unittest
import json
import manticoresearch
from manticoresearch.api.index_api import IndexApi  # noqa: E501
from manticoresearch.rest import ApiException
from parametrized_test_case import ParametrizedTestCase

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
        utilsApi.sql('mode=raw&query=SHOW THREADS')
        utilsApi.sql('mode=raw&query=DROP TABLE IF EXISTS products')
        # example create_example request
        res = utilsApi.sql('mode=raw&query=CREATE TABLE IF NOT EXISTS products (title text, price float, sizes multi, meta json, coeff float, tags1 multi, tags2 multi)')
        pprint(res)
        res = utilsApi.sql('mode=raw&query=TRUNCATE TABLE products')
        # example create_example response
        #
        #
        #
        print(res)
        self.assertEqual(res['error'],'')
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
        res = utilsApi.sql('mode=raw&query=TRUNCATE TABLE products')
        pprint(res)
        
        #
        
        res = utilsApi.sql('mode=raw&query=SHOW TABLES LIKE \'pro%\'')
        pprint(res)
        
        #
        res = utilsApi.sql('mode=raw&query=drop table forum')
        utilsApi.sql('mode=raw&query=create table forum(title text, content text, author_id int, forum_id int, post_date timestamp) min_infix_len=\'3\'')
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
        utilsApi.sql('mode=raw&query=DROP TABLE products')
        res = utilsApi.sql('mode=raw&query=CREATE TABLE IF NOT EXISTS products (title text,product_codes multi)')
        
        res = indexApi.insert({"index":"products","id":1,"doc":{"title":"first","product_codes":[4,2,1,3]}})
        pprint(res)
        res = searchApi.search({"index":"products","query":{"match_all":{}}})
        pprint(res)
        utilsApi.sql('mode=raw&query=DROP TABLE products')
        
        #
        
        res =  utilsApi.sql('mode=raw&query=SHOW AGENT STATUS')
        pprint(res)
        
        # example create percolate request
        
        #utilsApi.sql('mode=raw&query=create table products(title text, color string) type=\'pq\'')
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
        #utilsApi.sql('mode=raw&query=DROP TABLE products')
        
        
        #res =  searchApi.search({"index":"books","query":{"match":{"*":"try"}},"highlight":{}})
        #pprint(res)
        
        
if __name__ == '__main__':
    unittest.main()
