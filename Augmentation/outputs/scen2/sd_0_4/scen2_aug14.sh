
sleep 24.39

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.18
pkill sipp

sleep 4.79

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.34
pkill chromium