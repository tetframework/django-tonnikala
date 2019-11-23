Tonnikala templates - powered by ponies!
========================================

Django integration for [the one-ton templating language](https://github.com/tetframework/tonnikala).

To use, install (with `pip install django-tonnikala` or `python setup.py install`) and configure your settings:

```python
TEMPLATES = [
    {
        'BACKEND': 'django_tonnikala.backends.Tonnikala',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            # TODO
        },
    },
]
```

And add your templates to `your_app/tonnikala/`!

Running the example project
---------------------------

The git repository includes an example project

```bash
python3 -m venv venv
venv/bin/pip install -r example_project/requirements.txt
venv/bin/python example_project/manage.py migrate
venv/bin/python example_project/manage.py runserver
```

And then visit http://localhost:8000
