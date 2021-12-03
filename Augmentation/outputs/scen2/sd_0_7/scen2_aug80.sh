
sleep 24.66

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.6
pkill sipp

sleep 5.99

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 50.63
pkill chromium