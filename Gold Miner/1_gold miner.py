import os #파일 디렉터리를 다루기 위함
import pygame


#집게 클래스
class Claw(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center = position)

        self.offset = pygame.math.Vector2(default_offset_x_claw, 0)
        self.position = position

    def update(self):
        rect_center = self.position + self.offset
        self.rect = self.image.get_rect(center = rect_center)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.line(screen, BLACK, self.position, self.rect.center, 5) #직선 그리기

#보석 클래스
class Gemstone(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center = position)

def setup_gemstone():
    #작은 금
    small_gold = Gemstone(gemstone_images[0], (200, 380)) # 0번째 이미지를 (200, 300) 위치에
    gemstone_group.add(small_gold)#그룹에 추가
    #큰 금
    gemstone_group.add(Gemstone(gemstone_images[1], (300, 500)))
    #돌
    gemstone_group.add(Gemstone(gemstone_images[2], (300, 380)))
    #다이아몬드
    gemstone_group.add(Gemstone(gemstone_images[3], (900, 420)))


#기본 설정
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height)) #화면 사이즈 지정
pygame.display.set_caption("Gold Miner") #타이틀 이름설정

clock = pygame.time.Clock()#프레임을 제한히기 위함

#게임 관련 변수
default_offset_x_claw = 40 #집게와 중심점 사이의 거리

#색깔 변수
RED = (255, 0, 0)
BLACK = (0, 0, 0)

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

#보석 그룹
gemstone_group = pygame.sprite.Group()
setup_gemstone() #게임에 원하는 만큼의 보석을 정의

#집게 
claw_image = pygame.image.load(os.path.join(current_path, "claw.png"))
claw = Claw(claw_image, (screen_width//2, 110)) #가로위치는 화면 크기 기준으로 절반, 세로 위치는 위에서 110 px

running = True
while running:
    clock.tick(30) #FPS 값이 30으로 고정

    for event in pygame.event.get(): #마우스, 키보드 입력값을 받는다.
        if event.type == pygame.QUIT: #event의 type이 '창닫기'를 눌렀담면
            running = False #running event를 false로 바꿔준다.

    screen.blit(background, (0,0))

    gemstone_group.draw(screen) #그룹 내 모든 스프라이트를 screen에 표시
    claw.update()
    claw.draw(screen)

    pygame.display.update() #display 업데이트

pygame.quit()