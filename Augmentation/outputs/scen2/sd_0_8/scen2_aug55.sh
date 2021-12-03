
sleep 25.17

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.7
pkill sipp

sleep 4.24

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.68
pkill chromium