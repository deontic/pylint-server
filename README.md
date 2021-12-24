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
        # optional pylint_opts, you could leave out this one
        "pylint_opts": ["--disable=invalid-name,missing-function-docstring"] # if you want, you can specify arguments to pylint, there should be no spaces b/w args 
    }


    headers = {
        "Content-Type": "application/json"
    }


    response = requests.post("https://unindex.pythonanywhere.com:443/analyze", json=data)
    json = response.json()
    print(json['output'])

```
response:

<img src="https://github.com/Un-index/pylint-server/blob/main/docs/img.png" alt="a screenshot showing the response"></img>
