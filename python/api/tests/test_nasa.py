#!/usr/bin/env python
#!/usr/bin/python3

import os
import sys
import unittest
from pathlib import Path

TEST_DIR = os.path.dirname(os.path.realpath(__file__))
API_DIR = os.path.dirname(TEST_DIR)

sys.path.insert(0, API_DIR)
from nasa import NASA, EPIC, Curiosity

def clean_dir(directory:Path):
    assert directory.exists() and directory.is_dir()
    for x in directory.iterdir():
        if x.is_file(): x.unlink()
        elif x.is_dir(): clean_dir(x)
    directory.rmdir()

class TestNASA(unittest.TestCase):
    def setUp(self)->None:
        self.test_dir = Path(TEST_DIR) / 'TestNASA'
        if not self.test_dir.exists(): self.test_dir.mkdir()
        self.epic = EPIC(save_dir=self.test_dir)

    def tearDown(self) -> None:
        if self.test_dir.exists() and self.test_dir.is_dir(): clean_dir(self.test_dir)

    def test_get_epic_images(self):
        self.epic.get_epic_images()
        nasa_dir: Path = self.test_dir / 'epic'
        gif_dir: Path = nasa_dir / 'gifs'
        images_dir: Path = nasa_dir / 'images'
        data_dir:  Path = nasa_dir / 'api_data'
        self.assertTrue(nasa_dir.exists() and nasa_dir.is_dir())
        self.assertTrue(gif_dir.exists() and gif_dir.is_dir())
        self.assertTrue(images_dir.exists() and images_dir.is_dir())
        self.assertTrue(data_dir.exists() and data_dir.is_dir())

if __name__ == '__main__':
    print(f"Testing NASA API...")
    unittest.main()
