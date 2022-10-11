import CONF


"""
"Config File": https://docs.gunicorn.org/en/stable/settings.html#config-file

> By default, a file named `gunicorn.conf.py` will be read
> from the *same* directory where `gunicorn` is being run.
"""


#// EXAMPLE: `gunicorn -b 127.0.0.1:7000 --chdir src main:app -w 4 -t 30 --reload`


bind = '127.0.0.1:7000'

#// 'Worker Processes': https://docs.gunicorn.org/en/stable/settings.html#worker-processes
workers = 4   # DEFAULT: 1

timeout = 30  # DEFAULT: 30


chdir = CONF.SRC

#// https://docs.gunicorn.org/en/stable/settings.html#wsgi-app
wsgi_app = "main:app"


#// 'Debugging': https://docs.gunicorn.org/en/stable/settings.html#debugging
reload = True

