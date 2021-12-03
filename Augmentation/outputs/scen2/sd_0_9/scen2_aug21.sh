
sleep 25.09

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.92
pkill sipp

sleep 5.74

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.97
pkill chromium