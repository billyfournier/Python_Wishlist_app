"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Items(Controller):
    def __init__(self, action):
        super(Items, self).__init__(action)

        self.load_model('ItemModel')
        self.db = self._app.db

    def show(self,id):
        item = self.models['ItemModel'].get_item(id)
        wishlist_users = self.models['ItemModel'].get_users_who_wishlisted_item(id)
        print wishlist_users, '8' * 40
        ## didn't have time to get the last part of this one finished
        return self.load_view('showitem.html', item=item, users=wishlist_users)


    def add(self):
        if 'user' not in session:
            return self.load_view('index.html')
        else:
            return self.load_view('additem.html')

    def delete(self,id):
        self.models['ItemModel'].delete_item(id)
        return redirect('/')



    def create(self):
        for item in ['name']:
            if item not in request.form:
                print '------- error with form -----------'
                return redirect('/')
        item_info =  {
            'name' : request.form['name'],
            'created_by' : session['user']['username'],
            'user_id' : session['user']['id']
        }
        item_check = self.models['ItemModel'].create_item(item_info)
        if item_check != True:
            for error in item_check:
                flash(error)
                return redirect('/items/add')

        return redirect('/')
