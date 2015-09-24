Tonnikala templates - powered by ponies!
========================================

Django integration for [the one-ton templating language](https://github.com/tetframework/tonnikala).

To use, install (with `python setup.py install`) and configure your settings:

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
