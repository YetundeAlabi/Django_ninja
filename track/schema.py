from datetime import date
from typing import List
from pydantic import Field
from ninja import Query, Schema
from ninja import Schema

class EmployeeIn(Schema):
    first_name: str
    last_name: str
    department_id: int = None
    birthdate: date = None


class EmployeeOut(Schema):
    id: int
    first_name: str
    last_name: str
    department_id: int = None
    birthdate: date = None


# class Filters(Schema):
#     limit: int = 100
#     offset: int = None
#     query: str = None
#     category__in: List[str] = Field(None, alias="categories")


# @api.get("/filter")
# def events(request, filters: Filters = Query(...)):
#     return {"filters": filters.dict()}