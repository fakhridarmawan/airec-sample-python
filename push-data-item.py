#! /usr/bin/python
# coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkairec.request.v20201126.PushDocumentRequest import PushDocumentRequest

# Create a client of the AcsClient class.
client = AcsClient(
    ak="accesskeyid",
    secret="accesskeysecret",
    #Enter the region. If the region is China (Beijing), enter cn-beijing.
    region_id="ap-southeast-1"
)
# Configure the endpoint.
# Specify the region ID, service name, and endpoint.
client.add_endpoint("ap-southeast-1", "Airec", "airec.ap-southeast-1.aliyuncs.com")
# Create a request and configure parameters.
# Create a request for a specific API operation. The class of the request is named by adding Request to the end of the API operation name.
# For example, the name of the API operation that is used to obtain pushed documents is PushDocument. In this case, the name of the request class is PushDocumentRequest.
request = PushDocumentRequest()
request.set_instanceId("INSTANCEID")
request.set_tableName("item")
# Configure parameters for the request.
content = "[{ \
        \"cmd\": \"add\", \
        \"fields\": { \
            \"item_id\": \"115\", \
            \"item_type\": \"article\", \
            \"status\": \"1\", \
            \"scene_id\": \"1\", \
            \"title\": \"test-115\", \
            \"content\": \"Content\", \
            \"pub_time\": \"1590327038\" \
        } \
    }]"

request.set_content(content)
request.set_content_type("application/json")
# Initiate the request by using the method that is supported by the client, obtain the response, and handle the exception.
try:
    response = client.do_action_with_exception(request)
    print(response)
except ClientException as e:
    print(e)
except ServerException as e:
    print(e)