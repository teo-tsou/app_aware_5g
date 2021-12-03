
sleep 25.52

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.85
pkill sipp

sleep 4.38

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 52.17
pkill chromium
