#!/usr/bin/python

import pdb
import random
 
def get_data():
    """Return 3 random integers between 0 and 9"""
    return random.sample(range(10), 3)
 
def consume():
    """Displays a running average across lists of integers sent to it"""
    running_sum = 0
    data_items_seen = 0
 
    while True:
        data = yield
        data_items_seen += len(data)
        running_sum += sum(data)
        print('The running average is {}'.format(running_sum / float(data_items_seen)))
# formater or %s, etc 

def produce(consumer):
    """Produces a set of values and forwards them to the pre-defined consumer
    function"""
    while True:
        data = get_data()
        print('Produced {}'.format(data))
        consumer.send(data)
        yield
 
# the send method is very hard to debug
# always need to find a alternative way
if __name__ == '__main__':
    consumer = consume()
    pdb.set_trace()
    consumer.send(None)
    producer = produce(consumer)
 
    for _ in range(10):
        print('Producing...')
        #producer.next()
        next(producer)
