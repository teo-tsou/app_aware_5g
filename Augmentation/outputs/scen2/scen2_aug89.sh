
sleep 24.07

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.98
pkill sipp

sleep 2.86

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.42
pkill chromium