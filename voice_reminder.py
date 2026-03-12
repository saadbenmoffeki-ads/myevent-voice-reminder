from twilio.rest import Client

# Twilio credentials (replace with your own)
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# Example: initiate a reminder call
call = client.calls.create(
    twiml='<Response><Say voice="alice">Reminder: Your meeting is in 1 hour!</Say></Response>',
    from_='+1XXXXXXXXXX',  # Twilio number
    to='+213XXXXXXXXX'     # User phone number
)

print(f"Call initiated! SID: {call.sid}")
