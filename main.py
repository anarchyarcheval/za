def on_overlap_tile(sprite, location):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        void_wall_right
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    tiles.set_wall_at(location2, True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        log_tile_placeholder2
    """),
    on_overlap_tile2)

def on_overlap_tile3(sprite3, location3):
    tiles.set_wall_at(location3, True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        log_tile_placeholder1
    """),
    on_overlap_tile3)

def on_overlap_tile4(sprite4, location4):
    tiles.set_wall_at(location4, True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        log_tile_placeholder3
    """),
    on_overlap_tile4)

def on_a_pressed():
    mySprite.vy = -150
    animation.run_image_animation(mySprite,
        assets.animation("""
            archeval_wings_front
        """),
        50,
        False)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    animation.run_image_animation(mySprite,
        assets.animation("""
            archeval_wings_left
        """),
        100,
        False)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_overlap_tile5(sprite5, location5):
    scene.set_background_image(assets.image("""
        sky further
    """))
    tiles.set_tilemap(tilemap("""
        level5
    """))
    tiles.place_on_random_tile(mySprite, assets.tile("""
        portal spawn
    """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        portal 0
    """),
    on_overlap_tile5)

def on_overlap_tile6(sprite6, location6):
    scene.set_background_image(assets.image("""
        filename 2
    """))
    scrunkly.destroy()
    tiles.set_tilemap(tilemap("""
        filename
    """))
    tiles.place_on_tile(mySprite, tiles.get_tile_location(3, 3))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile3
    """),
    on_overlap_tile6)

def on_overlap_tile7(sprite7, location7):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        void_centre
    """),
    on_overlap_tile7)

def on_overlap_tile8(sprite8, location8):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        void_roof0
    """),
    on_overlap_tile8)

def on_overlap_tile9(sprite9, location9):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        void_wall_left0
    """),
    on_overlap_tile9)

def on_right_pressed():
    animation.run_image_animation(mySprite,
        assets.animation("""
            archeval_wings_right
        """),
        100,
        False)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_overlap_tile10(sprite10, location10):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        void_floor0
    """),
    on_overlap_tile10)

def on_overlap_tile11(sprite11, location11):
    tiles.set_wall_at(location11, True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        log_tile_placeholder0
    """),
    on_overlap_tile11)

def on_overlap_tile12(sprite12, location12):
    global scrunkly
    scene.set_background_image(assets.image("""
        sky0
    """))
    tiles.set_tilemap(tilemap("""
        level8
    """))
    tiles.place_on_random_tile(mySprite, assets.tile("""
        pillar bottom1
    """))
    scrunkly = sprites.create(assets.image("""
        scrunkly0
    """), SpriteKind.enemy)
    animation.run_image_animation(scrunkly,
        assets.animation("""
            scrunkly twirl
        """),
        100,
        True)
    scrunkly.set_position(75, 1)
    scrunkly.follow(mySprite)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        portal 1
    """),
    on_overlap_tile12)

def on_overlap_tile13(sprite13, location13):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        void
    """),
    on_overlap_tile13)

def on_overlap_tile14(sprite14, location14):
    tiles.set_wall_at(location14, True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        log_tile_placeholder
    """),
    on_overlap_tile14)

def on_on_overlap(sprite15, otherSprite):
    game.over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

scrunkly: Sprite = None
mySprite: Sprite = None
mySprite = sprites.create(assets.image("""
    archie_static
"""), SpriteKind.player)
animation.run_image_animation(mySprite, assets.animation("""
    myAnim
"""), 200, False)
mySprite.set_stay_in_screen(True)
scene.camera_follow_sprite(mySprite)
mySprite.ay = 500
controller.move_sprite(mySprite, 100, 0)
scene.set_background_image(assets.image("""
    cityscape
"""))
tiles.set_tilemap(tilemap("""
    level3
"""))
tiles.place_on_random_tile(mySprite, assets.tile("""
    forestTiles0
"""))