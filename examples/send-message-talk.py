import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import zulip

client = zulip.Client(email="weather-bot@mrtalk.co.kr", client="ConsoleClient/0.1")
firstmsg = "안녕하세요"
messagefirst = {
    "type": "private",
    "to": "mr.neo@mrtalk.co.kr",
    "content": firstmsg,
}

client.send_message(messagefirst)

def send_message(Client, orginmsg, senderid, receiverid, client):

    botmsg = orginmsg + "에 대한 봇톡"
    message = {
        "type": "private",
        "to": "mr.neo@mrtalk.co.kr",
        "content": botmsg ,
    }

    if client == "website":
        Client.send_message(message)

# Print each message the user receives
# This is a blocking call that will run forever
# client.call_on_each_message(lambda msg: sys.stdout.write("message:" + str(send_message(client,msg['content'],msg['sender_id'],msg['recipient_id'],msg['client'])) + "\n"))
client.call_on_each_message(lambda msg: send_message(client,msg['content'],msg['sender_id'],msg['recipient_id'],msg['client']))

