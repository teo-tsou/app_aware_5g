
sleep 25.47

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.43
pkill sipp

sleep 5.09

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 52.09
pkill chromium
