import subprocess


class Addon():
    name = 'Screen Brightness'
    icon = 'mdi:monitor'
    unit = '%'
    sensor_type = 'number'
    type = 'number'

    def exposedControls(self):
        return {
            "Screen_Brightness": {
                "type": "number",
                "icon": "mdi:monitor",
                "min": 0,
                "max": 100,
            }
        }

    def getInfo(self):
        stdout = subprocess.run(
            "ddcutil getvcp 10 --bus 21",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE).stdout.decode("UTF-8")
        results = stdout.lower()
        results = results.strip().split(':')[1].strip()
        print(results)
        results = results.strip().split(',')[0].strip()
        print(results)
        status = results.strip().replace('current value =','').strip()
        print(status)
        
        

        return status

    def startControl(self, topic, data):
        subprocess.call('ddcutil setvcp 10 ' + data + ' --bus 21', shell=True)
