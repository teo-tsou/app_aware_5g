
sleep 23.46

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 72.58
pkill sipp

sleep 7.22

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 50.67
pkill chromium