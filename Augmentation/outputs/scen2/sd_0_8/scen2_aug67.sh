
sleep 24.63

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.5
pkill sipp

sleep 5.22

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.89
pkill chromium