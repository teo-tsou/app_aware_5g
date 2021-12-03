
sleep 24.31

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.14
pkill sipp

sleep 5.87

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 50.19
pkill chromium