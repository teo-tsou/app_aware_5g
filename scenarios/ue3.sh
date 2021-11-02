sleep 11
start_time=$(date +%s)
# perform a task
end_time=$(date +%s)

#elapsed time with second resolution
elapsed=$(( end_time - start_time ))
while [ $elapsed -lt 10 ]
do
        curl -H 'Cache-Control: no-cache' 192.168.3.103:80
        sleep 0.1
        echo "Elapsed time: $elapsed"
        end_time=$(date +%s)
        elapsed=$(( end_time - start_time ))
done


