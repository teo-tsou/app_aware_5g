sleep 21.6

#WEB-SERVER
start_time=$(date +%s)
# perform a task
end_time=$(date +%s)

#elapsed time with second resolution
elapsed=$(( end_time - start_time ))
while [ $elapsed -lt 6.22 ]
do
        curl -H 'Cache-Control: no-cache' 192.168.3.103:80
        echo "Elapsed time: $elapsed"
        end_time=$(date +%s)
        elapsed=$(( end_time - start_time ))
done

sleep 16.85

#WEB-SERVER
start_time=$(date +%s)
# perform a task
end_time=$(date +%s)

#elapsed time with second resolution
elapsed=$(( end_time - start_time ))
while [ $elapsed -lt 1.58 ]
do
        curl -H 'Cache-Control: no-cache' 192.168.3.103:80
        echo "Elapsed time: $elapsed"
        end_time=$(date +%s)
        elapsed=$(( end_time - start_time ))
done

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.96
pkill chromium


#WEB-SERVER
start_time=$(date +%s)
# perform a task
end_time=$(date +%s)

#elapsed time with second resolution
elapsed=$(( end_time - start_time ))
while [ $elapsed -lt 50.68 ]
do
        curl -H 'Cache-Control: no-cache' 192.168.3.103:80
        echo "Elapsed time: $elapsed"
        end_time=$(date +%s)
        elapsed=$(( end_time - start_time ))
done
