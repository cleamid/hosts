echo 127.0.0.1 liveupdate.mac.sandai.net >> ~/Downloads/hosts
sudo cp ~/Downloads/hosts /etc/hosts
killall -HUP mDNSResponder
