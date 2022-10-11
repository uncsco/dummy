from flask import Flask, send_from_directory
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# // https://flask.palletsprojects.com/en/2.1.x/quickstart/#variable-rules

@app.route('/idem/<val>')
def idem(val):
    return f"val: {escape(val)}"

@app.route('/idem-int/<int:n>')
def idem_int(n: int):
    return f"n={n}"




'''
@app.route('/front-end/')
def front_end_home():
    return send_from_directory('front_end', 'index.html')
'''

'''
@app.route("/front-end/js/<path:f_path>")
def front_end_js(f_path):
    return send_from_directory('front_end', f"js/{f_path}", mimetype="text/javascript")
'''


@app.route('/front-end/', defaults={'f_path': ''})  # WIP ======================

# ?? `defaults`: https://stackoverflow.com/a/39545134
@app.route(
    "/front-end/<path:f_path>",
    #defaults={'f_path': 'index.html'}
)
def front_end(f_path):
    ##return send_from_directory('front_end', "index.html", mimetype="text/html")

    mimetype = "text/html"
    #if f_path is None : f_path = "index.html"  # NOPE

    # // https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
    if f_path.endswith(".css"):
        mimetype = "text/css"
    elif f_path.endswith(".js"):
        mimetype = "text/javascript"
    else:
        f_path = "index.html"  # WIP =====================================


    # // `send_from_directory`: https://stackoverflow.com/a/20648053
    # // `mimetype`: https://stackoverflow.com/a/66512695
    return send_from_directory('front_end', f_path, mimetype=mimetype)


'''
TODO: To TRY...

@app.route('/FRONT/<path:f_path>')      # ...
@app.route('/FRONT/css/<path:f_path>')  # ...
@app.route('/FRONT/js/<path:f_path>')   # ...
'''


'''
TODO:

https://codeburst.io/full-stack-single-page-application-with-vue-js-and-flask-b1e036315532
https://github.com/oleg-agapov/flask-vue-spa
'''
