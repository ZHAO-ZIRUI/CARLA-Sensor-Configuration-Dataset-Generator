# CARLA Sensor Configuration Dataset Generator

**VERSION: 0.2.0**

The CARLA Sensor Configuration Dataset Generator is an open-source program that allows you to generate a [CARLA Simulator](https://github.com/carla-simulator/carla) dataset that is based on a sensor configuration file specified by the user. 

## Processes and Trials

The application takes a set of sensor configuratiom inputs from a file as YAML format, decodes them into a job sequence, performs a trial and finally generates a dataset that matches the sensor configuratiom description. The process is shown in the diagram below:



## Requirments

- Python 3.8.X Environment
- Special version of the self-built CARLA Simulator (Includes customised maps and assets)
  - Windows: [OneDrive](https://1drv.ms/u/s!AlsjJokLSSi8gekoeku4vFsb4ZAYew?e=J0gQIM) / [Baidu Netdisk](https://pan.baidu.com/s/1gunABaw2A10OQiTd1C9uig?pwd=kk93)
  - Linux: [OneDrive](https://1drv.ms/u/s!AlsjJokLSSi8gekniz4iciEvE22a0g?e=p7DDtY) / [Baidu Netdisk](https://pan.baidu.com/s/1YrpKcAGLfnTv4o7DrSS9qQ?pwd=w625)

## Install

1. Decompression self-built CARLA Simulator to `{CARLA_ROOT}`
   
   > `{CARLA_ROOT}` is the root directory of **CARLA Simulator**. You can define this directory yourself. In the following, please replace the keyword with the appropriate directory.

2. Clone or Decompression this program to `{APP_ROOT}`

    > `{APP_ROOT}` is the root directory of **this application**. You can define this directory yourself. In the following, please replace the keyword with the appropriate directory.

3. **(OPTIONAL)** Create and activate virutal Python environment
   
    ```
    # Create virtual environment
    $ cd {APP_ROOT}
    $ python -m venv ./venv

    # [Windows+Powershell] Activate venv
    $ .\venv\Scripts\Activate.ps1

    # [Windwos+CMD] Activate venv
    $ .\venv\Scripts\activate.bat

    # [Linux] Activate venv
    $ source ./venv/bin/activate

    ```

4. Install requirements Python packages
   
    ```
    # Install public packages
    $ pip install -r ./requirements.txt

    # [Windows] Install carla python packages
    $ pip install {CARLA_ROOT}\PythonAPI\carla\dist\carla-0.9.13-cp38-cp38-win_amd64.whl

    # [Linux] Install carla python packages
    $ pip install {CARLA_ROOT}/PythonAPI/carla/dist/carla-0.9.13-cp38-p38-liunux_x86_64_whl
    ```

    > **⚠ WARN:** You must use the `.whl` package included in the CARLA distribution we provide, otherwise an unknown error may be raised!

## Start

This program contains a simple demo that consists of a set of sensor configuration files (File: `./input/demo_config_*.yaml`), a set of road test scenario replay file (File: `./scenarios/demo*.log`) and their profiles (File: `./scenario.yaml`). This means that you can run the program directly and try to [set up sensors](#setup-sensors) and [set up sceanrios](#setup-scenarios) later.

1. Start CARLA Simulator and keep it on at all times.

    ```
    $ cd {CARLA_ROOT}

    # [Windows]
    # You can also open it directly by double-clicking on it using the Windows GUI.
    $ .\CarlaUE4.exe

    # [Linux]
    $ ./CarlaUE4.sh
    ```

    > **⚠ WARN:** The program will automatically reset and set up CARLA world, please do not run other CARLA clients during the whole process.

2. Start demo:
   
    ```
    $ python ./main.py -c 20
    ```

If everything is all right, you will not see any log of the ERROR level in the system standard output. And in the output folder (`{./output/}`), you will see the following file structure.

<!-- TODO:UPDATE OUTPUT -->
```
output
 ├─demo_config_1  # Result from config file demo (demo_config_1.yaml)
 │  ├─0           # The first sensor in the list of yaml files 
 │  └─1           # The sencond sensor in the list of yaml files
 ├─demo_config_2  # Result from config file demo (demo_config_2.yaml)
 │  ├─0
 │  └─1
 └─Demo  # Result from pre-coded demo
     ├─0
     │  ├─123.png  # camera -> png result
     │  ├─...
     │  └─143.png  # the number of result: 20
     ├─1
     │  ├─123.ply  # lidar -> ply result
     │  ├─...
     │  └─143.ply    
     └─2
        ├─123.csv  # radar -> csv result
        ├─...
        └─143.csv  
```


## Setup Sensors

The sensor configuration file is encoded in [YAML format](https://yaml.org/). A single `.yaml` file represents a set of sensor settings in this program. And the program also supports multiple config inputs, iterating through all the `.yaml` files in the input folder.

A sensor configuration file looks like:

```
-
 blueprint_name: 'sensor.camera.rgb'
 transform:
  x: 0.8
  y: 0.0
  z: 1.8
  pitch: 0.0
  yaw: 0.0
  roll: 0.0
 attribute:
  image_size_x: 1920
  image_size_y: 1920
```
> You can find the full example configuration file [here](./input/demo_config_1.yaml)

The sensor configuration file is encoded as follows structure:

| Level | Data / Name    | Type    | Requried | Description                            |
|-------|----------------|---------|----------|----------------------------------------|
| 0     | -              | list    | TRUE     | Element identifiers in the root list   |
| 1     | blueprint_name | str     | TRUE     | Sensor blueprint name defined by CARLA |
| 1     | transform      | dict    | TRUE     | Sensor transform defined by CARLA      |
| 2     | x              | num     | TRUE     | transform - location - x               |
| 2     | y              | num     | TRUE     | transform - location - y               |
| 2     | z              | num     | TRUE     | transform - location - z               |
| 2     | pitch          | num     | TRUE     | transform - rotation - pitch           |
| 2     | yaw            | num     | TRUE     | transform - rotation - yaw             |
| 2     | roll           | num     | TRUE     | transform - rotation - roll            |
| 1     | attribute      | dict    | TRUE     | Sensor attributes dictionary           |
| 2     |                |         |          | Attribute elements can be NULL         |
| 2     | image_size_x   | num/str | FALSE    | Sensor attribute node defined by CARLA |

> Here are some useful references:
> - CARLA Simulator Blueprint Library (https://carla.readthedocs.io/en/latest/bp_library/)
> - CARLA Transform Define (https://carla.readthedocs.io/en/latest/python_api/#carla.Transform)
> - CARLA Sensor Reference (https://carla.readthedocs.io/en/latest/ref_sensors/)

## Setup Scenarios
<!-- TODO:ADD CONTENT -->

## Arguments

<!-- TODO:ARGUMENTS DETAILS -->
Program can control behaviour by adding startup arguments, such as running examples (`--demo`) or displaying help (`-h` or `--help`).

You can try the following code to access the arguments help screen:

```
$ python ./main.py -h
```

If you need to change the default values of the arguments, you can found them at `./runtime.py`

> **⚠ WARN:** This operation is risky and may result in unknown errors!

## Adjustments

Due to the different configurations of the hardware devices running the CARLA simulator, in some cases it may be necessary to adjust the startup arguments of this program to ensure correct and efficient data acquisition.


## About

### License

The CARLA Sensor Configuration Iterator spcific code is distributed under MIT License.

### Authors

The CARLA Sensor Configuration Iterator specific code is the work of **ZHAO Zirui** during his employment at the Southern University of Science and Technology. He will provide limited open source maintenance for the duration of his employment.
