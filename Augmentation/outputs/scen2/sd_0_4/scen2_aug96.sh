
sleep 24.74

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.13
pkill sipp

sleep 5.82

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.78
pkill chromium