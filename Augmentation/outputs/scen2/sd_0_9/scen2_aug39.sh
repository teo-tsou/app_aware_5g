
sleep 24.55

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.62
pkill sipp

sleep 2.66

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.62
pkill chromium