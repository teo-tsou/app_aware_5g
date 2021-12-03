
sleep 25.76

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.85
pkill sipp

sleep 5.35

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.12
pkill chromium