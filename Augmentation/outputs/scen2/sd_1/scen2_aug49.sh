
sleep 26.59

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.54
pkill sipp

sleep 7.33

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 50.97
pkill chromium