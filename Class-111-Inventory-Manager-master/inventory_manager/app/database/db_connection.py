"""
    This module is a connection instance
    You need to create a .db file using sqlite3 in order to use DATABASE, script for db is in dev.txt
"""

from flask import g
import sqlite3

DATABASE = "dev_inventory_manager.db"


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db
