
sleep 24.07

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.98
pkill sipp

sleep 5.33

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.42
pkill chromium