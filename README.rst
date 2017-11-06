Fast Queue
==========

Simple Task Producer


Getting Started
---------------

When you import fast_queue, it does some Module Wrapper and Import Hook magic to create a mock that will schedule the task on your broker of choice in a way that celery can consume.

.. code:: python

    from fast_queue.myapp.mail import send_mail
    send_mail('fast@queue.rocks')


Goal
----

Decouple all your celery dependencies from your web project. With fast-queue You can separate your async task impl from your web project. Nowadays, most projects that relies on Celery is great monolithic with both web code and the async task code. With Fast-Queue, you can break them apart in two packages without any cross dependency.

You can benefit

Development benefits:
- Web project does not have dependency of the your async tasks.
- Async tasks, can evolve apart from the web project, as long as the signature does not change.


Deployment benefits:
- Separated and independent deploys for both web and async task project
- Smaller web project size, and for the ones that use serveless, project size should be always a concern.


Installing
----------

Just pip install it!

    pip install fast-queue


License
-------

This project is licensed under MIT license


For Early Adopters
------------------

Although I'm already using it on production environment, there are some improvements and bugs ahead that must be fixed.

- Easier to configure without monkey patching stuff
- Support for Python 3
