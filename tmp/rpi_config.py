# Auto-deployed fallback config for rpi-mqtt-monitor
# Uses environment variables if present; safe defaults otherwise.
import os

version = "0.6.3"

# MQTT server configuration
mqtt_host = os.environ.get('MQTT_HOST', '127.0.0.1')
mqtt_user = os.environ.get('MQTT_USER', '')
mqtt_password = os.environ.get('MQTT_PASSWORD', '')
mqtt_port = int(os.environ.get('MQTT_PORT', '1883'))
mqtt_discovery_prefix = os.environ.get(
    'MQTT_DISCOVERY_PREFIX', 'homeassistant')
mqtt_topic_prefix = os.environ.get(
    'MQTT_TOPIC_PREFIX', 'rpi-' + os.uname().nodename)
mqtt_uns_structure = ""

# Retain / QOS
retain = True
qos = 0

# Home Assistant API configuration (optional)
hass_token = os.environ.get('HASS_TOKEN', '')
hass_host = os.environ.get('HASS_HOST', '')

# Messages configuration
language = 'en'

# Interval in seconds between probes
service_sleep_time = int(os.environ.get('RPI_MONITOR_INTERVAL', '60'))

# Other optional / compatibility keys referenced by the script
apt_updates = False
drive_temps = False
expire_after_time = int(os.environ.get('EXPIRE_AFTER_TIME', '0'))
get_content_outputfile = False
net_io = False
output_filename = ''
output_mode = ''
output_type = ''
random_delay = 0
ha_device_name = os.uname().nodename

# Features (defaults)
discovery_messages = True
restart_button = True
shutdown_button = True
update = True
display_control = False
os_user = 'root'
git_update = True
cpu_load = True
cpu_temp = True
used_space = True
used_space_path = '/'
voltage = False
sys_clock_speed = False
swap = False
memory = True
uptime = True
uptime_seconds = False
wifi_strength = True
wifi_ssid = True
network_speed_test = False
external_drives = []
ext_sensors = []
use_availability = False

# Backwards-compatible aliases / additional expected keys
wifi_signal = wifi_strength
# thermal zone (default 0); can be overridden with env var CPU_THERMAL_ZONE
cpu_thermal_zone = int(os.environ.get('CPU_THERMAL_ZONE', '0'))
# some versions expect a DBM value flag
wifi_signal_dbm = False
# Raspberry Pi specific options
rpi5_fan_speed = False
rpi_power_status = False

# update check interval (seconds)
update_check_interval = int(os.environ.get('UPDATE_CHECK_INTERVAL', '86400'))

# group messages / discovery
group_messages = False
config_update = True
