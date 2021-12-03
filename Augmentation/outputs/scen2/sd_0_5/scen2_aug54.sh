
sleep 24.76

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.6
pkill sipp

sleep 4.36

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.31
pkill chromium