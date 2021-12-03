
sleep 25.23

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.67
pkill sipp

sleep 6.61

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.41
pkill chromium