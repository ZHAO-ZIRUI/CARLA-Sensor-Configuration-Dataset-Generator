## Application Arguments

This program allows the user to provide arguments in two ways:

1. **(RECOMMENDED)** Execute with command line startup arguments
2. Edit `<ROOT>/runtime.py` file

In this document we will describe in detail the definitions, effects, types and default values of all parameters.

| Args Name                         | Short | Long            | Editable | Link                                                                    |
|-----------------------------------|-------|-----------------|----------|-------------------------------------------------------------------------|
| app_root_path                     |       |                 | FALSE    | [app_root_path](#app_root_path)                                         |
| app_loguru_format                 |       |                 | FALSE    | [app_loguru_format](#app_loguru_format)                                 |
| app_loguru_level                  |       | --log           | TRUE     | [app_loguru_level](#app_loguru_level)                                   |
| app_loguru_next_line              |       |                 | FALSE    | [app_loguru_next_line](#app_loguru_next_line)                           |
| io_input_directory                | -i    | --input         | TRUE     | [io_input_directory](#io_input_directory)                               |
| io_output_directory               | -o    | --output        | TRUE     | [io_output_directory](#io_output_directory)                             |
| carla_ip_addr                     |       | --carla-ip-addr | TRUE     | [carla_ip_addr](#carla_ip_addr)                                         |
| carla_port                        |       | --carla-port    | TRUE     | [carla_port](#carla_port)                                               |
| carla_setup_wait_time             |       |                 | TRUE     | [carla_setup_wait_time](#carla_setup_wait_time)                         |
| carla_sim_step_wait_scenario_time | -s    | --wait-scenario | TRUE     | [carla_sim_step_wait_scenario_time](#carla_sim_step_wait_scenario_time) |
| carla_sim_step_wait_record_time   | -r    | --wait-record   | TRUE     | [carla_sim_step_wait_record_time](#carla_sim_step_wait_record_time)     |
| carla_sim_max_count               | -c    | --count         | TRUE     | [carla_sim_max_count](#carla_sim_max_count)                             |
| carla_sim_time_random             |       | --random        | TRUE     | [carla_sim_time_random](#carla_sim_time_random)                         |
| scenario_config_filepath          |       |                 | FALSE    | [scenario_config_filepath](#scenario_config_filepath)                   |

---

### app_root_path

- **Type:** *NONE*
- **Default:** `NONE`
- **Editable:** ❌ (*DYNAMIC VALUES FOR DATA EXCHANGE*)
- **CLI Argument:** ❌ (*NOT PROVIDE*)
- **Describe:** The root directory of the application, which is automatically detected and assigned by the program at startup.

### app_loguru_format

- **Type:** *str*
- **Default:** `'<c>{time:YYYY-MM-DD hh:mm:ss.SSSSS}</c> <m>|</m> <lvl>{level:<8}</lvl> <m>|</m> {message}'`
- **Editable:** ❌ (*CRITICAL VARIABLES FOR LOGGING SUBSYSTEM*)
- **CLI Argument:** ❌ (*NOT PROVIDE*)
- **Describe:** The encoder string for logging system (loguru), modification may cause errors.

### app_loguru_level

- **Type:** *str (OPTIONS)*
- **Default:** `'INFO'`
- **Editable:** ✅
- **CLI Argument:** ✅
  -  `--log <LOG_LEVEL>`
  -  **OPTIONS:** `TRACE`, `DEBUG`, `INFO`, `SUCCESS`, `WARNING`, `ERROR`, `CRITICAL`
- **Describe:** The minimum level of logging, with the options defined by loguru.

### app_loguru_next_line

- **Type:** *str (GENERATED VIA CODE)*
- **Default:** `'\n' + ' ' * 42`
- **Editable:** ❌ (*CRITICAL VARIABLES FOR LOGGING SUBSYSTEM*)
- **CLI Argument:** ❌ (*NOT PROVIDE*)
- **Describe:** Define the indentation of the next line in the logging system by defining the string programmatically.

### io_input_directory

- **Type:** *str*
- **Default:** `'./input'`
- **Editable:** ✅
- **CLI Argument:** ✅ 
  - `-i <INPUT_DIRECTORY>`
  - `--input <INPUT_DIRECTORY>`
- **Describe:** Input directory. The sensor configuration files in YAML format need to be stored in this directory.

### io_output_directory

- **Type:** *str*
- **Default:** `'./output'`
- **Editable:** ✅
- **CLI Argument:** ✅ 
  - `-o <OUTPUT_DIRECTORY>`
  - `--output <OUTPUT_DIRECTORY>`
- **Describe:** Output directory. The dataset will be generated to this directory.

### carla_ip_addr

- **Type:** *str*
- **Default:** `'127.0.0.1'`
- **Editable:** ✅
- **CLI Argument:** ✅ 
  - `--carla-ip-addr <CARLA_IP_ADDR>`
- **Describe:** CARLA simulator server's IP address in IPv4.

### carla_port

- **Type:** *num*
- **Default:** `2000`
- **Editable:** ✅
- **CLI Argument:** ✅ 
  - `--carla-port <CARLA_PORT>`
- **Describe:** CARLA simulator server's port.

### carla_setup_wait_time

- **Type:** *num*
- **Default:** `2.0`
- **Editable:** ✅
- **CLI Argument:** ❌ (*NOT PROVIDE*)
- **Describe:** The time program waits for the CARLA emulator to perform system-level operations like startup or clean. If your computer's performance is limited, especially if the CPU and IO are poor, you can **increase** this value appropriately. Instead you can **decrease** this value to get a smaller execution time.


### carla_sim_step_wait_scenario_time

- **Type:** *num*
- **Default:** `1.0`
- **Editable:** ✅
- **CLI Argument:** ✅ 
  - `-s <CARLA_SIM_STEP_WAIT_SCENARIO_TIME>`
  - `--wait-scenario <CARLA_SIM_STEP_WAIT_SCENARIO_TIME>`
- **Describe:** The time program waits for the CARLA emulator to load scenario slice. If you are experiencing LOD problems (Models and textures do not load as expected), you can **increase** this value appropriately. Instead you can **decrease** this value to get a smaller execution time.

### carla_sim_step_wait_record_time

- **Type:** *num*
- **Default:** `1.0`
- **Editable:** ✅
- **CLI Argument:** ✅ 
  - `-r <CARLA_SIM_STEP_WAIT_RECORD_TIME>`
  - `--wait-record <CARLA_SIM_STEP_WAIT_RECORD_TIME>`
- **Describe:** The time program waits for the CARLA emulator to save image (`.png`) or pointcloud (`.pcd`) data to disk. If the number of your data is incorrect or the data content is missing or corrupted, you can **increase** this value appropriately. Instead you can **decrease** this value to get a smaller execution time.

### carla_sim_max_count

- **Type:** *num (int)*
- **Default:** `20`
- **Editable:** ✅
- **CLI Argument:** ✅ 
  - `-c <CARLA_SIM_MAX_COUNT>`
  - `--count <CARLA_SIM_MAX_COUNT>`
- **Describe:** This value refers to the number of slices performed during the execution of each scenario in the program, and this value also represents the number of generated data pairs.

### carla_sim_time_random

- **Type:** *num (int)*
- **Default:** `0`
- **Editable:** ✅
- **CLI Argument:** ✅ 
  - `--random <CARLA_SIM_TIME_RANDOM>`
- **Describe:** This value indicates the randomness of the sampling time point when slicing the scenario. The random numbers take values in `(-<CARLA_SIM_TIME_RANDOM>, +<CARLA_SIM_TIME_RANDOM>)`. 


### scenario_config_filepath

- **Type:** *str*
- **Default:** `./scenario.yaml`
- **Editable:** ❌ (*CRITICAL VARIABLES*)
- **CLI Argument:** ❌ (*NOT PROVIDE*)
- **Describe:** Relative paths to scenario profiles.
