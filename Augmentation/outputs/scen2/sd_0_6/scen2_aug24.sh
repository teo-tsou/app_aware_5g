
sleep 23.91

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.79
pkill sipp

sleep 5.6

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.06
pkill chromium