# Raspberry Adventures Monorepo 🍓

Welcome to the **Raspberry Adventures** repository! This is a branch-based monorepo containing various MicroPython and physical computing projects designed for the **Raspberry Pi Pico** and **Raspberry Pi Pico W**.

## Monorepo Structure 📁
Instead of subfolders, this repository maintains separate projects on dedicated git branches. Switch to the corresponding branch to view and work on that project's codebase.

| Branch Name | Project Name | Description | Key Files |
| :--- | :--- | :--- | :--- |
| **`pico_plant_watering`** | **Gary the Plant Alert 🌿** | Re-connectable soil moisture sensor on Pico W that polls a capacity sensor on Pin 26 (ADC0) and sends a Telegram notification if the plant needs water. | `water_level_check.py`, `secrets.py`, `statistics.py` |
| **`pico_scripts`** | **Pico Hardware Scripts 💡** | Standard board and GPIO script collection including a 1-second LED toggler, a dual red/blue police siren sequence, and basic board utilities. | `blinker1s.py`, `board_led.py`, `police.py`, `helloThere.py` |
| **`plant_watering`** | **MicroPython Stats Library 📈** | A memory-efficient implementation of mathematical and statistical operations (median, mean, mode, stdev, variance) optimized for MicroPython. | `statistics.py` |

---

## How to Switch Projects 🚀

To explore or deploy a specific project, switch to its branch using `git checkout`:

```bash
# Switch to Gary the Plant Watering Alert system
git checkout pico_plant_watering

# Switch to the Pico basic scripts collection
git checkout pico_scripts

# Switch to the MicroPython statistics utility branch
git checkout plant_watering
```

---

## How to Run on Raspberry Pi Pico 💻

1. **Setup Thonny IDE**: Download and install [Thonny](https://thonny.org/).
2. **Connect Pico**: Plug in your Raspberry Pi Pico/Pico W via micro-USB while holding the `BOOTSEL` button (or simply plug it in if MicroPython is already installed).
3. **Select Interpreter**: Set the interpreter in Thonny to **MicroPython (Raspberry Pi Pico)** in the bottom right corner.
4. **Deploy Files**: 
   - Open the files from your chosen branch in Thonny.
   - For config files (like `secrets.py` on `pico_plant_watering`), customize the variables with your credentials.
   - Save the files directly onto the **Raspberry Pi Pico**.
5. **Run**: Press **F5** or the green "Run" button in Thonny to execute the script!
