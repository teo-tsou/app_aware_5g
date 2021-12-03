
sleep 25.4

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.83
pkill sipp

sleep 4.6

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.87
pkill chromium