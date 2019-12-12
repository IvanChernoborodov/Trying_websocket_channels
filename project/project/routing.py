# mysite/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing
from channels.security.websocket import OriginValidator


# application = ProtocolTypeRouter({
#     # (http->django views is added by default)
#     'websocket': AuthMiddlewareStack(
#         URLRouter(
#             chat.routing.websocket_urlpatterns
#         ),
#     ),
#
# })

application = ProtocolTypeRouter({
    "websocket": OriginValidator(
        AuthMiddlewareStack(
            URLRouter(chat.routing.websocket_urlpatterns),
        ),
        ["http://127.0.0.1:8000"],
    ),
})