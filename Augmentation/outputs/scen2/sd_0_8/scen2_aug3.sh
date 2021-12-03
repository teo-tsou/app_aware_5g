
sleep 27.13

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.79
pkill sipp

sleep 3.79

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.56
pkill chromium