scene.onOverlapTile(SpriteKind.Player, assets.tile`
        void_wall_right
    `, function on_overlap_tile(sprite: Sprite, location: tiles.Location) {
    game.over(false)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        log_tile_placeholder2
    `, function on_overlap_tile2(sprite2: Sprite, location2: tiles.Location) {
    tiles.setWallAt(location2, true)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        log_tile_placeholder1
    `, function on_overlap_tile3(sprite3: Sprite, location3: tiles.Location) {
    tiles.setWallAt(location3, true)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        log_tile_placeholder3
    `, function on_overlap_tile4(sprite4: Sprite, location4: tiles.Location) {
    tiles.setWallAt(location4, true)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    mySprite.vy = -150
    animation.runImageAnimation(mySprite, assets.animation`
            archeval_wings_front
        `, 50, false)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function on_left_pressed() {
    animation.runImageAnimation(mySprite, assets.animation`
            archeval_wings_left
        `, 100, false)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        portal 0
    `, function on_overlap_tile5(sprite5: Sprite, location5: tiles.Location) {
    scene.setBackgroundImage(assets.image`
        sky further
    `)
    tiles.setTilemap(tilemap`
        level5
    `)
    tiles.placeOnRandomTile(mySprite, assets.tile`
        portal spawn
    `)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        myTile3
    `, function on_overlap_tile6(sprite6: Sprite, location6: tiles.Location) {
    scene.setBackgroundImage(assets.image`
        filename 2
    `)
    scrunkly.destroy()
    tiles.setTilemap(tilemap`
        filename
    `)
    tiles.placeOnTile(mySprite, tiles.getTileLocation(3, 3))
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        void_centre
    `, function on_overlap_tile7(sprite7: Sprite, location7: tiles.Location) {
    game.over(false)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        void_roof0
    `, function on_overlap_tile8(sprite8: Sprite, location8: tiles.Location) {
    game.over(false)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        void_wall_left0
    `, function on_overlap_tile9(sprite9: Sprite, location9: tiles.Location) {
    game.over(false)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function on_right_pressed() {
    animation.runImageAnimation(mySprite, assets.animation`
            archeval_wings_right
        `, 100, false)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        void_floor0
    `, function on_overlap_tile10(sprite10: Sprite, location10: tiles.Location) {
    game.over(false)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        log_tile_placeholder0
    `, function on_overlap_tile11(sprite11: Sprite, location11: tiles.Location) {
    tiles.setWallAt(location11, true)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        portal 1
    `, function on_overlap_tile12(sprite12: Sprite, location12: tiles.Location) {
    
    scene.setBackgroundImage(assets.image`
        sky0
    `)
    tiles.setTilemap(tilemap`
        level8
    `)
    tiles.placeOnRandomTile(mySprite, assets.tile`
        pillar bottom1
    `)
    scrunkly = sprites.create(assets.image`
        scrunkly0
    `, SpriteKind.Enemy)
    animation.runImageAnimation(scrunkly, assets.animation`
            scrunkly twirl
        `, 100, true)
    scrunkly.setPosition(75, 1)
    scrunkly.follow(mySprite)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        void
    `, function on_overlap_tile13(sprite13: Sprite, location13: tiles.Location) {
    game.over(false)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        log_tile_placeholder
    `, function on_overlap_tile14(sprite14: Sprite, location14: tiles.Location) {
    tiles.setWallAt(location14, true)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap(sprite15: Sprite, otherSprite: Sprite) {
    game.over(false)
})
let scrunkly : Sprite = null
let mySprite : Sprite = null
mySprite = sprites.create(assets.image`
    archie_static
`, SpriteKind.Player)
animation.runImageAnimation(mySprite, assets.animation`
    myAnim
`, 200, false)
mySprite.setStayInScreen(true)
scene.cameraFollowSprite(mySprite)
mySprite.ay = 500
controller.moveSprite(mySprite, 100, 0)
scene.setBackgroundImage(assets.image`
    cityscape
`)
tiles.setTilemap(tilemap`
    level3
`)
tiles.placeOnRandomTile(mySprite, assets.tile`
    forestTiles0
`)
