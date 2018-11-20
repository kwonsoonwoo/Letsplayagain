import json
import os

import django
import pyproj

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
django.setup()

import requests

from config.settings.base import secrets

# 모델들이 아래에 있어야 장고에서 불러올수 있음
from toylibrary.models import Toylibrary
from kidscafe.models import Kidscafe
from culture.models import Culture
from park.models import Park

# kidscafe xcode, ycode를 latitude, longitude로 변환하기 위한 pyproj 모듈 인자 설정
# 한국의 경우 WGS84 경위도를 기준으로 EPSG:4326, EPSG:4166을 사용
p = pyproj.Proj(init='epsg:5181')
outProj = pyproj.Proj("+proj=longlat +ellps=GRS80 +no_defs")


# 장난감 도서관 json데이터 파싱
def toylibrary_parsing():
    # json 파일 경로 설정
    file_path = 'data/toylibrary.json'
    # json 파일 읽어오기
    toylibrary_json = open(file_path, 'rt').read()
    # json 파일 불러오기
    toylibrary_data = json.loads(toylibrary_json)
    # toylibraries 변수에 toylibrary_data의 'DATA' 키 값만 순회
    for toylibraries in toylibrary_data['DATA']:
        # 만약 toylibraries의 'addr_rd'에 '미운영'이라는 string이 없으면
        # Toylibrary 객체 생성 및 데이터베이스에 저장
        # 있으면 객체를 만들지 않는다.
        if '미운영' not in toylibraries['addr_rd']:
            pass
            # Toylibrary 객체 생성
            # update_or_create는 기존에 생성한 파일이 있을 경우 추가되는것만 업데이트한다
            Toylibrary.objects.update_or_create(
                name=toylibraries['lib_nm'],
                gu=toylibraries['addr_gu'],
                tell=toylibraries['tel'],
                website=toylibraries['website'],
                address=toylibraries['addr'],
                address_road=toylibraries['addr_rd'],
                latitude=toylibraries['latitude'],
                longitude=toylibraries['longitude'],
            )


# 키즈카페 json데이터 파싱
def kidscafe_parsing():
    # json 파일 경로 설정
    file_path = 'data/kidscafe.json'
    # json 파일 읽어오기
    kidscafe_json = open(file_path, 'rt').read()
    # json 파일 불러오기
    kidscafe_data = json.loads(kidscafe_json)
    # kidscafe_list 변수에 kidscafe_data의 'DATA' 키 값만 순회
    for kidscafe_list in kidscafe_data.get('DATA'):
        # 만약 json 파일의 'tel' value가 null이면 스킵
        if not kidscafe_list.get('tel'):
            continue
        # 다른 app의 위치정보와는 달리 키즈카페는 xcode, ycode로 되어 있기 때문에 위도,경도 변환이 필요함
        # pyproj 패키지의 transform 메서드를 사용하여 xcode와, ycode를 x와 y변수에 할당
        # 통상적으로 Longitude(경도)=X, Latitude(위도)=Y 로 정의되어 있음
        # 서울데이터광장의 경우에도 ycode=위도, xcode=경도라고 표기.
        x, y = pyproj.transform(p, outProj, kidscafe_list['xcode'], kidscafe_list['ycode'])
        # Kidscafe 객체 생성
        # update_or_create는 기존에 생성한 파일이 있을 경우 추가되는것만 업데이트한다
        Kidscafe.objects.update_or_create(
            name=kidscafe_list['nm'],
            address=kidscafe_list['addr_old'],
            address_road=kidscafe_list['addr'],
            tell=kidscafe_list['tel'],
            latitude=y,
            longitude=x,
            check_date=kidscafe_list['check_date'],
        )


# 서울시 공원 openAPI 데이터 크롤링해서 데이터 베이스에 저장
def park_crawling():
    # 서울시에서 발행받은 인증키 설정(개인 인증키이기 때문에 secrets폴더에 저장)
    client_key = secrets['CULTURE_API_CLIENT_KEY']
    # 파일 형식(xml과 json중 json선택)
    file_format = 'json'
    # service 명
    service = 'SearchParkInfoService'

    # url변수에 위에 설정해놨던 변수들을 넣어 크롤링 할 주소 완성
    url = f'http://openapi.seoul.go.kr:8088/{client_key}/{file_format}/{service}/1/132/'
    # request로 url에 get요청을 보낸다
    response = requests.get(url)
    # 별도의 json.loads() 라이브러리 메서드를 사용하지 않아도,
    #  requests 라이브러리에 있는 json() 메서드로 간단히 처리 가능
    data = response.json()

    # data의 SearchParkInfoService의 row 키를 순회
    for park in data['SearchParkInfoService']['row']:
        Park.objects.update_or_create(
            name=park['P_PARK'],
            overview=park['P_LIST_CONTENT'],
            use_note=park['USE_REFER'],
            region=park['P_ZONE'],
            address=park['P_ADDR'],
            tell=park['P_ADMINTEL'],
            latitude=park['LATITUDE'],
            longitude=park['LONGITUDE'],
            website=park['TEMPLATE_URL'],
        )


# 서울시 문화행사 openAPI 데이터 크롤링해서 데이터 베이스에 저장
def culture_crawling():
    # 서울시에서 발행받은 인증키 설정(개인 인증키이기 때문에 secrets폴더에 저장)
    client_key = secrets['CULTURE_API_CLIENT_KEY']
    # 파일 형식(xml과 json중 json선택)
    file_format = 'json'
    # service 명
    service = 'SearchConcertDetailService'

    # url변수에 위에 설정해놨던 변수들을 넣어 크롤링 할 주소 완성
    url = f'http://openapi.seoul.go.kr:8088/{client_key}/{file_format}/{service}/1/474/'
    # request로 url에 get요청을 보낸다
    response = requests.get(url)
    # 별도의 json.loads() 라이브러리 메서드를 사용하지 않아도,
    #  requests 라이브러리에 있는 json() 메서드로 간단히 처리 가능
    culture_data = response.json()

    # data의 SearchConcertDetailService의 row 키를 순회
    for culture_event in culture_data['SearchConcertDetailService']['row']:
        # 만약 USE_TRGT 키 값에 유아 혹은 영아라는 키워드가 들어가 있다면 객체 생성
        if '유아' in culture_event['USE_TRGT'] or '영아' in culture_event['USE_TRGT']:
            Culture.objects.update_or_create(
                gu=culture_event['GCODE'],
                place=culture_event['PLACE'],
                start_date=culture_event['STRTDATE'],
                end_date=culture_event['END_DATE'],
                time=culture_event['TIME'],
                homepage=culture_event['ORG_LINK'],
                target_user=culture_event['USE_TRGT'],
                fee=culture_event['USE_FEE'],
                inquiry=culture_event['INQUIRY'],
            )


if __name__ == "__main__":
    toylibrary_parsing()
    kidscafe_parsing()
    park_crawling()
    culture_crawling()
