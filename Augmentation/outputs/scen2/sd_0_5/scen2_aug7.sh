
sleep 24.31

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.69
pkill sipp

sleep 4.69

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.07
pkill chromium