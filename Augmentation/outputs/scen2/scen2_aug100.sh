
sleep 24.62

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.46
pkill sipp

sleep 2.69

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.82
pkill chromium