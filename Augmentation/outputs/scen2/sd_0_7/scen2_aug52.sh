
sleep 25.34

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.69
pkill sipp

sleep 4.35

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 50.73
pkill chromium