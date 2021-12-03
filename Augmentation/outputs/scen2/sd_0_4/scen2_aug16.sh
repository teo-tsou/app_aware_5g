
sleep 24.47

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.28
pkill sipp

sleep 5.78

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.33
pkill chromium