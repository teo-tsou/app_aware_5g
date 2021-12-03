
sleep 25.73

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.38
pkill sipp

sleep 4.87

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 50.67
pkill chromium