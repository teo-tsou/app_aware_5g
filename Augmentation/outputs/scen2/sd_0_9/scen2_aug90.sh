
sleep 23.01

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.49
pkill sipp

sleep 5.01

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 50.54
pkill chromium