
sleep 23.56

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.36
pkill sipp

sleep 4.77

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.81
pkill chromium