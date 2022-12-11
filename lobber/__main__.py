from constants import *
from game.directing.director import Director
from game.directing.scene_manager import SceneManager
from pathlib import Path

def main():
    current_directory = Path.cwd()
    director = Director(SceneManager.VIDEO_SERVICE)
    director.start_game()

if __name__ == "__main__":
    main()