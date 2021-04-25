# Pocket Player

Pocket Player is Video Player for Raspberry Pi with an Webinterface \
It scans all the videos in the ./data folder an displays it in a webinterface \
The videos will be played looped via the [OMXPlayer](https://www.raspberrypi.org/documentation/raspbian/applications/omxplayer.md)


## Installation
```git
git clone 
```

## Required Libraries
+ Python 3.xx
+ Flask
```bash
pip3 install flask
```

## Usage

1. copy the video files to ./data
2. start the webserver  

```python
python3 webserver.py
```
## Supported Formats
...are support \
<b> please note, that audio via hdmi is enabled </b>

## License
