
sleep 23.98

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.7
pkill sipp

sleep 5.93

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.03
pkill chromium