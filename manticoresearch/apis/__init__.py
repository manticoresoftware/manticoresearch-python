
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.index_api import IndexApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from manticoresearch.api.index_api import IndexApi
from manticoresearch.api.search_api import SearchApi
from manticoresearch.api.utils_api import UtilsApi
