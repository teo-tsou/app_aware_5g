
sleep 25.79

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.67
pkill sipp

sleep 5.37

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.89
pkill chromium