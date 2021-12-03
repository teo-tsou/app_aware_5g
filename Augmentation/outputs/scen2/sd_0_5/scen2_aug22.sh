
sleep 26.17

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.78
pkill sipp

sleep 4.92

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.62
pkill chromium