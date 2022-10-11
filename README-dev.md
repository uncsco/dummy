## Flask - *deploying* with Gunicorn

https://flask.palletsprojects.com/en/2.2.x/deploying/gunicorn/?highlight=gunicorn#running

- `--chdir`: https://stackoverflow.com/a/42966708

- `-b 127.0.0.1:8000` // ALT: `0.0.0.0:8888`

- `--reload`

```sh
gunicorn -b 127.0.0.1:7000 --chdir src main:app -w 4 --reload
```

## Gunicorn - and CONFIG file

- Config file is `gunicorn.conf.py`

- Run with simply:

```sh
gunicorn
```

