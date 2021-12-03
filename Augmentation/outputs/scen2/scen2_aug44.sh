
sleep 25.51

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.31
pkill sipp

sleep 4.61

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.75
pkill chromium