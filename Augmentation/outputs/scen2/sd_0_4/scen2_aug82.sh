
sleep 25.78

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.8
pkill sipp

sleep 5.21

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.28
pkill chromium