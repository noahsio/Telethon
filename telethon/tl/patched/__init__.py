from .. import types, alltlobjects
from ..custom.message import Message as _Message

class MessageEmpty(_Message, types.MessageEmpty):
    pass

types.MessageEmpty = MessageEmpty
alltlobjects.tlobjects[MessageEmpty.CONSTRUCTOR_ID] = MessageEmpty

class MessageService(_Message, types.MessageService):
    pass

types.MessageService = MessageService
alltlobjects.tlobjects[MessageService.CONSTRUCTOR_ID] = MessageService

class Message(_Message, types.Message):
    pass

types.Message = Message
alltlobjects.tlobjects[Message.CONSTRUCTOR_ID] = Message

# Register old constructor IDs so sessions that haven't re-negotiated the
# layer yet (Telegram still sends the previous schema) keep working.
alltlobjects.tlobjects[0x9cb490e9] = Message  # message pre-layer 223 (without from_rank)
