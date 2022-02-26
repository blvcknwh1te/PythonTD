import pygame

pygame.mixer.pre_init(41000,16)
pygame.mixer.init()



noMoneySound=pygame.mixer.Sound('sounds/Nomoney.wav')
moneyFall=pygame.mixer.Sound('sounds/moneyFalling1.wav')


buildSound=pygame.mixer.Sound('sounds/money.wav')

lifeLost=pygame.mixer.Sound('sounds/minuslife1.wav')

###Tower Attack Sounds:
arrowSound=pygame.mixer.Sound('sounds/arrow_1.wav')
lightningSound=pygame.mixer.Sound('sounds/lightning.wav')
fireSound=pygame.mixer.Sound('sounds/fire1.wav')
shootSound=pygame.mixer.Sound('sounds/shoot.wav')
frostAttackSound=pygame.mixer.Sound('sounds/frostAttacked.wav')
frostCrushSound=pygame.mixer.Sound('sounds/windAttack.wav')

towerAttackSounds=[arrowSound,lightningSound,fireSound,shootSound,frostAttackSound]