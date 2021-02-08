import pygame


######MOBS:
#Fly
flyWalk=(pygame.image.load(('images/Mobs/Fly/fly.png')),
         pygame.image.load(('images/Mobs/Fly/fly1.png')))

flyBigWalk=(pygame.image.load(('images/Mobs/Fly/fly_big.png')),
         pygame.image.load(('images/Mobs/Fly/fly_big_2.png')))

batWalk=(pygame.image.load(('images/Mobs/bat/bat1.png')),
         pygame.image.load(('images/Mobs/bat/bat2.png')),
         pygame.image.load(('images/Mobs/bat/bat3.png')),
         pygame.image.load(('images/Mobs/bat/bat4.png')))

batRedWalk=(pygame.image.load(('images/Mobs/bat/bat_red_1.png')),
         pygame.image.load(('images/Mobs/bat/bat_red_2.png')),
         pygame.image.load(('images/Mobs/bat/bat_red_3.png')),
         pygame.image.load(('images/Mobs/bat/bat_red_4.png')))

spiderWalk=(

    #SPIDER DOWN
    (pygame.image.load(('images/Mobs/spider/spider_down_1.png')),
            pygame.image.load(('images/Mobs/spider/spider_down_2.png')),
            pygame.image.load(('images/Mobs/spider/spider_down_3.png')),
            pygame.image.load(('images/Mobs/spider/spider_down_4.png'))),
     #SPIDER UP
    (pygame.image.load(('images/Mobs/spider/spider_up_1.png')),
            pygame.image.load(('images/Mobs/spider/spider_up_2.png')),
            pygame.image.load(('images/Mobs/spider/spider_up_3.png')),
            pygame.image.load(('images/Mobs/spider/spider_up_4.png')))
    ,
    #SPIDER LEFT
    (pygame.image.load(('images/Mobs/spider/spider_left_1.png')),
            pygame.image.load(('images/Mobs/spider/spider_left_2.png')),
            pygame.image.load(('images/Mobs/spider/spider_left_3.png')),
            pygame.image.load(('images/Mobs/spider/spider_left_4.png'))),
    #SPIDER RIGHT
    (pygame.image.load(('images/Mobs/spider/spider_right_1.png')),
            pygame.image.load(('images/Mobs/spider/spider_right_2.png')),
            pygame.image.load(('images/Mobs/spider/spider_right_3.png')),
            pygame.image.load(('images/Mobs/spider/spider_right_4.png')))

     )

spiderGreenWalk=(

    #SPIDER DOWN
    (pygame.image.load(('images/Mobs/spider/spider_green_down_1.png')),
            pygame.image.load(('images/Mobs/spider/spider_green_down_2.png')),
            pygame.image.load(('images/Mobs/spider/spider_green_down_3.png')),
            pygame.image.load(('images/Mobs/spider/spider_green_down_4.png'))),
     #SPIDER UP
    (pygame.image.load(('images/Mobs/spider/spider_green_up_1.png')),
            pygame.image.load(('images/Mobs/spider/spider_green_up_2.png')),
            pygame.image.load(('images/Mobs/spider/spider_green_up_3.png')),
            pygame.image.load(('images/Mobs/spider/spider_green_up_4.png')))
    ,
    #SPIDER LEFT
    (pygame.image.load(('images/Mobs/spider/spider_green_left_1.png')),
            pygame.image.load(('images/Mobs/spider/spider_green_left_2.png')),
            pygame.image.load(('images/Mobs/spider/spider_green_left_3.png')),
            pygame.image.load(('images/Mobs/spider/spider_green_left_4.png'))),
    #SPIDER RIGHT
    (pygame.image.load(('images/Mobs/spider/spider_green_right_1.png')),
            pygame.image.load(('images/Mobs/spider/spider_green_right_2.png')),
            pygame.image.load(('images/Mobs/spider/spider_green_right_3.png')),
            pygame.image.load(('images/Mobs/spider/spider_green_right_4.png')))

     )


#####################################

#HUD Icons:
iconHeart=pygame.image.load(('images/icons/heart.png'))
iconCoin=pygame.image.load(('images/icons/coin.png'))


#Tower Icons:
iconArcher=pygame.image.load(('images/icons/archer_1.png'))
iconLightning=pygame.image.load(('images/icons/lightning1.png'))
iconFireMage=pygame.image.load(('images/icons/tower_of_fire.png'))
iconMinigun=pygame.image.load(('images/icons/minigun1.png'))
iconFrostTower=pygame.image.load(('images/icons/frostTower2.png'))

towerIcons=(iconArcher,iconLightning,iconFrostTower,iconMinigun)

#Buttons
button_pressed=pygame.image.load(('images/icons/button_pressed.png'))

##TowerImages
towerImages=(
    ###ARCHER
(pygame.image.load(('images/towers/tower_archer.png')),#
pygame.image.load(('images/towers/tower_archer_1.png')),
pygame.image.load(('images/towers/tower_archer_2.png')),
pygame.image.load(('images/towers/tower_archer_3.png')),
pygame.image.load(('images/towers/tower_archer_4.png')),
pygame.image.load(('images/towers/tower_archer_5.png')),
pygame.image.load(('images/towers/tower_archer_6.png')),
pygame.image.load(('images/towers/tower_archer_7.png')),
pygame.image.load(('images/towers/tower_archer_8.png'))),
    #####LIGHTNING
    (pygame.image.load(('images/towers/lightning_tower1.png')),
     pygame.image.load(('images/towers/lightning_tower2.png')),
     pygame.image.load(('images/towers/lightning_tower3.png')),
     pygame.image.load(('images/towers/lightning_tower4.png')),
     pygame.image.load(('images/towers/lightning_tower5.png')),
     pygame.image.load(('images/towers/lightning_tower6.png')),
     pygame.image.load(('images/towers/lightning_tower7.png')),
     pygame.image.load(('images/towers/lightning_tower8.png'))),
    #######FROST TOWER
(pygame.image.load(('images/towers/frostTower.png')),
 pygame.image.load(('images/towers/frostTower_1.png')),
 pygame.image.load(('images/towers/frostTower_2.png')),
 pygame.image.load(('images/towers/frostTower_3.png')),
 pygame.image.load(('images/towers/frostTower_4.png')),
 pygame.image.load(('images/towers/frostTower_5.png')),
 pygame.image.load(('images/towers/frostTower_6.png')),
 pygame.image.load(('images/towers/frostTower_7.png')),
 pygame.image.load(('images/towers/frostTower_8.png'))

 ),
    ######MINIGUN TOWER
    (pygame.image.load(('images/towers/minigun_bunker_neutral.png')))
    #####FROST TOWER



)

minigun_Shoot=(
    (pygame.image.load(('images/towers/minigun_bunker1_1.png')),#1 четверть
     pygame.image.load(('images/towers/minigun_bunker1_2.png')),
     pygame.image.load(('images/towers/minigun_bunker1_3.png'))),

(pygame.image.load(('images/towers/minigun_bunker2_1.png')),#2 четверть
     pygame.image.load(('images/towers/minigun_bunker2_2.png')),
     pygame.image.load(('images/towers/minigun_bunker2_3.png'))),

(pygame.image.load(('images/towers/minigun_bunker3_1.png')),#3 четверть
     pygame.image.load(('images/towers/minigun_bunker3_2.png')),
     pygame.image.load(('images/towers/minigun_bunker3_3.png'))),

(pygame.image.load(('images/towers/minigun_bunker4_1.png')),#4 четверть
     pygame.image.load(('images/towers/minigun_bunker4_2.png')),
     pygame.image.load(('images/towers/minigun_bunker4_3.png')))

)
###Bullets:

#arrowBullet=pygame.image.load(('images/Towers/arrow1.png'))

shurikenBullet=(pygame.image.load(('images/Bullets/Shuriken1_1.png')),
                pygame.image.load(('images/Bullets/Shuriken2_1.png')),
                pygame.image.load(('images/Bullets/Shuriken3_1.png')))

frostBullet=(pygame.image.load(('images/Bullets/ice_sphere_1.png')),
                pygame.image.load(('images/Bullets/ice_sphere_2.png')),
                pygame.image.load(('images/Bullets/ice_sphere_3.png')),
             pygame.image.load(('images/Bullets/ice_sphere_4.png')),
             pygame.image.load(('images/Bullets/ice_sphere_5.png')),
             pygame.image.load(('images/Bullets/ice_sphere_6.png')),
            pygame.image.load(('images/Bullets/ice_sphere_7.png'))
             )


allBullets=(shurikenBullet,frostBullet)


#SpecEffects:

damageEffect=(
pygame.image.load(('images/effects/damage1.png')),
pygame.image.load(('images/effects/damage2.png')),
pygame.image.load(('images/effects/damage3.png'))
)


####BACKGROUND///MENU
background=pygame.image.load(('images/background/background_default.png'))

clouds=pygame.image.load(('images/background/clouds.png'))

towers=pygame.image.load(('images/background/towers.png'))

sky=pygame.image.load(('images/background/sky.png'))

button_images=(
pygame.image.load(('images/buttons/play.png')),
pygame.image.load(('images/buttons/saveButton.png')),
pygame.image.load(('images/buttons/tutorial.png')),
pygame.image.load(('images/buttons/exit.png'))
)

button_play_blocked=pygame.image.load(('images/buttons/play_blocked.png'))

button_images_activated=(
pygame.image.load(('images/buttons/play_active.png')),
pygame.image.load(('images/buttons/saveButton_active.png')),
pygame.image.load(('images/buttons/tutorial_active.png')),
pygame.image.load(('images/buttons/exit_active.png'))
)

button_images_clicked=(
pygame.image.load(('images/buttons/play_clicked.png')),
pygame.image.load(('images/buttons/saveButton_clicked.png')),
pygame.image.load(('images/buttons/tutorial_clicked.png')),
pygame.image.load(('images/buttons/exit_clicked.png'))
)

background_blocked=pygame.image.load(('images/background/background_blocked.png'))

background_tutorial=pygame.image.load(('images/background/background_tutorial.png'))

bg_save_mask=pygame.image.load(('images/background/background_save_mask.png'))

background_save = pygame.image.load(('images/background/background_save.png'))

bg_finished=pygame.image.load(('images/background/bg_finished.png'))

bg_game_over=pygame.image.load(('images/background/bg_game_over.png'))

saveBox=pygame.image.load(('images/buttons/saveBox.png'))