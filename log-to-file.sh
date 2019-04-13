#!/bin/bash

OUT_FILE="./$(date --date=@$(date +'%s') '+%Y%m%d-%H%M')-temp-log.csv"

echo "ts;Time;temp1;temp2;Package-id-0;Core-0-temp;Core-1-temp;Thread-0-freq;Thread-1-freq;Thread-2-freq;Thread-3-freq;" > $OUT_FILE

while true
do
    # Logging time, temperatures and cores frequency to file
    echo -n "$(date +"%s");" >> $OUT_FILE
    echo -n "$(date --date=@$(date +'%s') '+%Y-%m-%d-%H:%M');" >> $OUT_FILE
    TEMP="$(sensors | sed -n "/+/p" | sed "s/^[a-zA-Z0-9 ]*:\s*\([0-9.+-]*\).*$/\1/" | sed ':a;N;$!ba;s/\n/;/g' | tee /dev/tty);"
    echo -n $TEMP >> $OUT_FILE
    echo "$(cat /proc/cpuinfo | grep 'MHz' | grep -o '[0-9].\+' | sed ':a;N;$!ba;s/\n/;/g');" >> $OUT_FILE
    sleep 3
done
