
sleep 25.79

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.72
pkill sipp

sleep 6.25

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 54.08
pkill chromium