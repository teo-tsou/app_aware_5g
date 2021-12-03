
sleep 25.6

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.07
pkill sipp

sleep 3.85

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.37
pkill chromium