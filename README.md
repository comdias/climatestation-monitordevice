# Climate Station Monitor Device
Monitor device Software for Climate Station

This is a Raspberry Pi Python software to send data to [MDiasTech Climate Station](http://climatestation-mdiastech.rhcloud.com/).

## Getting Started
All you need is a Raspberry Pi, a temperature sensor and internet connectivity.

### Temperature sensor
For my personal station, I used a waterproof DS18B20 to stick it our of my bedroom window.
Adafruit have a [tutorial](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/hardware) on how to use the sensor.
They explain all the wiring and the software to read the sensor (pretty much the same I used).

### Deployment
Create a folder at /home/pi/thermometer and copy all project files there.
Edit thermometer.py to add your device key. Please request your device key throught the [Climate Station contact page](http://climatestation-mdiastech.rhcloud.com/monitor/contact/).
Configure thermometer to run during startup.

#### Add device key
Edit [thermometer.py](thermometer.py) as bellow with the provided device key.
```
device_key='YOUR-KEY'
```

#### Starting the thermometer
Configure [thermometer_start](thermometer_start) to start after reboot.

An option is to use crontab:
```
@reboot     /home/pi/thermometer/thermometer_start
```
