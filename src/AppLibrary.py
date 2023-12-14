import os
from stub_io import StubIO
from repositories.reference_repository import ReferenceRepository
from services.reference_services import ReferenceService
from app import App


class AppLibrary:
    def __init__(self):
        self._io = StubIO()
        self.dirname = os.path.dirname(__file__)
        self.robot_file_name = 'robot_references.csv'
        self.robot_bib_file_path = os.path.join(self.dirname, '..', 'data')
        self.robot_file_path = os.path.join(self.dirname, '..', 'data', self.robot_file_name)
        self._reference_repository = ReferenceRepository(self.robot_file_path, self.robot_bib_file_path)
        self._reference_service = ReferenceService(self._reference_repository)
        self._app = App(
            self._reference_service,
            self._io
        )

    def input(self, value):
        self._io.add_input(value)

    def output_should_contain(self, value):
        outputs = self._io.outputs
        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def run_application(self):
        self._app.run()

    def create_reference(self, type, fields):
        self._reference_service.create_reference(type, *fields)

    def create_bib_format_file(self, filename):
        self._reference_service.create_bib_format_file(filename)  

    def print_refs(self):
        self._reference_service.print_refs()

    def delete_reference(self, delete_bib_ref):
        self._reference_service.delete_reference(delete_bib_ref)    
