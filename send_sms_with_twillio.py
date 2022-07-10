from twilio.rest import Client 
 
account_sid = '**********************************' # Twillio account SID
auth_token = '***********************************' # Twillio auth token
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='***********************************', #Messaging service SID
                              body='Twilio Test Successful',      
                              to='**********' # Recipient's phone number
                          ) 
 
print(message.sid)