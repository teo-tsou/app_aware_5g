
sleep 26.87

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.85
pkill sipp

sleep 7.34

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 50.47
pkill chromium