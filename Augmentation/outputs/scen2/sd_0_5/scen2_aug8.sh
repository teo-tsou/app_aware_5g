
sleep 24.89

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.19
pkill sipp

sleep 4.63

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 52.58
pkill chromium
