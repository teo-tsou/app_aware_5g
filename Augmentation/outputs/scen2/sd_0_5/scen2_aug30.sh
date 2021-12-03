
sleep 24.89

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.34
pkill sipp

sleep 4.67

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.93
pkill chromium