
from system.core.model import Model
import re

class WishlistModel(Model):
    def __init__(self):
        super(WishlistModel, self).__init__()


    def remove_wishlist_item(self,user_id,item_id):
        data = {
            'item_id' : item_id,
            'user_id' : user_id
        }
        query = 'DELETE FROM wishlist WHERE user_id = :user_id AND item_id = :item_id'
        self.db.query_db( query, data )
        return True

    def add_to_wishlist(self,user_id,item_id):
        data = {
            'item_id' : item_id,
            'user_id' : user_id
        }
        query = 'INSERT INTO wishlist (user_id, item_id)VALUE(:user_id, :item_id);'
        self.db.query_db( query, data )
        return True

    def get_user_wishlist_items(self, user_id):
        data = { 'id' : user_id }
        query =  'SELECT items.id, items.name, items.created_by, items.created_at FROM items '
        query += 'INNER JOIN wishlist ON items.id = wishlist.item_id '
        query += 'INNER JOIN users ON wishlist.user_id = :id '
        query += 'GROUP BY items.name'
        wishlist = self.db.query_db( query, data )
        return wishlist

    def get_other_wishlist_items(self, user_id):
        data = { 'id' : user_id }
        query =  'SELECT items.id, items.name, items.created_by, items.created_at FROM items '
        query += 'INNER JOIN wishlist ON items.id = wishlist.item_id '
        query += 'INNER JOIN users ON wishlist.user_id != :id '
        query += 'WHERE items.id NOT IN( SELECT items.id FROM items '
        query += 'INNER JOIN wishlist ON items.id = wishlist.item_id '
        query += 'INNER JOIN users ON wishlist.user_id = :id) '
        query += 'GROUP BY items.name'


        wishlist = self.db.query_db( query, data )
        return wishlist
