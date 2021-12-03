sleep 22.05

#WEB-SERVER
start_time=$(date +%s)
# perform a task
end_time=$(date +%s)

#elapsed time with second resolution
elapsed=$(( end_time - start_time ))
while [ $elapsed -lt 7.75 ]
do
        curl -H 'Cache-Control: no-cache' 192.168.3.103:80
        echo "Elapsed time: $elapsed"
        end_time=$(date +%s)
        elapsed=$(( end_time - start_time ))
done

sleep 16.22

#WEB-SERVER
start_time=$(date +%s)
# perform a task
end_time=$(date +%s)

#elapsed time with second resolution
elapsed=$(( end_time - start_time ))
while [ $elapsed -lt 2.68 ]
do
        curl -H 'Cache-Control: no-cache' 192.168.3.103:80
        echo "Elapsed time: $elapsed"
        end_time=$(date +%s)
        elapsed=$(( end_time - start_time ))
done

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.03
pkill chromium


#WEB-SERVER
start_time=$(date +%s)
# perform a task
end_time=$(date +%s)

#elapsed time with second resolution
elapsed=$(( end_time - start_time ))
while [ $elapsed -lt 49.7 ]
do
        curl -H 'Cache-Control: no-cache' 192.168.3.103:80
        echo "Elapsed time: $elapsed"
        end_time=$(date +%s)
        elapsed=$(( end_time - start_time ))
done
