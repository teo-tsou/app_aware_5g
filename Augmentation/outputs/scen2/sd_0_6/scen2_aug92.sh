
sleep 25.83

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.09
pkill sipp

sleep 4.89

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.56
pkill chromium