import abc


class AbsObserver(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, value):
        pass

    def __enter__(self):
        return self

    def display(self):
        if self.warning in self.flight_manifest.keys():
            print("WARNING: Divert flights for {}".format(self.warning))
        else:
            print("Flights to {} arriving on time".format(self.airport_name))

    @abc.abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass