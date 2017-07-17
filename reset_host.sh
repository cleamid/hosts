cd ~/Download
wget ftp://35.167.203.34/hosts -O ~/Downloads/hosts

echo 127.0.0.1 liveupdate.mac.sandai.net >> ~/Downloads/hosts

sudo cp ~/Downloads/hosts /etc/hosts
sudo killall -HUP mDNSResponder
rm ~/Downloads/hosts
