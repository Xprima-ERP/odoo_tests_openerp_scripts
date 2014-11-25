# -*- coding: utf-8 -*-

import argparse
import psycopg2
import ConfigParser
from anybox.recipe.openerp.runtime import start_openerp


DBNAME_PARAM = "database_name"


def _get_openerp_config(session, config_name):
    """Returns the value of the specified configl."""
    config = ConfigParser.SafeConfigParser()
    config.read(session.openerp_config_file)
    host = config.get("options", config_name)
    return host


def _get_connection(session):
    db_options = {
        "database": "template1",
        "user": _get_openerp_config(session, "db_user"),
        "password": _get_openerp_config(session, "db_password"),
        "host": _get_openerp_config(session, "db_host"),
        "port": _get_openerp_config(session, "db_port")
    }
    for key, value in db_options.items():
        if value == "False" or not value:
            del db_options[key]

    conn = psycopg2.connect(**db_options)
    conn.autocommit = True
    return conn


def create_db(session):
    parser = argparse.ArgumentParser()
    parser.add_argument(DBNAME_PARAM, help="Database name to create")
    args = parser.parse_args()

    conn = _get_connection(session)
    cur = conn.cursor()
    cur.execute("CREATE DATABASE %s;" % getattr(args, DBNAME_PARAM))
    cur.close()
    conn.close()
    session.open(db=getattr(args, DBNAME_PARAM), with_demo=True)
    session.close()


def drop_db(session):
    parser = argparse.ArgumentParser()
    parser.add_argument(DBNAME_PARAM, help="Database name to drop")
    args = parser.parse_args()

    conn = _get_connection(session)
    cur = conn.cursor()
    cur.execute("DROP DATABASE %s;" % getattr(args, DBNAME_PARAM))
    cur.close()
    conn.close()


def main(session):
    start_openerp.main(
        '/odoo_server/parts/odoo_server/openerp-server',
        '/odoo_server/etc/odoo.cfg',
        version=(7, 0),
        just_test=True
    )
