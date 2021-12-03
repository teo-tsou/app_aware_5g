
sleep 24.17

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.45
pkill sipp

sleep 5.0

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.79
pkill chromium