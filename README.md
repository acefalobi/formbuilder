=====
FormBuilder
=====

FormBuilder is an online interface that allows users to create forms and publish for interaction by others

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "formbuilder_app" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'formbuilder_app',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^', include('formbuilder_app.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000 to get started
