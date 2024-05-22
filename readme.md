## Information before using
I changed all the paths to prevent possible information leakage.
In order to run the code, you will need to configure the paths to match your own system (search "path/to")

Note that Python files end with '_t' in '/models' and ' /exps'  means using Dual-Arch

## How to Use

Change settings (see ' /exps' ).

- **init-cls**: The number of classes in the first incremental stage. 
- **increment**: The number of classes in each incremental stage. By default, the number of classes per incremental stage is equivalent per stage.
- **model_name**: The model's name should be selected from the methods in '/model', *e.g.*, `lwf`, `icarl`,  `lwf_t`, `icarl_t`.

Select a CL method in eva.py or main.py, then run.