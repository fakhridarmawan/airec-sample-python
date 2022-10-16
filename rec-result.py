#! /usr/bin/env python
#coding=utf-8

# Obtain recommendation results.
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
client = AcsClient('accesskeyid', 'accesskeysecret', 'ap-southeast-1')

request = CommonRequest()
request.set_accept_format('json')
request.set_method('GET')
request.set_protocol_type('https') # https | http
request.set_domain('airec.ap-southeast-1.aliyuncs.com')
request.set_version('2020-11-26')

# You must specify the scene ID and the number of returned results. You must specify the user ID or IMEI.
request.add_query_param('returnCount', "2")
request.add_query_param('userId', "1")
request.add_query_param('sceneId', "1")
request.add_header('Content-Type', 'application/json')
request.set_uri_pattern('/v2/openapi/instances/INSTANCEID/actions/recommend')
body = '''{}'''
request.set_content(body.encode('utf-8'))

response = client.do_action_with_exception(request)

# python2:  print(response) 
print(str(response, encoding = 'utf-8'))