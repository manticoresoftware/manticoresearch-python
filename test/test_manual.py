
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
        res = utilsApi.sql("CREATE TABLE IF NOT EXISTS movies (title text, plot text, _year integer, rating float, code multi) min_infix_len='2'")
        
        docs = [ \
            {"insert": {"table" : "movies", "id" : 1, "doc" : {"title" : "Star Trek 2: Nemesis", "plot": "The Enterprise is diverted to the Romulan homeworld Romulus, supposedly because they want to negotiate a peace treaty. Captain Picard and his crew discover a serious threat to the Federation once Praetor Shinzon plans to attack Earth.", "_year": 2002, "rating": 6.4, "code": [1,2,3]}}}, \
            {"insert": {"table" : "movies", "id" : 2, "doc" : {"title" : "Star Trek 1: Nemesis", "plot": "The Enterprise is diverted to the Romulan homeworld Romulus, supposedly because they want to negotiate a peace treaty. Captain Picard and his crew discover a serious threat to the Federation once Praetor Shinzon plans to attack Earth.", "_year": 2001, "rating": 6.5, "code": [1,12,3]}}},
            {"insert": {"table" : "movies", "id" : 3, "doc" : {"title" : "Star Trek 3: Nemesis", "plot": "The Enterprise is diverted to the Romulan homeworld Romulus, supposedly because they want to negotiate a peace treaty. Captain Picard and his crew discover a serious threat to the Federation once Praetor Shinzon plans to attack Earth.", "_year": 2003, "rating": 6.6, "code": [11,2,3]}}}, \
            {"insert": {"table" : "movies", "id" : 4, "doc" : {"title" : "Star Trek 4: Nemesis", "plot": "The Enterprise is diverted to the Romulan homeworld Romulus, supposedly because they want to negotiate a peace treaty. Captain Picard and his crew discover a serious threat to the Federation once Praetor Shinzon plans to attack Earth.", "_year": 2003, "rating": 6.5, "code": [1,2,4]}}},
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
        pprint(res)

        search_request = {"table":"movies","query":{"bool": {"must": [ {"match": {"title":"4"}}] }}}

        res = searchApi.search(search_request)
        pprint(res)

        autocomplete_request = {"table":"movies","query": "Romul","options": {"fuzziness": 0, "layouts": "us,uk"} }

        res = searchApi.autocomplete(autocomplete_request)
        pprint(res)

        pprint("Tests finished")
        
if __name__ == '__main__':
    unittest.main()
