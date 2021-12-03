
sleep 24.73

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.1
pkill sipp

sleep 6.24

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.68
pkill chromium