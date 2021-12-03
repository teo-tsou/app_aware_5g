
sleep 25.49

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 71.2
pkill sipp

sleep 4.62

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.66
pkill chromium