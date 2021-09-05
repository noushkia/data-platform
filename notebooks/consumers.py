import json
from channels.generic.websocket import WebsocketConsumer

from notebooks.models import Notebook, Cell
from notebooks.services.notebook import get_notebook_session_service
from notebooks.services.session import SessionService, make_new_session, SessionIsDown


class NotebookConsumer(WebsocketConsumer):

    def connect(self):
        # pylint: disable=attribute-defined-outside-init
        self.notebook_id = self.scope['url_route']['kwargs']['notebook_id']

        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        cell_id = text_data_json['cell_id']
        code = text_data_json['code']
        cell = Cell.objects.get(pk=cell_id)
        cell.code = code
        cell.cell_status = Cell.CellStatus.RUNNING
        cell.save()

        try:
            session_service = get_notebook_session_service(self.notebook_id)
            result = session_service.run_script(code)
            message_type = "run_cell"
        except SessionIsDown:
            result = "Session is down. Please restart session"
            message_type = "notification"

        self.send(text_data=json.dumps({
            'cell_id': cell_id,
            'result': result,
            'message_type': message_type,
        }))

        cell.cell_status = Cell.CellStatus.DONE
        cell.save()
