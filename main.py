from Observers.london import London
from Observers.manchester import Manchester
from Subject.weather_warning import WeatherWarning

# set a flood warning for Heathrow, Luton or Paris

with WeatherWarning() as weather_warning:
    with London(weather_warning), Manchester(weather_warning):
        weather_warning.set_warning("Luton")