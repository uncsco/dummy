# // Vars with *default* values: https://stackoverflow.com/a/2013589
HOST=${HOST:-127.0.0.1}
PORT=${PORT:-7000}
SRC=${SRC:-src}
MAIN=${MAIN:-main}
APP=${APP:-app}
WORKERS=${WORKERS:-4}
TIMEOUT=${TIMEOUT:-30}

# `--timeout`: https://docs.gunicorn.org/en/stable/settings.html#timeout


# // gunicorn -b 127.0.0.1:7000 --chdir src main:app -w 4 -t 30 --reload
gunicorn -b $HOST:$PORT --chdir $SRC $MAIN:$APP -w $WORKERS -t $TIMEOUT --reload
