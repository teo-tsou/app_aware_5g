
sleep 25.19

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 71.0
pkill sipp

sleep 5.05

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.93
pkill chromium