
sleep 24.02

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.92
pkill sipp

sleep 3.98

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.29
pkill chromium