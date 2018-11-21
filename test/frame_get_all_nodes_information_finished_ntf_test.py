"""Unit tests for FrameGetAllNodesInformationFinishedNotification."""
import unittest
from pyvlx.frame_creation import frame_from_raw
from pyvlx.frame_get_all_nodes_information import FrameGetAllNodesInformationFinishedNotification


class TestFrameGetAllNodesInformationFinishedNotification(unittest.TestCase):
    """Test class for FrameGetAllNodesInformationFinishedNotification."""

    # pylint: disable=too-many-public-methods,invalid-name

    def test_discover_node_request(self):
        """Test FrameGetAllNodesInformationFinishedNotification."""
        frame = FrameGetAllNodesInformationFinishedNotification()
        self.assertEqual(bytes(frame), b'\x00\x03\x02\x05\x04')

    def test_discover_node_request_from_raw(self):
        """Test parse FrameGetAllNodesInformationFinishedNotification from raw."""
        frame = frame_from_raw(b'\x00\x03\x02\x05\x04')
        self.assertTrue(isinstance(frame, FrameGetAllNodesInformationFinishedNotification))

    def test_str(self):
        """Test string representation of FrameGetAllNodesInformationFinishedNotification."""
        frame = FrameGetAllNodesInformationFinishedNotification()
        self.assertEqual(
            str(frame),
            '<FrameGetAllNodesInformationFinishedNotification/>')
