
sleep 24.61

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.32
pkill sipp

sleep 3.7

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.75
pkill chromium