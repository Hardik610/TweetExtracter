from flask import Flask,request,jsonify
import json
from querymaker.query_builder import QueryBuilder	


def common():
	elasticsearch_size = int(request.args.get('size',100))
	elasticsearch_from = int(request.args.get('from',0))
	data = json.loads(request.data)
	criteria =  data.get('criteria')
	sort = data.get('sort')
	s = QueryBuilder(criteria).search(index='tweets_index', doc_type='tweet')
	if sort:
		s=s.sort(*sort)
	s=s[elasticsearch_from:elasticsearch_size]
	try:
		elasticsearch_result=QueryBuilder.execute(s)
	except Exception:
		result = {
			"status" : "failure"
		}
		return result
	result = dict()
	if elasticsearch_result is not None:
		hits = elasticsearch_result.hits
		result["count"] = {"total": hits.total, "fetched": len(hits.hits) }
		result["results"] = hits.hits
	return result