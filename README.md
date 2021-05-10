# TensorFlow Object Detection Security Camera

## _Object detection security camera that sends you a message and image using telegram when it detects an object in frame._


<p align="center">
   <img src="/doc/Animated GIF-source.gif">
</p>



## Installation:

Update & Upgrade  

```sh
sudo apt-get update
sudo apt-get dist-upgrade
```

git clone this repository and create virtual environment

```sh
https://github.com/partylikeits1983/TensorFlow-Object-Detection-Security-Camera-Telegram-Bot.git
```

Rename folder to something shorter

```sh
mv TensorFlow-Object-Detection-Security-Camera-Telegram-Bot tfsecuritycam
cd tfsecuritycam
```

Download virtual env

```sh
sudo pip3 install virtualenv
```

Create env
```sh
python3 -m venv tfsecuritycam
```

Activate env
```sh
source tfsecuritycam/bin/activate
```

Get requirements for env
```sh
bash requirements.sh
```
_This may take a while so go make yourself a cup of coffee._


Make ./tfsecuritycam executable:
```sh
sudo chmod +x ./tfsecuritycam.sh
```

Download pretrained model
```sh
wget https://storage.googleapis.com/download.tensorflow.org/models/tflite/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip
```

Rename and save model to folder
```sh
unzip coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip -d Sample_TFLite_model
```

Create Telegram bot & get your chat_id:

1. Get telegram bot API key using [BotFather](https://t.me/botfather)
2. Get your telegram Chat_ID using [UserInfoBot](https://github.com/nadam/userinfobot)


Create config.json file

<p align="center">
   <img src="/doc/pi.gif">
</p>

```sh
python3 config.py
```

Run the security camera bash script
```sh
python3 ./tfsecuritycam
```

Or run the telegram bot and object detection script separately:
```sh
python3 main.py
python3 telegram-main.py
```
