# pylint-server
free static code analysis server for Python, via pylint

## usage

```python

import requests

with open('test.py') as f:
    code = f.read()

    data = {
        "filename": "test.py", # this specifies the name for the file used in the output
        "code": code,          # the code to check
    }


    headers = {
        "Content-Type": "application/json"
    }


    response = requests.post("https://unindex.pythonanywhere.com:443/analyze", json=data)
    json = response.json()
    print(json['output'])

```
response:

<img src="https://github.com/Un-index/pylint-server/blob/main/docs/img.png" width=320 alt="a screenshot showing the response"></img>

you can add arguments to pylint by changing `data` in the code above to:
```python
data = {
    "filename": "test.py", # this specifies the name for the file used in the output
    "code": code,          # the code to check
    # if you want(optional), you can specify arguments to pylint, there should be no spaces b/w args 
    "pylint_opts": ["--disable=invalid-name,missing-function-docstring"] 
}

```
