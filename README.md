# Pico Plant Watering 🌿

This project runs on a Raspberry Pi Pico W. It connects to Wi-Fi, monitors the water level of a plant ("Gary") using an analog soil moisture sensor on Pin 26, and sends a Telegram notification if the plant is thirsty (when the median of 5 consecutive readings drops below 400).

## Hardware Components
- Raspberry Pi Pico W
- Soil moisture sensor connected to Pin 26 (ADC0)

## Software Components
- `water_level_check.py`: The main script that runs the Wi-Fi connection, polling loop, and Telegram notifications.
- `secrets.py`: Stores your Wi-Fi credentials and Telegram Bot configurations.
- `statistics.py`: Provides lightweight statistical helpers (like median) for MicroPython.
