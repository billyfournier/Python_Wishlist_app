
from system.core.model import Model
import re

class ItemModel(Model):
    def __init__(self):
        super(ItemModel, self).__init__()


    def get_item(self,id):
        data = { 'id' : id }
        query = 'SELECT * FROM items WHERE id = :id'
        item = self.db.query_db( query, data )
        return item[0]

    def get_users_who_wishlisted_item(self,id):
        data = { 'id' : id }
        query =  'SELECT users.username FROM users '
        query += 'INNER JOIN wishlist ON users.id = wishlist.user_id '
        query += 'INNER JOIN items ON wishlist.item_id = :id '
        query += 'GROUP BY users.username'
        users = self.db.query_db( query, data )
        return users

    ## Not working due to:
    ##   Cannot delete or update a parent row: a foreign key constraint fails
    def delete_item(self,id):
        data = { 'id' : id }
        query = 'DELETE FROM items WHERE id = :id'
        self.db.query_db( query, data )
        return True


    def create_item(self, item_info):
        errors = []
        if len(item_info['name']) < 3:
            errors.append('name least 3 characters')
        if len(errors) > 0:
            return errors

        data = {
            'name' : item_info['name'],
            'created_by' : item_info['created_by']
        }
        query_check_item = 'SELECT * FROM items WHERE items.name = :name LIMIT 1'
        query_add_item = 'INSERT INTO items (name, created_by)VALUE(:name, :created_by)'

        check = self.db.query_db( query_check_item, data ) # Because item names are unique
        if len(check) != 0:
            errors.append('item already exists')
            return errors
        print 'test'
        query_add_item = 'INSERT INTO items (name, created_by)VALUE(:name, :created_by)'
        item_id = self.db.query_db( query_add_item, data )
        print item_info, '8' * 40
        wishlist_data = {
            'user_id' :  item_info['user_id'],
            'item_id' : item_id
        }
        query = 'INSERT INTO wishlist (user_id, item_id)VALUE(:user_id, :item_id)'
        self.db.query_db( query, wishlist_data )
        return True
