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