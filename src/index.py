from repositories.reference_repository import Reference_Repository
from services.reference_services import ReferenceService
from console_io import ConsoleIO
from app import App

def main():
    reference_repo = Reference_Repository()
    service_ref = ReferenceService(reference_repo)
    console_io = ConsoleIO()
    app = App(service_ref, console_io)

    app.run()

if __name__ == "__main__":
    main()
