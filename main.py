
import endpoints
from protorpc import message_types, messages, remote

class OutputMessage(messages.Message):
    message = messages.StringField(1)

@endpoints.api(name='hello', version='v1')
class HelloApi(remote.Service):
    @endpoints.method(message_types.VoidMessage,
        OutputMessage,
        path="helloworld",
        http_method='POST')
    def print_hello(self, request):
        return OutputMessage(message="Hello, World!")

api = endpoints.api_server([HelloApi])        
