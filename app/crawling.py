import json
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
django.setup()
from toylibrary.models import Toylibrary
from kidscafe.models import Kidscafe


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
                website=toylibraries['website'],
                address=toylibraries['addr'],
                address_road=toylibraries['addr_rd'],
                latitude=toylibraries['latitude'],
                longitude=toylibraries['longitude'],
            )


def kidscafe_parsing():
    file_path = 'data/kidscafe.json'
    kidscafe_json = open(file_path, 'rt').read()
    kidscafe_data = json.loads(kidscafe_json)
    for kidscafe_list in kidscafe_data.get('DATA'):
        # 만약 json 파일의 'tel' value가 null이면 스킵
        if not kidscafe_list.get('tel'):
            continue
        # Kidscafe 객체 생성
        # update_or_create는 기존에 생성한 파일이 있을 경우 추가되는것만 업데이트한다
        Kidscafe.objects.update_or_create(
            name=kidscafe_list['nm'],
            address=kidscafe_list['addr_old'],
            address_road=kidscafe_list['addr'],
            tell=kidscafe_list['tel'],
            longitude=kidscafe_list['xcode'],
            latitude=kidscafe_list['ycode'],
            check_date=kidscafe_list['check_date'],
        )


if __name__ == "__main__":
    kidscafe_parsing()
