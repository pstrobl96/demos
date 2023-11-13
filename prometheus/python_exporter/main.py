import time
from prometheus_client import start_http_server, Counter, Gauge, Histogram
import random

c = Counter('my_counter', 'Description of counter', ["super_label", "hyper_label"])
g = Gauge('my_gauge', 'Description of gauge', ["super_label", "hyper_label"])
h = Histogram('my_histogram', 'Description of histogram', ["super_label", "hyper_label"])

def process_request():
    time.sleep(random.random())
    if random.randint(0,1) == 0:
        c.labels("one","mine").inc()
        c.labels("two","mine").inc(2)
        g.labels("set","mine").set(42)
    else:
        g.labels("set","mine").dec(10)

    for i in range(0,10):
        h.labels("demo", "mine").observe(random.random()*10)    
        h.labels("demo2", "mine").observe(random.random()*10)   
        h.labels("demo3", "mine").observe(random.random()*10)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request()