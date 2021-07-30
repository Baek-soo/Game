import os #파일 디렉터리를 다루기 위함
import pygame

#보석 클래스
class Gemstone(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center = position)


#기본 설정
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height)) #화면 사이즈 지정
pygame.display.set_caption("Gold Miner") #타이틀 이름설정

clock = pygame.time.Clock()#프레임을 제한히기 위함

#배경 이미비 불러오기
current_path = os.path.dirname(__file__) #현재 파일의 위치 반환
background = pygame.image.load(os.path.join(current_path, "background.png")) # 디렉터리와 디렉터리(파일명) 결합

# 4개 보석 이미지 불러오기 (작은 금, 큰 금, 돌, 다이아몬드)
gemstone_images = [
    pygame.image.load(os.path.join(current_path, "small_gold.png")), #작은 금
    pygame.image.load(os.path.join(current_path, "big_gold.png")), #큰 금
    pygame.image.load(os.path.join(current_path, "stone.png")), #돌
    pygame.image.load(os.path.join(current_path, "diamond.png")) #다이아몬드
]

running = True
while running:
    clock.tick(30) #FPS 값이 30으로 고정

    for event in pygame.event.get(): #마우스, 키보드 입력값을 받는다.
        if event.type == pygame.QUIT: #event의 type이 '창닫기'를 눌렀담면
            running = False #running event를 false로 바꿔준다.

    screen.blit(background, (0,0))
    pygame.display.update() #display 업데이트

pygame.quit()