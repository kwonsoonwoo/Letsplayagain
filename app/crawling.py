import json
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
django.setup()
from toylibrary.models import Toylibrary


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
            Toylibrary.objects.create(
                name=toylibraries['lib_nm'],
                gu=toylibraries['addr_gu'],
                website=toylibraries['website'],
                address=toylibraries['addr'],
                address_road=toylibraries['addr_rd'],
                latitude=toylibraries['latitude'],
                longitude=toylibraries['longitude'],
            )


if __name__ == "__main__":
    toylibrary_parsing()
