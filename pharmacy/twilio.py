from twilio.rest import Client

account_sid = "AC652ed419cb9d686b719ff7a71084064d"
auth_token  = "8b5a0905d17263be38d6ef875527bde1"

client = Client(account_sid, auth_token)

def send_sms(phone_number, body):
    message = client.messages.create(
        to= str(phone_number),
        from_="+12407021252",
        body= body)
    return message


def send_fax(file):
    fax = client.fax.v1.faxes.create(
        to="+17034018245",
        from_="+12407021252",
        media_url= file
    )
    return fax
