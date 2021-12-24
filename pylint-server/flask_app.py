# server to send back feedback after analyzing python code
# pip install pylint via console

from flask import Flask
from flask import request
from flask import Response

# import pylint.lint
# import threading
import uuid
import json
import os


# def deleteAsync(filename):
#     threading.Thread(target=lambda: os.remove(filename)).start()


app = Flask(__name__)

# see logs at
# logs: https://www.pythonanywhere.com/user/unindex/files/var/log/
# error logs: https://www.pythonanywhere.com/user/unindex/files/var/log/unindex.pythonanywhere.com.error.log


@app.route('/')
def info():
    return """
    <html>
    <head>
    <title>pylint-server</title>
    <style>body{font-family: Sans-Serif;}</style>
    </head>
    <body>
    <h1>pylint-server</h1>
    Allows you to run Python code through <a href="https://pypi.org/project/pylint/">Pylint</a>, which is a 'Python static code analysis tool which looks for programming errors, helps enforcing a coding standard, sniffs for code smells and offers simple refactoring suggestions.'
    <br><br>
    Endpoints:
    <ul><li>/analyze {filename:string, code:string} -> output:string</li></ul>
    </body>
    </html>

    """
# available at https://unindex.pythonanywhere.com:443/analyze


@app.route('/analyze', methods=['POST'])
def analyze():
    req = request.get_json()
    print(req)
    name = req.get('filename')
    src = req.get('code')
    if not (name and src):
        return Response(json.dumps({'error': f"{not name and 'name was not was specified as a parameter' or ''} {not src and 'src was not was specified as a parameter' or ''}"}), status=400, mimetype='application/json')
    pylint_opts = ', '.join(req.get('pylint_opts') or [])
    print("using"+str(pylint_opts))
    uuid4 = str(uuid.uuid4())

    filename = uuid4+".py"
    with open(f'./{filename}', 'w') as f:
        f.write(src)

    # # can't get output running from subprocess, so doing this instead
    output = os.popen(f'pylint {filename} {pylint_opts or ""}').read()
    output = output.rstrip().replace(uuid4, name)
    # deleteAsync(filename)
    os.remove(filename)
    # returns {"output": "[OUTPUT HERE]"}
    return Response(json.dumps({'output': output}), status=200, mimetype='application/json')
