# Dogecoin Price Tracker

Keep in mind that the app window will stay on top, providing you with live updates on the Dogecoin price without having to search for it

## Requirements

- Python 3.x
- `requests` library
- `plyer` library
- `Pillow` library

## Documentation

https://www.coingecko.com/api/documentation

## Important Commands:

```bash

# Steps
# 1 - Run the following command to change the execution policy for the current session in Power Shell (Windows)
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

# 2 - Activate the virtual environment

.\venv\Scripts\Activate

# 3 - Install in the session:

pip install plyer

pip install requests

pip install Pillow

# 4 - Run:

python dogecoin_price_gui.py