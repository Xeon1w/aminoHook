import json
from flask import Flask, request
import rer

app = Flask(__name__)


def sus(f):
    code = rer.main(str(f))
    return code


@app.route('/', methods=['POST'])
def json_example():
    req_data = request.get_json()
    link = req_data['link']
    try:
        code = rer.main(str(link))
        return sus(link)
    except:
        return sus(link)


if __name__ == '__main__':
    app.run(port=5001)
