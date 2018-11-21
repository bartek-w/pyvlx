"""Unit tests for FrameGetAllNodesInformationRequest."""
import unittest
from pyvlx.frame_creation import frame_from_raw
from pyvlx.frame_get_all_nodes_information import FrameGetAllNodesInformationRequest


class TestFrameGetAllNodesInformationRequest(unittest.TestCase):
    """Test class for FrameGetAllNodesInformationRequest."""

    # pylint: disable=too-many-public-methods,invalid-name

    def test_discover_node_request(self):
        """Test FrameGetAllNodesInformationRequest with NO_TYPE."""
        frame = FrameGetAllNodesInformationRequest()
        self.assertEqual(bytes(frame), b'\x00\x03\x02\x02\x03')

    def test_discover_node_request_from_raw(self):
        """Test parse FrameGetAllNodesInformationRequest from raw."""
        frame = frame_from_raw(b'\x00\x03\x02\x02\x03')
        self.assertTrue(isinstance(frame, FrameGetAllNodesInformationRequest))

    def test_str(self):
        """Test string representation of FrameGetAllNodesInformationRequest."""
        frame = FrameGetAllNodesInformationRequest()
        self.assertEqual(
            str(frame),
            '<FrameGetAllNodesInformationRequest/>')
