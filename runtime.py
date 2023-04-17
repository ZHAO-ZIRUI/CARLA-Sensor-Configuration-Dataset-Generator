app_root_path = None
app_loguru_format = '<c>{time:YYYY-MM-DD hh:mm:ss.SSSSS}</c> <m>|</m> <lvl>{level:<8}</lvl> <m>|</m> {message}'
app_loguru_level = 'INFO'
app_loguru_next_line = '\n' + ' ' * 42
app_is_demo = False

io_input_directory = './input'
io_output_directory = './output'

carla_ip_addr = '127.0.0.1'
carla_port = 2000
carla_setup_wait_time = 2.0

carla_sim_step_wait_scenario_time = 1.0
carla_sim_step_wait_record_time = 1.0
carla_sim_max_count = 20
carla_sim_time_random = 0.0

scenario_config_filepath = './scenario.yaml'