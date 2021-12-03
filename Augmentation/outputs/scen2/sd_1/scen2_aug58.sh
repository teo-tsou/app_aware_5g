
sleep 23.55

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.93
pkill sipp

sleep 5.53

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.48
pkill chromium