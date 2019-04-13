#!/bin/bash

OUT_FILE="./$(date --date=@$(date +'%s') '+%Y%m%d-%H%M')-sysinfo.txt"

# 1. Kernel info
echo "KERNEL VERSION ------------------" > $OUT_FILE
cat /proc/version >> $OUT_FILE
echo " " >> $OUT_FILE

# 2. CPU info
echo "CPU INFO ------------------------" >> $OUT_FILE
cat /proc/cpuinfo >> $OUT_FILE
#cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor >> $OUT_FILE
echo " " >> $OUT_FILE

# 3. RAM info
echo "RAM INFO ------------------------" >> $OUT_FILE
cat /proc/meminfo >> $OUT_FILE
echo " " >> $OUT_FILE

# 4. Disks info
echo "DISKS INFO ----------------------" >> $OUT_FILE
df -H >> $OUT_FILE
echo " " >> $OUT_FILE

# 5. NVME and SSD related info
echo "SSD INFO ------------------------" >> $OUT_FILE
if ls /dev/nvme* 1> /dev/null 2>&1 && command -v nvme 1> /dev/null 2>&1 ; then
    sudo nvme list >> $OUT_FILE
    echo " " >> $OUT_FILE
    sudo nvme smart-log /dev/nvme0n1 >> $OUT_FILE
    echo " " >> $OUT_FILE
else
    echo "- NVME disks not found or nvme-cli didn't installed" >> $OUT_FILE
    echo "- NVME disks not found or nvme-cli didn't installed"
    echo " " >> $OUT_FILE
fi

if command -v smartctl 1> /dev/null 2>&1 ; then
    sudo smartctl -i /dev/sda >> $OUT_FILE
else
    echo "- Look like smartmontools didn't installed" >> $OUT_FILE
    echo "- Look like smartmontools didn't installed"
    echo " " >> $OUT_FILE
fi

# 6. Network
echo "NETWORK INFO --------------------" >> $OUT_FILE
ip a >> $OUT_FILE
echo " " >> $OUT_FILE

# 7. USB devices
echo "USB DEVICES ---------------------" >> $OUT_FILE
lsusb >> $OUT_FILE
echo " " >>$OUT_FILE

# 8. PCIe devices
echo "PCI-E DEVICES -------------------" >> $OUT_FILE
sudo lspci -v >> $OUT_FILE
echo " " >> $OUT_FILE

echo "CREATED: ${OUT_FILE}"
