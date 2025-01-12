if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Hydra-sjz/My-Music-x-FilterBot.git /My-Music-x-FilterBot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /My-Music-x-FilterBot
fi
cd /shobanafilterbot
pip3 install -U -r requirements.txt
echo "🎵 music Filter-𝕏-Bot Starting...."
python3 bot.py
