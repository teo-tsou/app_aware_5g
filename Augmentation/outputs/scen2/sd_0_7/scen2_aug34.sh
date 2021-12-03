
sleep 24.67

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.77
pkill sipp

sleep 6.21

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.34
pkill chromium