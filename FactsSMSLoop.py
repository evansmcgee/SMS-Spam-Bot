import requests
from twilio.rest import TwilioRestClient
import time
import random

account_sid = 'Your Twilio Account SID'
auth_token = 'Your Twilio Auth Token'
animal_int = raw_input('1) Cat Facts 2) Dog Facts ... anything else will exit : ')
while True:
    try:
        receiver = raw_input('Target Phone # ? : ')
        sender = "+15873166702"
        client = TwilioRestClient(account_sid, auth_token)
        if animal_int=='1':
            r_in = requests.get('http://catfacts-api.appspot.com/api/facts?number=1')
        elif animal_int=='2':
            r_in = requests.get('http://dog-api.kinduff.com/api/facts?number=1')
        else:
            break
        s = r_in.text
        start = '["'
        end = '"]'
        sms = s[s.find(start)+len(start):s.rfind(end)]
        print sms
        message = client.messages.create(to=receiver, from_=sender,body=sms)
        time.sleep(random.randrange(10,900))
    except KeyboardInterrupt:
        print '\n Goodbye'
        break
