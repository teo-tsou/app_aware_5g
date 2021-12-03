
sleep 25.25

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 71.18
pkill sipp

sleep 6.02

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.48
pkill chromium