HyperKitty - Archiver for for GNU Mailman v3
============================================

HyperKitty is an open source Django application under development. It aims to
provide web interface to access GNU Mailman archives.

This is the hyperkitty_standalone component, which provides the Django project
files and some examples to configure Apache and Mailman.


Installation using VirtualEnv
-----------------------------

Virtualenv creates an isolated python environment where you can add HyperKitty
and its dependencies without messing up your system Python install.

First, create the virtualenv and activate it::

    virtualenv venv_hk
    source venv_hk/bin/activate

Then download the components of HyperKitty::

    git clone git://github.com/pypingou/kittystore.git
    cd kittystore
    python setup.py develop
    cd ..
    bzr branch http://bzr.fedorahosted.org/bzr/hyperkitty/hyperkitty
    cd hyperkitty
    python setup.py develop
    cd ..


Setting up the databases
------------------------

Now you can create the KittyStore and HyperKitty databases, and set their
access URLs in ``settings.py`` (or ``settings_local.py``). HyperKitty's
database can be created using the following command::

    python manage.py syncdb

KittyStore's database will be created automatically on first access.

Then, you can run ``kittystore-import`` to import existing archives into the
mailman database. Thoses archives can be downloaded by a script similar to the
``get_mbox.py`` script provided in the ``kittystore`` module. If you're
installing hyperkitty on the machine which hosted the previous version of
mailman, the archived are already available locally and you can use them
directly.


Configuring Apache
------------------

Then, register HyperKitty into Apache's web server using the provided example
configuration file (``hyperkitty.apache.conf``) and reload Apache.

Now, create the static files directory to be served by Apache with the
command::

    python manage.py collectstatic

You should now be all set. Try accessing HyperKitty in your web browser.


Connecting to Mailman
---------------------

To receive incoming emails from Mailman, you must add the follwing lines to
``mailman.cfg``::

    [archiver.hyperkitty]
    class: hyperkitty.lib.archiver.Archiver
    enable: yes
    configuration: /path/to/here/hyperkitty.cfg

The ``hyperkitty.cfg`` file which path is specified by the ``configuration``
key is an additional HyperKitty-specific configuration file for which an
example is provided. See the included ``hyperkitty.cfg`` file.

After having made these changes, you must restart Mailman. Check its log files
to make sure the emails are correctly archived. You should not see "``Broken
archiver: hyperkitty``" messages.


License
-------

HyperKitty is licensed under the `GPL v3.0`_

.. _GPL v3.0: http://www.gnu.org/licenses/gpl-3.0.html
