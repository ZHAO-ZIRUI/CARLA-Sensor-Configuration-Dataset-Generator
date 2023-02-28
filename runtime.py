app_root_path = None
app_loguru_format = '<c>{time:YYYY-MM-DD hh:mm:ss.SSSSS}</c> <m>|</m> <lvl>{level:<8}</lvl> <m>|</m> {message}'
app_loguru_level = 'INFO'
app_loguru_next_line = '\n' + ' ' * 42
app_is_demo = False

io_input_directory = './input'
io_output_directory = './output'

carla_ip_addr = '127.0.0.1'
carla_port = 2000
carla_map_name = 'Test1'
carla_setup_wait_time = 0.5
carla_fixed_delta_time = 0.05
carla_sync_wait_time = 0.5

carla_vehicle_bp_name = 'vehicle.tesla.model3'
carla_vehicle_transform = (0, 0, 2, 0, 0, 0)

carla_target_bp_name_options = [
    'static.prop.apartment01',
    'static.prop.apartment02',
    'static.prop.apartment03'
]
carla_target_r_min = 15
carla_target_r_max = 25

carla_sim_step_time = 0.5
carla_sim_max_count = 20