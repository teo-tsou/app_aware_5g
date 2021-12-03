
sleep 23.94

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 67.73
pkill sipp

sleep 6.39

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 50.76
pkill chromium