
sleep 24.95

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.46
pkill sipp

sleep 4.35

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.01
pkill chromium