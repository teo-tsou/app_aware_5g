
sleep 26.53

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.1
pkill sipp

sleep 4.02

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.81
pkill chromium