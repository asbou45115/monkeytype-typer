# monkeytype-typer

This project opens up monkeytype type racing test on microsoft edge and auto types the prompt. The interval of which the prompt is typed out can be changed from 0.01 to any other value, however, values less than this cause a WPM of 'Infinite' 

https://github.com/user-attachments/assets/f645040d-9f93-4a88-be2a-a4324647073f

![image](https://github.com/user-attachments/assets/a4514580-b0f3-4c15-8cb8-2c374a8f8057)

## Installation

- Download microsoft edge driver from [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?cs=1873324239&form=MA13LH) OR respective browser
- Place the driver file within desired location (default written in script is C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe) and accordingly change 'PATH' in code as follows:
  ```bash
  PATH = r"\PATH\TO\DRIVER.exe"
  ```

NOTE: if using different browser, the selenium code must be changed to the specific browser being used 

```bash
pip install -r requirements.txt
```

## Usage

To run the script enter in the terminal 

```bash
python3 typer.py
```

