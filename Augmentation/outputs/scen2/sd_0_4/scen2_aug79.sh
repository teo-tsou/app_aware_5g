
sleep 24.8

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.88
pkill sipp

sleep 4.78

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.1
pkill chromium