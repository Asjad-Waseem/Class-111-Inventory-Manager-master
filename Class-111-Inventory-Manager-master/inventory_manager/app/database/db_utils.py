"""
    This module contains all database utilities
"""

from inventory_manager.app.database.db_connection import get_db


# ---- C R E A T E   P R O D U C T
def create(name, price, quantity, description, category):
    values = (name, price, quantity, description, category, True)
    query = """INSERT INTO product(name, price, quantity, description, category, is_active) VALUES(?, ?, ?, ?, ?, ?)"""
    cursor = get_db()
    last_row_id = cursor.execute(query, values).lastrowid
    cursor.commit()
    return last_row_id


# ---- C R E A T E   R E V I E W
def create_review(name, review, product_id):
    values = (name, review, product_id)
    query = """INSERT INTO review(name, review, product_id) VALUES(?, ?, ?)"""
    cursor = get_db()
    last_row_id = cursor.execute(query, values).lastrowid
    cursor.commit()
    return last_row_id


# ---- G E T   A L L   P R O D U C T S
def get_all_products():
    cursor = get_db().execute("SELECT * FROM product WHERE is_active = True ORDER BY id DESC", ())
    results = cursor.fetchall()
    cursor.close()
    return results


def get_filter_products(search):
    query = "SELECT * FROM product WHERE is_active = True AND name LIKE '%{}%'".format(search)
    cursor = get_db().execute(query,
                              ())
    results = cursor.fetchall()
    cursor.close()
    return results


def get_in_filter_products(search):
    query = "SELECT * FROM product WHERE is_active = 0 AND name LIKE '%{}%'".format(search)
    cursor = get_db().execute(query,
                              ())
    results = cursor.fetchall()
    cursor.close()
    return results


# ---- G E T   O N E   P R O D U C T
def get_one_product(product_id):
    cursor = get_db().execute("SELECT * FROM product WHERE id = %s" % product_id, ())
    results = cursor.fetchall()
    cursor.close()
    return results


# ---- G E T   R E V I E W S
def get_reviews(product_id):
    cursor = get_db().execute("SELECT * FROM review WHERE product_id = %s" % product_id, ())
    results = cursor.fetchall()
    cursor.close()
    return results


# ---- U P D A T E   P R O D U C T
def update_one_product(product_id, values: dict):
    value_string = ",".join("%s=\"%s\"" % (key, val) for key, val in values.items())
    query = """UPDATE product SET %s WHERE id={}""".format(product_id) % value_string
    cursor = get_db()
    cursor.execute(query)
    cursor.commit()
    return True


# ---- D E L E T E   P R O D U C T
def delete(product_id):
    query = "Delete from product WHERE id=%s" % product_id
    cursor = get_db()
    cursor.execute(query, ())
    cursor.commit()
    return True


def delete_product(product_id):
    query = "UPDATE product SET is_active=False WHERE id=%s" % product_id
    cursor = get_db()
    cursor.execute(query, ())
    cursor.commit()
    return True


# ---- G E T   I N A C T I V E  P R O D U C T S
def get_inactive_products():
    cursor = get_db().execute("SELECT * FROM product WHERE is_active = 0")
    results = cursor.fetchall()
    cursor.close()
    return results


# ---- A C T I V A T E   P R O D U C T
def set_is_active(product_id):
    query = "UPDATE product SET is_active = True WHERE id = %s" % product_id
    cursor = get_db()
    cursor.execute(query, ())
    cursor.commit()
    return True
