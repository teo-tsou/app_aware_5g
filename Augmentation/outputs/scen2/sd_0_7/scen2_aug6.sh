
sleep 25.12

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.73
pkill sipp

sleep 5.4

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.3
pkill chromium