from common import say


def lambda_handler(event, context):
    print("send")

    print(say.call())

    return
