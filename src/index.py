from services.reference_services import ReferenceService
from console_io import ConsoleIO
from app import App

def main():
    service_ref = ReferenceService()
    console_io = ConsoleIO()
    app = App(service_ref, console_io)
    app.run()

if __name__ == "__main__":
    main()
