#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 76.7
pkill chromium

#WEB-SERVER
start_time=$(date +%s)
# perform a task
end_time=$(date +%s)

#elapsed time with second resolution
elapsed=$(( end_time - start_time ))
while [ $elapsed -lt 22.13 ]
do
        curl -H 'Cache-Control: no-cache' 192.168.3.103:80
        echo "Elapsed time: $elapsed"
        end_time=$(date +%s)
        elapsed=$(( end_time - start_time ))
done
  
sleep 28.13

#WEB-SERVER
start_time=$(date +%s)
# perform a task
end_time=$(date +%s)

#elapsed time with second resolution
elapsed=$(( end_time - start_time ))
while [ $elapsed -lt 23.67 ]
do
        curl -H 'Cache-Control: no-cache' 192.168.3.103:80
        echo "Elapsed time: $elapsed"
        end_time=$(date +%s)
        elapsed=$(( end_time - start_time ))
done
