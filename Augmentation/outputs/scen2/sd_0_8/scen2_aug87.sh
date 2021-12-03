
sleep 26.05

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.0
pkill sipp

sleep 4.46

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.75
pkill chromium