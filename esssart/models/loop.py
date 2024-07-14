from collections import namedtuple
from .base import Base


class Loop(Base):
    table = "loop"
    fields = [
        "id TEXT PRIMARY KEY",
        "app_version INTEGER",
        'attachment_id TEXT',
        "bar_length INTEGER",
        "username TEXT",
        "creator_id INTEGER",
        "bps string",
        "instrument TEXT",
        "buffer_path TEXT",
        "buffer_url TEXT",
        "created INTEGER",
        "color_history BLOB",
        "cdn_attachment_id integer"
        "creator_username TEXT",
        'is_bass BOOLEAN',
        'is_drum BOOLEAN',
        'is_mic BOOLEAN',
        'is_normalized BOOLEAN',
        'is_note BOOLEAN',
        "length INTEGER",
        "length_16ths INTEGER",
        "original_pitch INTEGER",
        "preset_name TEXT",
        "primary_colour TEXT",
        "sample_rate INTEGER",
        'created TEXT',
    ]

    index = ["loop_idx ON loop(id)",
             "loop_idx_attachment ON loop(attachment_id)"
             "loop_user on loop(username)"
             "loop_creator on loop(creator_id)"]

    def __init__(self, db):
        super().__init__(db)
        self.Loop = namedtuple("Loop", self.field_names)
        self.tuple = self.Loop


