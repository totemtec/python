import json
import time

import numpy as np
import pandas as pd
import redis
import requests
from redis.commands.search.field import (
    NumericField,
    TagField,
    TextField,
    VectorField,
)
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import Query
from sentence_transformers import SentenceTransformer

url = "https://raw.githubusercontent.com/bsbodden/redis_vss_getting_started/main/data/bikes.json"
response = requests.get(url)
bikes = response.json()

json.dumps(bikes[0], indent=2)

client = redis.Redis(host="demo.totemtec.com", port=6379, decode_responses=True, password="PASSWORD")

res = client.ping()
# >>> True

# pipeline = client.pipeline()
# for i, bike in enumerate(bikes, start=1):
#     redis_key = f"bikes:{i:03}"
#     pipeline.json().set(redis_key, "$", bike)
#  res = pipeline.execute()
# # >>> [True, True, True, True, True, True, True, True, True, True, True]

res = client.json().get("bikes:010", "$.brand")
# >>> ['Summit']


exit()