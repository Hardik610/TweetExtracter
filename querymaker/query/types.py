from .query import Query
from elasticsearch_dsl import Q

# For contains
class MultiMatch(Query):
    def __init__(self, query, fields):
        self.query = query
        fields = fields or "_all"
        self.fields = fields if type(fields) == list else [fields]

    def build(self):
        q = Q("multi_match", query=self.query, fields=self.fields)
        return q

    @classmethod
    def instantiate(cls, **kwargs):
        return cls(kwargs.get('query'), kwargs.get('fields'))


# For eq, gt, gte, lt, lte
class Range(Query):
    def __init__(self, query, fields, operator):
        self.operator = operator
        self.query = query
        self.fields = fields if type(fields)==list else [fields]

    def build(self):
        criterion = {
            self.fields[0]: {
                self.operator: self.query
            }
        }
        # Range(** {'@timestamp': {'lt': 'now'}})
        q = Q("range", **criterion)
        return q

    @classmethod
    def instantiate(cls, **kwargs):
        return cls(kwargs.get('query'), kwargs.get('fields'), kwargs.get('operator'))


# For equals
class Term(Query):
    def __init__(self, query, fields):
        self.query = query
        self.fields = fields if type(fields)==list else [fields]

    def build(self):
        criterion = {self.fields[0]+".raw": self.query}
        #Q('term', category='meetup')
        q = Q("term", **criterion)
        return q

    @classmethod
    def instantiate(cls, **kwargs):
        return cls(kwargs.get('query'), kwargs.get('fields'))


# For startswith, endswith, wildcard
class Wildcard(Query):
    def __init__(self, query, fields):
        self.query = query
        self.fields = fields if type(fields)==list else [fields]

    def build(self):
        criterion = {self.fields[0]+".raw": self.query}
        #Q('term', category='meetup')
        q = Q("wildcard", **criterion)
        return q

    @classmethod
    def instantiate(cls, **kwargs):
        return cls(kwargs.get('query'), kwargs.get('fields'))