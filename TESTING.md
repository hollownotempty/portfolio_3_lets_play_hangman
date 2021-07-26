# Testing

## Bugs

1. After deployment, the program would fail to run and would throw an error 
    ```
    ModuleNotFoundError: No module named 'yaml'
    ```

    ![name_error](assets/images/screenshots/yaml_module.png)

    This was fixed by doing some research and discovering that a module named [PyYAML](https://pypi.org/project/PyYAML/)        

2. After deployment, input requests would not appear in the mock terminal but input could still be given, only showing the request after input was given. 

    ![mock_terminal](assets/images/screenshots/mock_terminal.png)
    After consulting the Slack community i found this could be solved by adding a ``` \n ``` to the end of any input.

