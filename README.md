# CleanScript
AI Hub에서 제공되는 KsponSpeech Open Data 전처리를 진행하는 프로젝트

# Output 형태
- Nvidia Jasper Model 의 학습 데이터셋 format 형태
- Clova Call Model 의 학습 데이터셋 format 형태

# Libraries
- csv
- json
- os
- natsort

# Functions

### fileOI.get_divided_script
AI Hub에서 제공되는 KsponDataset과 같이 음원별 스크립트가 pair 로 제작되어있는 형태에서 text script의 filepath만 모두 가져와서 리스트에 담는 함수
natsort 라이브러리를 통해 해당 파일들을 오름차순으로 정렬
- input_dir : 어떤 디렉토리에서 파일들을 찾을것인지에 대한 상위 디렉토리 경로
- file_extension : 어떤 확장자를 가진 파일을 리스트화 시킬것인지에 대한 확장자 (default : txt)

### script_preprocess.merge_script_like_clova_call
Github Open Source 중 clovaai의 ClocaCall model의 학습데이터셋에 맞는 형태로 제작하기 위한 함수

```
ClovaCall.json

[
  {
    "wav" : "42_0603_748_0_03319_00.wav",
    "text : "단체 할인이 가능한 시간대가 따로 있나요?",
    "speaker_id" : "03319"
  },
  ...,
  {
    "wav" : "42_0610_778_0_03607_01.wav",
    "text" : "애기들이 놀만한 놀이방이 따로 있나요?",
    "speaker_id" : "03607"
  }
]  
```
