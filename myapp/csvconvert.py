import json
import pyexcel as pe
import StringIO # py2.7, for python3, please use import io
from flask import make_response
import sys

reload(sys)
sys.setdefaultencoding('utf8')

""" Converts Json to csv """
def json_to_csv(res):
    
    d = []
    l  = len(res["results"])
    d.append((res["results"][0]["_source"]).keys())
    for i in range(l):
        d.append((res["results"][i]["_source"]).values())

    sheet = pe.Sheet(d)
    io = StringIO.StringIO()
    sheet.save_to_memory("csv", io)
    output = make_response(io.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=convert.csv"
    output.headers["Content-type"] = "text/csv"
    return output