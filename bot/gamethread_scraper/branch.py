import branchio
import os

client = branchio.Client(os.environ["BRANCH_KEY"])

def createURL(thread):
    data = {
        "threadId": thread.id
    }
    response = client.create_deep_link_url(data=data, channel="facebook")
    return response[branchio.RETURN_URL]
