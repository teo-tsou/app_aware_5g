
sleep 25.89

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.25
pkill sipp

sleep 5.58

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 52.2
pkill chromium
