
sleep 25.7

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.93
pkill sipp

sleep 5.85

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.01
pkill chromium