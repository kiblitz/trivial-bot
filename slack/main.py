import os
from slack import WebClient
from slack.errors import SlackApiError

#instantiate Stack Client
slack_token = os.environ.get("SECRET_SLACK_BOT_TOKEN")
client = WebClient(token=slack_token)

#constants
prefix = "$"

if __name__ == "__main__":
  try:
    response = client.chat_postMessage(
      channel = "ideas",
      text = "This is a test :tada:"
    )
  except SlackApiError as e:
    print(e.response["error"])
