
sleep 25.77

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.78
pkill sipp

sleep 5.5

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.73
pkill chromium