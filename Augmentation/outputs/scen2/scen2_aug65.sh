
sleep 25.56

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.45
pkill sipp

sleep 5.0

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.64
pkill chromium