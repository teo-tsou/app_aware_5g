
sleep 25.78

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.21
pkill sipp

sleep 6.3

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.75
pkill chromium