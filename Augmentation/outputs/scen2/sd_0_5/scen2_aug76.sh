
sleep 24.52

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.58
pkill sipp

sleep 5.79

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 50.9
pkill chromium