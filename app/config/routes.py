
from system.core.router import routes

routes['default_controller'] = 'Users'
routes['/users/logoff'] = 'Users#logout'
routes['/items/show/<id>'] = 'Items#show'
# routes['/'] = 'Users'
routes['POST']['/users/register'] = 'Users#register'
routes['POST']['/users/login'] = 'Users#login'
routes['/items/add'] = 'Items#add'
routes['POST']['/items/create'] = 'Items#create'
routes['POST']['/wishlist/<id>/remove'] = 'Wishlists#remove_wishlist_item'
routes['POST']['/wishlists/create/<id>'] = 'Wishlists#add_to_wishlist'
routes['POST']['/items/<id>/delete'] = 'Items#delete'



"""
    Here is an example of the restful routes for users:

    routes['GET']['/users'] = 'users#index'
    routes['GET']['/users/new'] = 'users#new'
    routes['POST']['/users'] = 'users#create'
    routes['GET']['/users/<int:id>'] = 'users#show'
    routes['GET']['/users/<int:id>/edit' = 'users#edit'
    routes['PATCH']['/users/<int:id>'] = 'users#update'
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'
"""
