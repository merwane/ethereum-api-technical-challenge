from resources.block import block_details
from flask import abort
import datetime

# finds the blocktime for a specific block returning timestamp
# converts timestamp epoch to date object
def block_to_time(block_number):
    details = block_details(block_number)
    timestamp = details["timestamp"]
    date = datetime.datetime.fromtimestamp(timestamp)
    return date

# formats date object to string
def dateobj_to_formatted(dateobj):
    formatted = dateobj.strftime('%Y-%m-%d %H:%M:%S')
    return formatted

# formats string date to date object
def str_to_dateobj(datestr):
    dateobj = datetime.datetime.strptime(datestr, '%Y-%m-%d')
    return dateobj

# formats date object to timestamp (epoch)
def dateobj_to_epoch(dateobj):
    epoch = datetime.datetime.timestamp(dateobj)
    return epoch

# returns a paginated list when given an array or dict
def get_paginated_list(results, url, start, limit):
    start = int(start)
    limit = int(limit)
    count = len(results)
    if count < start or limit < 0:
        abort(404)
    # make response
    obj = {}
    obj['start'] = start
    obj['limit'] = limit
    obj['count'] = count
    # make URLs
    # make previous url
    if start == 1:
        obj['previous'] = ''
    else:
        start_copy = max(1, start - limit)
        limit_copy = start - 1
        obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
    # make next url
    if start + limit > count:
        obj['next'] = ''
    else:
        start_copy = start + limit
        obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
    # finally extract result according to bounds
    obj['results'] = results[(start - 1):(start - 1 + limit)]
    return obj