from typing import Union

from fastapi import FastAPI
from search_engine import Search_engine
import numpy as np

search_e = Search_engine()
search_app = FastAPI()

#TODO: implement fastapi server with the functionality of finding best matches for an incoming user embedding
