
sleep 24.89

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.11
pkill sipp

sleep 4.26

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.29
pkill chromium