
sleep 24.54

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.64
pkill sipp

sleep 4.43

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.17
pkill chromium