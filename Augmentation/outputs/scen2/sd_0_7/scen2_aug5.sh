
sleep 23.75

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.8
pkill sipp

sleep 5.03

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.05
pkill chromium