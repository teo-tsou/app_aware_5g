
sleep 24.88

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.13
pkill sipp

sleep 5.59

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.92
pkill chromium