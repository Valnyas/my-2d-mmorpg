import Phaser from 'phaser'

class GameScene extends Phaser.Scene {
    constructor() {
        super({ key: 'GameScene' })
    }

    preload() {
        // Загрузка assets будет здесь
        this.load.image('logo', 'assets/logo.png')
    }

    create() {
        // Создание игрового мира
        this.add.text(400, 300, '2D MMORPG', {
            fontSize: '32px',
            fill: '#fff'
        }).setOrigin(0.5)

        this.add.text(400, 350, 'Разработка в процессе...', {
            fontSize: '16px',
            fill: '#ccc'
        }).setOrigin(0.5)
    }

    update() {
        // Игровая логика будет здесь
    }
}

const config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    parent: 'game-container',
    scene: GameScene,
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 0 },
            debug: false
        }
    }
}

// Запуск игры
const game = new Phaser.Game(config)

// Убираем сообщение о загрузке
document.querySelector('.loading').style.display = 'none'