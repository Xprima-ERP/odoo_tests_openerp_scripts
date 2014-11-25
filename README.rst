===============================
odoo_tests
===============================

.. image:: https://badge.fury.io/py/odoo_tests_openerp_scripts.png
    :target: http://badge.fury.io/py/odoo_tests_openerp_scripts


Test openerp_scripts to be used with Anybox Odoo recipe.

* Free software: GNU GPL v3.0 license

Features
--------

* Buildout.cfg example to use this package.
  ::
   [buildout]
   parts = odoo

   [odoo]
   eggs = odoo_tests_openerp_scripts
   recipe = anybox.recipe.openerp[bzr]:server
   version = git https://github.com/odoo/odoo.git odoo_server 7.0
   openerp_scripts = test_odoo=test_odoo arguments=session
                     create_db arguments=session
                     drop_db arguments=session

This buildout config will produce 3 scripts in the environment. test_odoo, create_db and drop_db.

test_odoo
^^^^^^^^^^^^^^^^^^^^^
Must be used with -d database_name -u module_name
 * -i might be used instead of -u.
 * all might be used instead of module_name

create_db
^^^^^^^^^^^^^^^^^^^^^
create_db -h for usage.

drop_db
^^^^^^^^^^^^^^^^^^^^^
drop_db -h for usage.
