from Observers.abs_observer import AbsObserver


class Manchester(AbsObserver):
    warning = ""
    airport_name = "Manchester Airport"

    flight_manifest = {"Luton": "BA005", "Paris": "PAR55"}

    def __init__(self, weather_warning):
        self._weather_warning = weather_warning
        weather_warning.attach(self)

    def update(self):
        self.warning = self._weather_warning.warning
        self.display()


    def __exit__(self, exc_type, exc_val, exc_tb):
        self._weather_warning.detach(self)