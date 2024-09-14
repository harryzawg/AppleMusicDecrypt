# AppleMusicDecrypt

Apple Music decryption tool, based
on [zhaarey/apple-music-alac-atmos-downloader](https://github.com/zhaarey/apple-music-alac-atmos-downloader)

**WARNING: This project is currently in an extremely early stage, and there are still a large number of undiscovered
bugs and unfinished features. USE IT WITH CAUTION.**

# Usage

In my version, modified by harryzawg, you can run main.exe with an argument so once it's connected, it immediately sends the argument through to it's CLI.
I've modified this cause I'm using it with my discord bot to download music, so it can run main.exe with it's link, for example you can run it like

```shell
(running in cmd, this will wait for it to connect, then once connected it runs the command download https://music.apple.com/tr/album/lone/627523021?i=627523279 without having to type anything while inside of the exe)
main.exe download https://music.apple.com/tr/album/lone/627523021?i=627523279
```
You can use this for any command, such as 

```shell
# Download song/album with default codec (in our case, ALAC)
download https://music.apple.com/jp/album/nameless-name-single/1688539265
# you can use DL for short
dl https://music.apple.com/jp/album/nameless-name-single/1688539265
# Download song/album with specified codec (you can do -c aac to download in aac, which is 256 kbps)
dl -c aac https://music.apple.com/jp/song/caribbean-blue/339592231
# if a file already exists, overwrite it with -f
dl -f https://music.apple.com/jp/song/caribbean-blue/339592231
# download every album from an specified artist
dl https://music.apple.com/jp/artist/%E3%83%88%E3%82%B2%E3%83%8A%E3%82%B7%E3%83%88%E3%82%B2%E3%82%A2%E3%83%AA/1688539273
# download every song from an specified artist
dl --include-participate-songs https://music.apple.com/jp/artist/%E3%83%88%E3%82%B2%E3%83%8A%E3%82%B7%E3%83%88%E3%82%B2%E3%82%A2%E3%83%AA/1688539273
# download every song from a playlist
dl https://music.apple.com/jp/playlist/bocchi-the-rock/pl.u-Ympg5s39LRqp
# download from a file with lines containing links in them
dlf urls.txt
# download song from specified m3u8 with default codec (alac)
m3u8 https://aod.itunes.apple.com/itunes-assets/HLSMusic116/v4/cb/f0/91/cbf09175-ce98-d133-1936-2e46b6992aa5/P631756252_lossless.m3u8
# View the audio quality information for a given song or album
quality https://music.apple.com/jp/album/nameless-name-single/1688539265
```

# Supported codecs

- `alac (stereo, 44100 16 bit, up to 192000 24 bit)`
- `ec3 (dolby atmos, ac3 or ec3)`
- `ac3 (dolby atmos, ac3)`
- `aac (stereo, 256 kbps 44100)`
- `aac-binaural (audio-stereo-binaural)`
- `aac-downmix (audio-stereo-downmix)`

# Supported links

- Shared link from apple music (https://music.apple.com/jp/album/%E5%90%8D%E3%82%82%E3%81%AA%E3%81%8D%E4%BD%95%E3%82%82%E3%81%8B%E3%82%82/1688539265?i=1688539274)
- Album link (https://music.apple.com/jp/album/nameless-name-single/1688539265)
- Song link (https://music.apple.com/jp/song/caribbean-blue/339592231)
- Artist link (https://music.apple.com/jp/artist/%E3%82%A8%E3%83%B3%E3%83%A4/160847)
- Playlist link (https://music.apple.com/jp/playlist/bocchi-the-rock/pl.u-Ympg5s39LRqp)

# Deploy

## Prepare Local Environment

1. Install [GPAC](https://gpac.io/downloads/gpac-nightly-builds/), [FFmpeg](https://ffmpeg.org/download.html) and [Android Debug Bridge](https://developer.android.com/tools/adb)
2. Download [Bento4 MP4Tools](https://www.bento4.com/downloads/) and add the executable files to the environment
   variables
3. Run `gpac -version`, `mp4box -version`, `mp4extract`, `mp4edit` and make sure all the commands run fine

## Prepare Android Environment

1. Install Apple Music (3.6.0-beta) and login
2. Play a song in Apple Music
3. Manually install Frida and start frida-server in background
4. Edit `config.toml`

```toml
[[devices]]
host = "127.0.0.1"
port = 5555
agentPort = 10020
suMethod = "su 0"
```
