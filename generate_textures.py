#!/usr/bin/env python3
"""MEKAPLUS MOD 텍스처 생성기 - PIL 사용"""

from PIL import Image, ImageDraw
import os

# 텍스처 경로
BASE_PATH = "/home/yuchan/ai-wsp/yeonseo/MEKAPLUS/src/main/resources/assets/mekaplus/textures"

def create_starlight():
    """Starlight - 별빛 느낌의 황금빛 주괴"""
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 주괴 기본 형태 (밝은 금색)
    draw.polygon([(3, 4), (13, 4), (13, 12), (3, 12)], fill=(255, 248, 180))
    # 하이라이트 (흰색)
    draw.line([(4, 5), (12, 5)], fill=(255, 255, 255), width=1)
    # 그림자 (어두운 금색)
    draw.line([(4, 11), (12, 11)], fill=(200, 180, 100), width=1)
    # 별빛 반짝임 (작은 점들)
    draw.point((6, 7), fill=(255, 255, 255))
    draw.point((10, 8), fill=(255, 255, 255))
    draw.point((8, 6), fill=(255, 255, 255))
    
    return img

def create_soul_head():
    """Soul Head - 영혼이 깃든 위더 머리"""
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 위더 머리 기본 (어두운 회색)
    draw.ellipse([2, 2, 14, 14], fill=(40, 40, 45))
    # 영혼 파란색 글로우
    draw.ellipse([4, 4, 12, 12], fill=(60, 80, 120))
    # 눈 (빨간색)
    draw.ellipse([5, 6, 7, 8], fill=(255, 50, 50))
    draw.ellipse([9, 6, 11, 8], fill=(255, 50, 50))
    # 영혼 입 (파란색)
    draw.rectangle([6, 10, 10, 11], fill=(100, 150, 255))
    # 영혼 기운 (외곽선)
    draw.ellipse([2, 2, 14, 14], outline=(100, 150, 255), width=1)
    
    return img

def create_antigear():
    """Antigear - 안티기어 톱니바퀴"""
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 중심 원 (어두운 회색)
    draw.ellipse([4, 4, 12, 12], fill=(60, 60, 70))
    # 톱니 (빨간색 테두리)
    for i in range(8):
        import math
        angle = i * math.pi / 4
        x = 8 + int(5 * math.cos(angle))
        y = 8 + int(5 * math.sin(angle))
        draw.ellipse([x-1, y-1, x+1, y+1], fill=(180, 50, 50))
    # 중심 구멍
    draw.ellipse([6, 6, 10, 10], fill=(30, 30, 35))
    # 하이라이트
    draw.point((7, 7), fill=(100, 100, 110))
    
    return img

def create_vibranium():
    """Vibranium - 비브라늄 보라색 주괴"""
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 주괴 기본 (밝은 보라색)
    draw.polygon([(3, 4), (13, 4), (13, 12), (3, 12)], fill=(160, 80, 200))
    # 하이라이트 (밝은 보라색)
    draw.line([(4, 5), (12, 5)], fill=(200, 120, 255), width=1)
    # 그림자 (어두운 보라색)
    draw.line([(4, 11), (12, 11)], fill=(100, 40, 140), width=1)
    # 에너지 결정 느낌 (하얀 점들)
    draw.point((6, 7), fill=(255, 200, 255))
    draw.point((10, 8), fill=(255, 200, 255))
    draw.point((8, 9), fill=(255, 255, 255))
    
    return img

def create_speed_module():
    """Speed Module 128x - 초록색/파란색 속도 모듈"""
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 모듈 배경 (파란색)
    draw.rectangle([2, 2, 14, 14], fill=(40, 80, 140))
    # 테두리
    draw.rectangle([2, 2, 14, 14], outline=(60, 100, 160), width=1)
    # 속도 화살표 (초록색)
    draw.polygon([(4, 8), (10, 5), (10, 11)], fill=(80, 255, 120))
    # 화살표 끝
    draw.polygon([(10, 8), (13, 8), (10, 5)], fill=(120, 255, 160))
    draw.polygon([(10, 8), (13, 8), (10, 11)], fill=(120, 255, 160))
    # 128x 텍스트 대신 빛나는 점
    draw.point((5, 12), fill=(255, 255, 150))
    
    return img

def create_damage_module():
    """Damage Module - 빨간색 데미지 모듈"""
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 모듈 배경 (빨간색)
    draw.rectangle([2, 2, 14, 14], fill=(140, 40, 40))
    # 테두리
    draw.rectangle([2, 2, 14, 14], outline=(180, 60, 60), width=1)
    # 칼날 느낌 (밝은 빨간색)
    draw.line([(4, 4), (12, 12)], fill=(255, 100, 100), width=2)
    draw.line([(12, 4), (4, 12)], fill=(255, 100, 100), width=2)
    # 중심 강조
    draw.ellipse([6, 6, 10, 10], fill=(255, 150, 150))
    # 하이라이트
    draw.point((7, 7), fill=(255, 255, 200))
    
    return img

def create_antimatter_synthesizer():
    """Antimatter Synthesizer - 반물질 합성기 블록"""
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 블록 기본 (어두운 청록색)
    draw.rectangle([0, 0, 15, 15], fill=(30, 50, 60))
    # 테두리 (밝은 청록색)
    draw.rectangle([0, 0, 15, 15], outline=(50, 80, 100), width=1)
    # 중심 코어 (보라색/파란색 글로우)
    draw.ellipse([4, 4, 12, 12], fill=(60, 40, 100))
    draw.ellipse([5, 5, 11, 11], fill=(100, 60, 160))
    draw.ellipse([6, 6, 10, 10], fill=(150, 100, 220))
    # 에너지 라인
    draw.line([(2, 2), (4, 4)], fill=(100, 150, 200), width=1)
    draw.line([(14, 2), (12, 4)], fill=(100, 150, 200), width=1)
    draw.line([(2, 14), (4, 12)], fill=(100, 150, 200), width=1)
    draw.line([(14, 14), (12, 12)], fill=(100, 150, 200), width=1)
    # 코어 하이라이트
    draw.point((8, 7), fill=(255, 255, 255))
    
    return img

def main():
    # 디렉토리 생성
    os.makedirs(f"{BASE_PATH}/item", exist_ok=True)
    os.makedirs(f"{BASE_PATH}/block", exist_ok=True)
    
    # 텍스처 생성 및 저장
    textures = {
        "item/starlight": create_starlight(),
        "item/soul_head": create_soul_head(),
        "item/antigear": create_antigear(),
        "item/vibranium": create_vibranium(),
        "item/speed_module_128x": create_speed_module(),
        "item/damage_module": create_damage_module(),
        "block/antimatter_synthesizer": create_antimatter_synthesizer(),
    }
    
    for name, img in textures.items():
        path = f"{BASE_PATH}/{name}.png"
        img.save(path)
        print(f"✓ Created: {path}")

if __name__ == "__main__":
    main()
