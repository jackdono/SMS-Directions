# SMS-Directions
A simple Flask app to send driving directions via SMS, using openrouteservice and a Twilio phone number.
##### Usage
To get the SMS working, you need a Twilio account and phone number. I haven't tested this yet because I need to submit some things to get one.
The message format it expects is `*start address* to *end address*`.

You can use the directions code independently with `from directions import getroute` and `getroute(start_addr, end_addr)`.
You'll also need to get an API key from [openrouteservice](https://openrouteservice.org/).