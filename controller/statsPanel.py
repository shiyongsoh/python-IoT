import psutil

class statsPanel:
    def Computer():
        #cpu
        cpuUsage = psutil.cpu_percent() #cpu usage
        cpuCoreCount = psutil.cpu_count() #cpu core count
        cpuStats = psutil.cpu_stats() #cpu stats

        #memory usage
        RAM = psutil.virtual_memory().percent

        #computer inbuilt sensors
        cpuTemps = psutil.sensors_temperatures() #cpu temps
        cpuFans = psutil.sensors_fans() #fans
        battery = psutil.sensors_battery() #battery

        return cpuUsage,cpuCoreCount,cpuStats,RAM,cpuTemps,cpuFans,battery