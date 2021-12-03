
sleep 23.46

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.8
pkill sipp

sleep 5.75

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.32
pkill chromium