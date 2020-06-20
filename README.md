Plug-in Template for Constructing Accelergy Plug-ins
--------------------------------------------------------

Accelergy allows users to define their own plug-ins that perform estimations
 specific to the architectures under evaluation. We provide this plug-in template 
as a starting point for the construction of a user-defined plug-in that can interact 
Accelergy.

### How to use this template

#### Step 1: make Accelergy aware of this plug-in

- Option 1: modify the Accelergy config file (`~\.config\accelergy\accelergy_config.yaml`)
            to include the absolute path to this folder, 
            i.e., add another item under the `estimator_plug_ins` key inside the config file.
- Option 2: run `pip3 install .` to install this plug-in into your system, 
            Accelergy will be able to identify and locate this plug-in automatically. 
            Note this plug-in needs to be REINSTALLED everytime it is updated.


#### Step 2: populate the interface functions
Populate the interface functions provided inside `plugin_wrapper.py` to implement your logic for
energy and area estimations. Detailed comments can be found in the files. 

#### Optional: modify the file names to reflect your plug-in's name











