import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import zulip

client = zulip.Client(email="weather-bot@mrtalk.co.kr", client="MyTestClient/0.1")
message = {
    "type": "private",
    "to": "mr.neo@mrtalk.co.kr",
    "content": "your content",
}
print(client.send_message(message))

# Print each message the user receives
# This is a blocking call that will run forever
client.call_on_each_message(lambda msg: sys.stdout.write(str(msg) + "\n"))

# Print every event relevant to the user
# This is a blocking call that will run forever
# This will never be reached unless you comment out the previous line
client.call_on_each_event(lambda msg: sys.stdout.write(str(msg) + "\n"))
