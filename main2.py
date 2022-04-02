"""
Simple script that creates a FastAPI app and defines a POST method that takes one path parameter, one query parameter,
and a request body containing a single field.
"""

from typing import Union, List
from fastapi import FastAPI
from pydantic import BaseModel


class Value(BaseModel):
    value: int


app = FastAPI()


@app.post("/{path}")
async def exercise_function(path: int, query: int, body: Value):
    return {"path": path, "query": query, "body": body}
