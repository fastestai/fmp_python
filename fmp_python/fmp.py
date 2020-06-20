import pandas as pd
import requests
import os
import io
from fmp_python.constants import BASE_URL
from fmp_python.constants import INDEX_PREFIX
from fmp_python.common.requestbuilder import RequestBuilder


class FMP(object):
    """
    Base class that implements  api calls 
    """

    class FMPException(Exception):
        pass

    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('FMP_API_KEY')


    #@format_data
    def get_quote_short(self, symbol, data_format):
        rb = RequestBuilder()
        rb.set_category('quote-short')
        rb.add_sub_category(symbol)
        quote = requests.get(rb.compile_request())
        return quote
    
    def get_quote(self,symbol):
        rb = RequestBuilder()
        rb.set_category('quote')
        rb.add_sub_category(symbol)
        quote = requests.get(rb.compile_request())
        return quote

    def get_index_quote(self,symbol):
        return FMP.get_quote(self,INDEX_PREFIX+symbol)

   
