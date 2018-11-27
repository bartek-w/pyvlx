"""Unit test for Scenes object."""
import unittest

from pyvlx import PyVLX, Scene, Scenes

# pylint: disable=too-many-public-methods,invalid-name


class TestScenes(unittest.TestCase):
    """Test class for scenes object."""

    def test_get_item(self):
        """Test get_item."""
        pyvlx = PyVLX()
        scenes = Scenes(pyvlx)
        scene1 = Scene(pyvlx, 0, 'Scene_1')
        scenes.add(scene1)
        scene2 = Scene(pyvlx, 1, 'Scene_2')
        scenes.add(scene2)
        scene3 = Scene(pyvlx, 2, 'Scene_3')
        scenes.add(scene3)
        self.assertEqual(scenes['Scene_1'], scene1)
        self.assertEqual(scenes['Scene_2'], scene2)
        self.assertEqual(scenes['Scene_3'], scene3)
        self.assertEqual(scenes[0], scene1)
        self.assertEqual(scenes[1], scene2)
        self.assertEqual(scenes[2], scene3)

    def test_get_item_failed(self):
        """Test get_item with non existing object."""
        pyvlx = PyVLX()
        scenes = Scenes(pyvlx)
        scene1 = Scene(pyvlx, 0, 'Scene_1')
        scenes.add(scene1)
        with self.assertRaises(KeyError):
            scenes['Scene_2']  # pylint: disable=pointless-statement
        with self.assertRaises(IndexError):
            scenes[1]  # pylint: disable=pointless-statement

    def test_iter(self):
        """Test iterator."""
        pyvlx = PyVLX()
        scenes = Scenes(pyvlx)
        scene1 = Scene(pyvlx, 0, 'Scene_1')
        scenes.add(scene1)
        scene2 = Scene(pyvlx, 1, 'Scene_2')
        scenes.add(scene2)
        scene3 = Scene(pyvlx, 2, 'Scene_3')
        scenes.add(scene3)
        self.assertEqual(
            tuple(scenes.__iter__()),
            (scene1, scene2, scene3))

    def test_len(self):
        """Test len."""
        pyvlx = PyVLX()
        scenes = Scenes(pyvlx)
        self.assertEqual(len(scenes), 0)
        scenes.add(Scene(pyvlx, 0, 'Scene_1'))
        scenes.add(Scene(pyvlx, 1, 'Scene_2'))
        scenes.add(Scene(pyvlx, 2, 'Scene_3'))
        scenes.add(Scene(pyvlx, 3, 'Scene_4'))
        self.assertEqual(len(scenes), 4)

    def test_add_same_object(self):
        """Test adding object with same scene_id."""
        pyvlx = PyVLX()
        scenes = Scenes(pyvlx)
        self.assertEqual(len(scenes), 0)
        scenes.add(Scene(pyvlx, 0, 'Scene_1'))
        scenes.add(Scene(pyvlx, 1, 'Scene_2'))
        scenes.add(Scene(pyvlx, 2, 'Scene_3'))
        scenes.add(Scene(pyvlx, 1, 'Scene_2_same_id'))
        self.assertEqual(len(scenes), 3)
        self.assertEqual(scenes[1].name, 'Scene_2_same_id')

    def test_add_item_failed(self):
        """Test add() with wrong type."""
        pyvlx = PyVLX()
        scenes = Scenes(pyvlx)
        with self.assertRaises(TypeError):
            scenes.add(scenes)
        with self.assertRaises(TypeError):
            scenes.add("scene")

    def test_clear(self):
        """Test clear() method."""
        pyvlx = PyVLX()
        scenes = Scenes(pyvlx)
        self.assertEqual(len(scenes), 0)
        scenes.add(Scene(pyvlx, 0, 'Scene_1'))
        scenes.add(Scene(pyvlx, 1, 'Scene_2'))
        scenes.clear()
        self.assertEqual(len(scenes), 0)
