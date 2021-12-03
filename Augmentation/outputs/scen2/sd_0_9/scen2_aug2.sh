
sleep 25.44

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 71.44
pkill sipp

sleep 3.87

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.64
pkill chromium