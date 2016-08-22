"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Wishlists(Controller):
    def __init__(self, action):
        super(Wishlists, self).__init__(action)

        self.load_model('WishlistModel')
        self.db = self._app.db

    def remove_wishlist_item(self, id):
        self.models['WishlistModel'].remove_wishlist_item(session['user']['id'],id)
        return redirect('/')

    def add_to_wishlist(self, id):
        self.models['WishlistModel'].add_to_wishlist(session['user']['id'],id)
        return redirect('/')
