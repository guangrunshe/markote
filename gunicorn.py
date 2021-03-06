import os


bind = '0.0.0.0:5000'
accesslog = 'app.log'
access_log_format = \
    '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
raw_env = [
    'GRAPH_CLIENT_ID=' + os.getenv('GRAPH_CLIENT_ID'),
    'GRAPH_CLIENT_SECRET=' + os.getenv('GRAPH_CLIENT_SECRET')
]
