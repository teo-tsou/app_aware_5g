
sleep 24.52

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.63
pkill sipp

sleep 5.26

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 51.68
pkill chromium
