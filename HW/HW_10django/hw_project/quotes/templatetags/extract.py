from bson.objectid import ObjectId
from django import template
from ..utils import get_mongodb

register = template.Library()


def get_author_info(id_):
    db = get_mongodb()
    author_data = db.authors.find_one({'_id': ObjectId(id_)})
    return {
        'fullname': author_data['fullname'],
        'birth_date': author_data.get('birth_date', None),
        'birth_location': author_data.get('birth_location', None),
        'description': author_data.get('description', None),
    }


register.filter('authors', get_author_info)
