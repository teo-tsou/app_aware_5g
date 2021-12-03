
sleep 24.86

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.08
pkill sipp

sleep 5.89

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.03
pkill chromium