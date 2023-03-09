import plivo
import csv

# Set up Plivo client with your API credentials
client = plivo.RestClient(auth_id='your_auth_id', auth_token='your_auth_token')

# Make a call using Plivo's API
response = client.calls.create(
    from_='your_plivo_number',
    to_='destination_phone_number',
    answer_url='http://example.com/answer_url/',
    answer_method='GET'
)

# Extract features returned from Plivo's response
call_uuid = response.uuid
call_status = response.status
call_direction = response.direction
call_rate = response.rate
call_duration = response.duration

# Write features to a CSV file
with open('call_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Call UUID', 'Status', 'Direction', 'Rate', 'Duration'])
    writer.writerow([call_uuid, call_status, call_direction, call_rate, call_duration])
