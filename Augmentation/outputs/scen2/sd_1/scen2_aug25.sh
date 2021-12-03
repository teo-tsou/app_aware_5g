
sleep 25.82

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.26
pkill sipp

sleep 4.42

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.62
pkill chromium