"""Send a request to the localhost server."""
import requests
#
# The port number is the ':8000' after localhost, in the url below.
# Make sure it matches the port you set up in the server file!
#
R = requests.get("http://localhost:8000/hi_temp_message")
#
# Print the status code of the request.  200 == Success!
#
print(R.status_code)
#
# Just for kicks, check out all the stuff that the R object has in it.
# HTTP can be overwhelming, but it's not going anywhere, so learn it!
#
# print(dir(R))
