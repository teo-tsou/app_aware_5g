
sleep 26.34

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.95
pkill sipp

sleep 7.14

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.75
pkill chromium