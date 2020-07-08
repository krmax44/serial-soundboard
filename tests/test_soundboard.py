import unittest
import soundboard
from os import path
from unittest.mock import patch

fixture = path.join(path.dirname(__file__), "fixture/", "sounds/")


def do_nothing(*args):
    pass


class TestSoundboard(unittest.TestCase):
    @patch("soundboard.SOUNDSPATH", fixture)
    def test_file_discovery(self):
        sounds = soundboard.all_sounds()
        self.assertListEqual(sounds, ["test.flac", "test.mp3"])

    @patch("soundboard.SOUNDSPATH", fixture)
    @patch("soundboard.playsound")
    def test_file_playing(self, patch):
        patch.new = do_nothing
        soundboard.play_sound("test.mp3")
        file = path.join(fixture, "test.mp3")

        self.assertEqual(patch.call_args_list, [unittest.mock.call(file, False)])


if __name__ == "__main__":
    unittest.main()
