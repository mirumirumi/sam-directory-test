from common import say
import requests


def lambda_handler(event, context):
    print("hello")

    print(say.call())

    print(requests)

    return
