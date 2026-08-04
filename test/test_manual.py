
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
from manticoresearch.models import *
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
        
        utilsApi.sql('query=DROP TABLE IF EXISTS movies')
        utilsApi.sql('DROP TABLE IF EXISTS movies_uuid')
        res = utilsApi.sql("CREATE TABLE IF NOT EXISTS movies (title text, plot text, _year integer, rating float, code multi) min_infix_len='2'")
        utilsApi.sql("CREATE TABLE IF NOT EXISTS movies_uuid (id uuid, title text)")
        
        docs = [ \
            {"insert": {"table" : "movies", "id" : 1, "doc" : {"title" : "Star Trek 2: Nemesis", "plot": "The Enterprise is diverted to the Romulan homeworld Romulus, supposedly because they want to negotiate a peace treaty. Captain Picard and his crew discover a serious threat to the Federation once Praetor Shinzon plans to attack Earth.", "_year": 2002, "rating": 6.4, "code": [1,2,3]}}}, \
            {"insert": {"table" : "movies", "id" : 2, "doc" : {"title" : "Star Trek 1: Nemesis", "plot": "The Enterprise is diverted to the Romulan homeworld Romulus, supposedly because they want to negotiate a peace treaty. Captain Picard and his crew discover a serious threat to the Federation once Praetor Shinzon plans to attack Earth.", "_year": 2001, "rating": 6.5, "code": [1,12,3]}}},
            {"insert": {"table" : "movies", "id" : 3, "doc" : {"title" : "Star Trek 3: Nemesis", "plot": "The Enterprise is diverted to the Romulan homeworld Romulus, supposedly because they want to negotiate a peace treaty. Captain Picard and his crew discover a serious threat to the Federation once Praetor Shinzon plans to attack Earth.", "_year": 2003, "rating": 6.6, "code": [11,2,3]}}}, \
            {"insert": {"table" : "movies", "id" : 4, "doc" : {"title" : "Star Trek 4: Nemesis", "plot": "The Enterprise is diverted to the Romulan homeworld Romulus, supposedly because they want to negotiate a peace treaty. Captain Picard and his crew discover a serious threat to the Federation once Praetor Shinzon plans to attack Earth.", "_year": 2003, "rating": 6.5, "code": [1,2,4]}}},
            {"insert": {"table" : "movies_uuid", "id" : "550e8400-e29b-41d4-a716-446655440000", "doc" : {"title" : "uuid doc"}}},
        ]
        indexApi.bulk('\n'.join(map(json.dumps,docs)))
        
        search_request = SearchRequest(
            table="movies",
        )

        matchFilter = QueryFilter() 
        matchFilter.match = {"title":"4"}
        mustCond = [ matchFilter ]
        boolFilter = BoolFilter(must=mustCond)
        searchQuery = SearchQuery(bool={"must": [ {"match": {"title":"4"}}] })
        search_request.query = searchQuery

        res = searchApi.search(search_request)
        self.assertEqual(res.hits.hits[0].id, 4)
        self.assertIsNone(res.hits.hits[0].uuid)

        search_request = {"table":"movies","query":{"bool": {"must": [ {"match": {"title":"4"}}] }}}

        res = searchApi.search(search_request)
        self.assertEqual(res.hits.hits[0].id, 4)
        self.assertIsNone(res.hits.hits[0].uuid)

        res = searchApi.search({"table": "movies_uuid", "query": {"match_all": {}}})
        self.assertIsNone(res.hits.hits[0].id)
        self.assertEqual(res.hits.hits[0].uuid, "550e8400-e29b-41d4-a716-446655440000")

        autocomplete_request = {"table":"movies","query": "Romul","options": {"fuzziness": 0, "layouts": "us,uk"} }

        res = searchApi.autocomplete(autocomplete_request)
        self.assertEqual(res[0]['total'], 2)
        self.assertEqual(res[0]['data'][0]['query'], 'romulan')
        self.assertEqual(res[0]['data'][1]['query'], 'romulus')

        pprint("Tests finished")
        
if __name__ == '__main__':
    unittest.main()
