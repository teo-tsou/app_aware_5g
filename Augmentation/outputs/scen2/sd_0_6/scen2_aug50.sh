
sleep 24.59

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.67
pkill sipp

sleep 5.05

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.62
pkill chromium