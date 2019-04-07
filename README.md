# temp-loggah
It is for hardware stress tests on Linux. So install `lm-sensors` first, then perform `sensors-detect`. Also you may want to install `stress-ng` and to use it like this: `stress-ng --cpu 0 --hdd 0 --vm 0 --io 0 --timeout 3h`. Hopefully not.

- Everything hardcoded! Check variables first
- Use [venv](https://docs.python.org/3/library/venv.html) for [matplotlib](https://matplotlib.org/index.html) installation
- Do not forget to `chmod +x` all .sh files

### Workflow
Make sure `sensors` works → Get system information with `get-sysinfo.sh` → Turn logging on with `log-to-file.sh` → Run stress tests and burn your PC with heavy math → Feed resulted .csv file to `plotter.py`.

[<img src="https://github.com/Atarity/temp-loggah/raw/master/data/image.png"/>](https://github.com/Atarity/temp-loggah/raw/master/data/image.png)