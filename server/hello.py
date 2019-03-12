from flask import Flask
from werkzeug.contrib.cache import MemcachedCache
cache = MemcachedCache(['cache:11211'])

app = Flask(__name__)

@app.route('/')
def hello():
    visits = cache.get('visits')    
    
    if visits is None:
      visits=0

    visits+=1
    cache.set('visits', visits, timeout=5 * 60)

    return 'visits {}'.format(visits)