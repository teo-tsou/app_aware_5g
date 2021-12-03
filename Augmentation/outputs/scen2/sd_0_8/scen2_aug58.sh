
sleep 26.89

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 72.31
pkill sipp

sleep 5.51

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.2
pkill chromium