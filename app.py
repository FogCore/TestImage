import os
import logging
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    if not os.path.exists('/tmp/meetings_number.txt'):
        with open('/tmp/meetings_number.txt', 'w') as file:
            file.write('1')
            return 'Hello World! I have been seen 1 time.\n'
    else:
        count = 1
        with open('/tmp/meetings_number.txt', 'r') as file:
            count += int(file.read())
        with open('/tmp/meetings_number.txt', 'w') as file:
            file.write(str(count))
            return 'Hello World! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
