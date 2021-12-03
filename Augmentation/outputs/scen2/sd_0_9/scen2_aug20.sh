
sleep 23.81

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.1
pkill sipp

sleep 4.62

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 50.85
pkill chromium