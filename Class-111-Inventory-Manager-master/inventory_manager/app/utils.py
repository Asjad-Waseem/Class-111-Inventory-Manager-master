"""
all utilities are here
"""

products = list(range(100))  # setting range for total products, can be increased
reviews = list(range(100))


def get_products(offset=0, per_page=10):
    return products[offset: offset + per_page]


def get_page_reviews(offset=0, per_page=3):
    return reviews[offset: offset + per_page]