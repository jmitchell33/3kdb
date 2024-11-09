import copy, sys, requests, time

url = str(sys.argv[1])
data = ""
for i in range(len(sys.argv)):
    if i >= 2:
        data = " ".join([data, sys.argv[i]])

headers = {'Content-Type': "application/json", 'Accept': "application/json"}

data = data.replace("x7B", "{")
data = data.replace("x7D", "}")

try:
    res = requests.post(url, json=data, headers=headers)
except (requests.exceptions.SSLError):
    time.sleep(3)
    try:
        res = requests.post(url, json=data, headers=headers)
    except:
        pass
except:
    pass