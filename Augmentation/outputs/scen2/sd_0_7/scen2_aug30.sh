
sleep 25.56

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.37
pkill sipp

sleep 6.02

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 50.95
pkill chromium