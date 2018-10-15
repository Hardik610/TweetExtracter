class Query(object):
    MULTIMATCH = "MULTIMATCH"
    TERM = "TERM"
    WILDCARD = "WILDCARD"
    RANGE = "RANGE"

    @classmethod
    def instantiate(cls, query_type_str, **kwargs):
        query_type = Query.get_mapping(query_type_str)
        return query_type.instantiate(**kwargs)

    @classmethod
    def get_mapping(cls, query_type_str):
        from .types import MultiMatch,Range,Term,Wildcard
        query_type_mapping = {
            "MULTIMATCH": MultiMatch,
            "TERM": Term,
            "WILDCARD": Wildcard,
            "RANGE": Range
        }
        return query_type_mapping[query_type_str]