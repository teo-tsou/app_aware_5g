
sleep 25.01

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.3
pkill sipp

sleep 4.67

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.13
pkill chromium