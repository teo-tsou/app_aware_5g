
sleep 25.08

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.44
pkill sipp

sleep 5.08

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.29
pkill chromium