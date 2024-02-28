from Subject.abs_subject import AbsSubject


class WeatherWarning(AbsSubject):
    _warning = ""

    @property
    def warning(self):
        return self._warning

    def set_warning(self, warning):
        self._warning = warning
        self.notify()