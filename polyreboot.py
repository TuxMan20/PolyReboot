#!/usr/bin/env python3

import requests
import json
'''
    Poly Studio X50 Reboot Script

    Using the Requests module, uses the session API to get login
    informations. "login" will hold a sessionId token.

    Then, using the system/reboot API, uses the sessionId as a Cookie in
    the header to authenticate, and sends the reboot command.
'''

ip = "YOUR_DEVICE_ADDR"
url = "https://" + ip + "/rest/session"

credentials = json.dumps({
  "user": "DEVICE_USER",
  "password": "DEVICE_PASSWORD"
})

login = requests.post(url, data=credentials, verify=False)
if (login.status_code == 200):
    urlReboot = "https://" + ip + "/rest/system/reboot"

    payload = json.dumps({
      "action": "reboot"
    })
    headers = {
      'Cookie': 'session_id=' + login.json().get('session').get('sessionId')
    }

    action = requests.post(urlReboot, headers=headers, data=payload, verify=False)

    if (action.status_code == 200):
        print("\nRequest Successful. Device is rebooting")
    else:
        print("\nRequest Failed. HTTP Error code: " + str(action.status_code))
else:
    print("\nAuthentication Failed. HTTP Error code: " + str(login.status_code))
