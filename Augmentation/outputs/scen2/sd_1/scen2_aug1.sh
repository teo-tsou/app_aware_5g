
sleep 25.27

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.69
pkill sipp

sleep 5.39

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.27
pkill chromium