
sleep 25.56

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.47
pkill sipp

sleep 4.76

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.25
pkill chromium