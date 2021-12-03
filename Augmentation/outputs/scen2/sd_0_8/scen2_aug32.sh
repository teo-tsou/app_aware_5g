
sleep 25.62

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.67
pkill sipp

sleep 2.96

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.15
pkill chromium