import urllib3
import json

http = urllib3.PoolManager()

def lambda_handler(event, context):
    print("Calling Slack!!!")
    url = ""
    msg = {
        "channel" : "#aws-events",
        "text" : event["Records"][0]["Sns"]["Message"],
    }

    encode_msg = json.dumps(msg).encode('utf-8')
    resp = http.request('POST', url, body=encode_msg)
    print({
        "message": event["Records"][0]["Sns"]["Message"],
        "status_code": resp.status,
        "response": resp.data
    })