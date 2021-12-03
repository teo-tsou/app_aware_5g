
sleep 25.29

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.98
pkill sipp

sleep 6.64

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.5
pkill chromium