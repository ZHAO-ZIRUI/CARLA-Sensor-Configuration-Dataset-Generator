argparse_description = """
The CARLA Sensor Configuration Iterator is an open-source programme that allows you to generate a CARLA Simulator dataset that is based on a sensor configuration file specified by the user. 
"""
argparse_help_none = "*"*20
argparse_carla_ip_addr = "Carla server's IP address in IPv4"
argparse_carla_port = "Carla server's port"
argparse_input = "Input directory. The sensor configuration files in YAML format need to be stored in this directory"
argparse_output = "Output directory. The dataset will be generated to this directory"
argparse_demo = "Run pre-coded demo with 1 job and 3 sensors"
argparse_r_min = "Minimum radius value of the random zone"
argparse_r_max = "Maximum radius value of the random zone"
argparse_count = "Number of randomised trials executed per Job"
argparse_delta_t = "PLEASE READ THE README! Interval between each collection in Job"
argparse_log = "Log level of the program"
argparse_wait_scenario = "The time program waits for the CARLA emulator to load scenario slice. If you are experiencing LOD problems (Models and textures do not load as expected), you can increase this value appropriately. Instead you can decrease this value to get a smaller execution time"
argparse_wait_record = "The time program waits for the CARLA emulator to save image (`.png`) or pointcloud (`.pcd`) data to disk. If the number of your data is incorrect or the data content is missing or corrupted, you can increase this value appropriately. Instead you can decrease this value to get a smaller execution time"
argparse_random = "This value indicates the randomness of the sampling time point when slicing the scenario"

argparse_epilog = """
GITHUB: https://github.com/ZHAO-Zirui/CARLA-Sensor-Configuration-Iterator.git
"""