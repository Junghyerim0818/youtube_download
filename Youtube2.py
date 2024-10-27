import streamlit as st
from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
import time

st.title('유튜브 영상 추출기')
url = st.text_input('유튜브 URL을 입력하세요.')

resoulution = ['360p', '720p', '1080p', '1440p', '2160p']
selected_res = st.selectbox('화질을 선택하세요.', resoulution)

def video_download(url):

    yt = YouTube(url, on_progress_callback = on_progress)

    for idx,i in enumerate(yt.streams):
        if i.resolution == selected_res:
            print(i.resolution)
            break
    
    print(yt.streams[idx])
    video_file = yt.streams[idx].download()

    return video_file

def audio_download(audio) :

    yt = YouTube(url, on_progress_callback = on_progress)

    audio = yt.streams.filter(only_audio = True).get_audio_only('webm')
    audio_file = audio.download()

    return audio_file

if st.button('다운로드'):
    if url:
        try:
            video_file = video_download(url)
            audio_file = audio_download(url)
            yt = YouTube(url, on_progress_callback = on_progress)
            st.success(f'[{yt.title}] 영상을 다운로드를 완료했습니다!')

        except AttributeError as e :
            st.error(f'다운로드 가능한 파일이 없습니다.')

        except Exception as e :
            st.error(f'예외 발생: {e}')