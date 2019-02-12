import boto3
import json
# import datetime
# from datetime import timezone

import logging
# import boto3
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

print('YO')



def handler(event, context):
    print( 'HELLO FROM PYTHON - consuming')
    print(json.dumps('HELLO FROM PYTHON - consuming'))
    file = open("testfile.txt","w")
    file.write("Hello World")
    file.close()
    incoming_payload = event["Records"][0]["Sns"]["Message"]
    print("incoming_payload:")
    print(incoming_payload)
    # for record in event["Records"]:
        # print(record["Sns"])
        # message = json.loads(record["Sns"]["Message"])
        # print("message", message)
    print("is offline?", os.getenv("IS_OFFLINE"))
    if os.getenv("IS_OFFLINE"):
        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html#boto3.session.Session.client
        # end point should work offline, but doesn't seem to 
        sns = boto3.client('sns', endpoint_url="http://127.0.0.1:4002")
    else:
        sns = boto3.client('sns')

    topic_arn = os.getenv("starterSnsTopic")
    print('topic arn', topic_arn)
    # don't actually just pass it blindly of course
    params = {'default':'blarggggg', "passed_from_publish": incoming_payload}
    # params =
    # context_parts = context.invoked_function_arn.split(':')
    # topic_name = "marks-blog-topic"
    # topic_arn = "arn:aws:sns:{region}:{account_id}:{topic}".format(
    #     region=context_parts[3], account_id=context_parts[4], topic=topic_name)

    # now = datetime.datetime.now(timezone.utc)
    # start_date = (now - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    # end_date = now.strftime("%Y-%m-%d")
    #
    # params = {"startDate": start_date, "endDate": end_date, "tags": ["neo4j"]}

    sns.publish(TopicArn= topic_arn, Message= json.dumps(params))

    # MessageStructure= "json",
