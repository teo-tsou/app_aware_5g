
sleep 24.89

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.3
pkill sipp

sleep 5.99

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 51.78
pkill chromium
