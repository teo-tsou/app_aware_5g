
sleep 24.44

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.23
pkill sipp

sleep 4.62

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.87
pkill chromium