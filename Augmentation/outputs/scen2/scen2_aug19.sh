
sleep 25.59

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.04
pkill sipp

sleep 3.97

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.82
pkill chromium