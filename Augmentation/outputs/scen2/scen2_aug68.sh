
sleep 25.77

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.84
pkill sipp

sleep 6.43

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.45
pkill chromium