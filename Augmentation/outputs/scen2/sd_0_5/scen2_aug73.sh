
sleep 24.55

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.12
pkill sipp

sleep 4.71

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.07
pkill chromium