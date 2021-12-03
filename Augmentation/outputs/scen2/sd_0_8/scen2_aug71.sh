
sleep 25.73

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.49
pkill sipp

sleep 3.29

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.26
pkill chromium