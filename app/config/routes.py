
from system.core.router import routes

routes['default_controller'] = 'Users'
routes['/users/logoff'] = 'Users#logout'
routes['POST']['/users/register'] = 'Users#register'
routes['POST']['/users/login'] = 'Users#login'

routes['/items/show/<id>'] = 'Items#show'
routes['/items/add'] = 'Items#add'
routes['POST']['/items/create'] = 'Items#create'
routes['POST']['/items/<id>/delete'] = 'Items#delete'

routes['POST']['/wishlist/<id>/remove'] = 'Wishlists#remove_wishlist_item'
routes['POST']['/wishlists/create/<id>'] = 'Wishlists#add_to_wishlist'
