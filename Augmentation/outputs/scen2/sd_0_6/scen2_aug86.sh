
sleep 24.4

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.35
pkill sipp

sleep 3.62

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.37
pkill chromium