twitter_config = {
  "access_token" : "554353771-Kjvz1ihaCpu3n4VKD4NPraulMKbMTGfHvwSaTHFr",
  "access_token_secret" : "yROO4XkoxBZfYSe5FUhHyLOSiOLvzKjtF5fBAOIXRlUn2",
  "consumer_key" : "yP15Wr9lowfWq0JC2wfUsWoo0" ,
  "consumer_secret" : "uVBN5plyFHl87DoMBN8buCpZPMsQ928FDUSovyRtkMVA6Ywg6t",
}


mappings = {
    "tweet_index": {
        "mappings": {
            "tweet": {
                "properties": {
                    "timestamp_ms": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "hashtags": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "created_at": {
                      "type": "datetime",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "datetime"
                        }
                      }
                    },
                    "screen_name": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "user_name": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "location": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "source_device": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "country": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "country_code": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "tweet_text": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "lang": {
                  "type": "string",
                  "fields": {
                    "raw": {
                      "index": "not_analyzed",
                      "type": "string"
                    }
                  }
                }
                }
            }
        }
    }

}