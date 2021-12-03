
sleep 24.53

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.08
pkill sipp

sleep 6.17

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.72
pkill chromium