
sleep 26.09

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.31
pkill sipp

sleep 4.7

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 54.28
pkill chromium