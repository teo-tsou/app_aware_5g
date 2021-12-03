
sleep 23.48

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.08
pkill sipp

sleep 5.39

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 50.43
pkill chromium