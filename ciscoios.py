from netmiko import ConnectHandler
from config import RSA_PRIVATE_KEY, DST_DIR
from logger import init_log

log = init_log()


def export_config(device: dict, dst_dir: str = DST_DIR):
    """
    This functions connects to the router, then gets the configuration from router and export
    as file, the filename is the router's management ip address.
    :param device: dictionary from csv_to_dict function
    :param dst_dir: destination directory to save the configuration files.
    :return:
    """
    device.update(
        {
            "device_type": "cisco_ios",
            "use_keys": True,
            "key_file": RSA_PRIVATE_KEY
        }
    )
    with ConnectHandler(**device) as conn:
        log.info(f"Connected to {device['ip']}...")
        conn.send_command("terminal length 0")
        if not conn.check_enable_mode():
            log.info(f"{device['ip']} - entering enable mode.")
            conn.enable()
        config = conn.send_command("more running-config")
        log.info(f"{device['ip']} - Enumerated the running config file.")
        with open(f"{dst_dir}/{device.get('ip', 'router')}.cfg", "w") as f:
            f.write(config)
            log.info(f"{device['ip']} - running configuration has written to {device.get('ip', 'router')}.cfg")
