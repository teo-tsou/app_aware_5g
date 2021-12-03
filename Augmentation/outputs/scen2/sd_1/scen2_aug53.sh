
sleep 25.2

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.2
pkill sipp

sleep 5.55

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.0
pkill chromium