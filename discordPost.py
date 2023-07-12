import sys, requests, time

url = str(sys.argv[1])
data = ""
for i in range(len(sys.argv)):
    if i >= 2:
        data = " ".join([data, sys.argv[i]])

payload = {"content" : data}
headers = {'Content-Type': "application/json", 'Accept': "application/json"}

try:
    res = requests.post(url, json=payload, headers=headers)
except (requests.exceptions.SSLError):
    time.sleep(3)
    try:
        res = requests.post(url, json=payload, headers=headers)
    except:
        pass
except:
    pass