import random
import time
#엄마몬스터 클래스: 기본값들 설정 .. 예를 들어  hp, 공격 받는 거, healing들..
#악당 몬스터, 불몬스터, 물몬스터
#기술스택) 일반공격, 마법공격(필살기), 치유스킬

#착한몬스터 공통 속성
class Monster():
    alive = True
    hp = 100

    def __init__(self, name):
        self.name = name
        self.max_hp = self.hp

    #일반스킬
    def attack(self,other):
        damage = random.randint(self.power-5,self.power+1)
        other.hp = max(other.hp - damage, 0)
        heal = random.randint(1,5)
        self.hp += heal
        if damage < self.power-3:
            print(f'{self.name}의 공격 miss!! {other.name}에게 {damage}의 데미지를 입혔습니다. {self.name}은 {heal}의 hp를 회복했습니다.')
        else:
            print(f'{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다. {self.name}은 {heal}의 hp를 회복했습니다.')

    #마법스킬
    def special_attack(self,other):
        damage = random.randint(self.power,self.power+5)
        other.hp = max(other.hp - damage, 0)
        if damage < self.power+2:
            print(f'{self.name}의 공격 miss!! {other.name}에게 {damage}의 데미지를 입혔습니다.')
        else:
            print(f'{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.')

    #치유스킬
    def healing(self):
        plus = random.randint(self.heal-2,self.heal+5)
        self.hp += plus
        print(f'치유스킬 발동. {plus}만큼 hp 회복')

    #상태체크
    def status_check(self, other):
        if self.hp > 0 and other.hp >0:
            print(f'{self.name} hp : {self.hp}/{self.max_hp}   {other.name} hp : {other.hp}/{other.max_hp}')
        elif self.hp >0 and other.hp <=0:
            print(f'{self.name}이 승리하였습니다! 모험을 계속 하세요!!')
            other.alive = False
        else:
            print(f'{self.name}이 쓰러졌습니다. 몬스터가 없으면 모험을 할 수 없습니다. 다시 돌아가 모험을 떠날 준비를 하세요.')
            self.alive = False

#나쁜 몬스터 속성
class EvilMonster(Monster):
    hp = random.randint(120, 150) #악당 hp는 랜덤하게!
    power = 12
    name = '드래곤'
    def __init__(self):
        self.max_hp = self.hp

    def attack(self, other):
        damage = random.randint(self.power - 5, self.power + 3)
        other.hp = max(other.hp - damage, 0)
        if damage < self.power:
            print(f'{self.name}의 공격 miss!! {other.name}에게 {damage}의 데미지를 입혔습니다.')
        else:
            print(f'{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.')

#착한 몬스터 1: 파워: 강, 회복력: 보통 , hp: 보통
class FireMonster(Monster):
    power = 12
    heal = 10
    def __init__(self,name):
        self.attribute = "fire"
        self.name = name
        self.max_hp = self.hp

#착한 몬스터 2: 파워: 보통, 회복력: 강, hp: 보통
class WaterMonster(Monster):
    power = 10
    heal = 12
    def __init__(self,name):
        self.attribute = "water"
        self.name = name
        self.max_hp = self.hp

#전투
def test(fight, a, b):
    if fight == "1":
        a.attack(b)
        time.sleep(1)
        if b.hp>0:
            print(f'드래곤의 반격')
            b.attack(a)
            time.sleep(1)
        a.status_check(b)
        time.sleep(2)
    elif fight == "2":
        a.special_attack(b)
        time.sleep(1)
        if b.hp>0:
            print(f'드래곤의 반격')
            b.attack(a)
            time.sleep(1)
        a.status_check(b)
        time.sleep(2)
    elif fight == "3":
        a.healing()
        time.sleep(1)
        if b.hp>0:
            print(f'드래곤의 반격')
            b.attack(a)
            time.sleep(1)
        a.status_check(b)
        time.sleep(2)
    else:
        print("잘못 입력하셨습니다. 다시 입력하세요.")

#스토리라인
player = input("환영합니다. 당신의 이름은?").strip()
print(f"{player}님! 다시 한 번 환영합니다~ 이곳은 몬스터 세상! 당신의 몬스터를 고르세요.")
time.sleep(1)
print("물 속성 몬스터(1): power= 10, heal=12 / 불 속성 몬스터(2): power = 12, heal = 10")
time.sleep(1)
choice = input("당신의 선택은? 1 또는 2를 입력하세요.").strip()

#전투
if choice == "1":
    mname = input("당신의 몬스터의 이름을 지어주세요.")
    time.sleep(1)
    print(f'준비는 끝났습니다. {player}님과 {mname}, 모험을 떠나세요!')
    e = EvilMonster()
    w = WaterMonster(mname)
    print(f'앗.. 출발하자마자 드래곤을 발견!!! 드래곤이 {mname}을(를) 사냥하려고 한다!! 싸워서 당신의 몬스터를 지키세요. 드래곤 hp: {e.max_hp}')
    time.sleep(2)
    while(True):
        print('공격스킬 1: 물총쏘기(일반+약간의 hp 회복), 2 : 용오름(마법), 3: 족욕타임(hp회복)')
        fight = input(f'{player}님, 공격방식을 고르세요. (1/2/3)').strip()
        time.sleep(1)
        test(fight, w, e)
        if w.alive == False or e.alive == False:
            break
elif choice == "2":
    mname = input("당신의 몬스터의 이름을 지어주세요.")
    time.sleep(1)
    print(f'준비는 끝났습니다. {player}님과 {mname}, 모험을 떠나세요!')
    e = EvilMonster()
    f = FireMonster(mname)
    print(f'앗.. 출발하자마자 드래곤 발견!!! 드래곤이 {mname}을(를) 사냥하려고 한다!! 싸워서 당신의 몬스터를 지키세요. 드래곤 hp: {e.max_hp}')
    time.sleep(1)
    while (True):
        print('공격스킬 1: 촛불공격(일반+약간의 hp 회복), 2 : 폭탄던지기(마법), 3: 마시멜로우 구워먹기(hp회복)')
        fight = input(f'{player}님, 공격방식을 고르세요. (1/2/3)').strip()
        time.sleep(1)
        test(fight, f, e)
        if f.alive == False or e.alive == False:
            break
else:
    print("잘못 입력하셨습니다.")


