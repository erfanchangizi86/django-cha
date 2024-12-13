from channels.routing import ProtocolTypeRouterوURLRouter
from channels.auth import AuthMiddlewareStack
from panel_sms import routing
application = ProtocolTypeRouter({
    "websocket":AuthMiddlewareStack(
        URlRouter(
            routing.websocket_urlpatterns
        )
    )   
})
