
sleep 24.41

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.77
pkill sipp

sleep 5.42

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.46
pkill chromium