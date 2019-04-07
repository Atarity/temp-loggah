#!/bin/bash

OUT_FILE="./$(date --date=@$(date +'%s') '+%Y%m%d-%H%M')-temp-log.csv"

echo "ts;Time;temp1;temp2;Package id 0;Core 0;Core 1;" > $OUT_FILE

while true
do
    # Logging time as UNIX time and temperatures to file
    echo -n "$(date +"%s");" >> $OUT_FILE
    echo -n "$(date --date=@$(date +'%s') '+%Y-%m-%d-%H:%M');" >> $OUT_FILE
    #sensors | sed -n "/+/p" | sed "s/^[a-zA-Z0-9 ]*:\s*\([0-9.+-]*\).*$/\1/" | sed ":a;N;$!ba;s/\n/;\t/g" >> $OUT_FILE
    TEMP="$(sensors | sed -n "/+/p" | sed "s/^[a-zA-Z0-9 ]*:\s*\([0-9.+-]*\).*$/\1/" | sed ':a;N;$!ba;s/\n/;\t/g' | tee /dev/tty);"
    echo $TEMP >> $OUT_FILE

    sleep 3
done
