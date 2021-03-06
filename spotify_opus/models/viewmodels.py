from typing import List, Optional


class AlbumVM:

    def __init__(self, name):
        self.name: str = name
        self.artists: List[str] = []
        self.tracks: List[TrackVM] = []
        self.image_url = ""


class TrackVM:

    def __init__(self, name: str, track_number: Optional[int] = None,
                 duration: str = "0:00"):
        self.name: str = name
        self.track_number: Optional[int] = track_number
        self.duration = duration

    def __repr__(self):
        return f"<TrackVM: {self.track_number}: {self.name}"


class SearchItemVM:

    def __init__(self, url: str, image_url: str,
                 primary_label: str = "Result Name",
                 sec_labels: List[str] = None):
        self.url = url
        self.image_url = image_url
        self.primary_label = primary_label
        self.sec_labels = sec_labels

    def __repr__(self):
        return f"<SearchItemVM: {self.primary_label}>"


class CategoryResultVM:

    def __init__(self, name: str):
        self.name: str = name
        self.items: List[SearchItemVM] = []

    def __repr__(self):
        return f"<CategoryResultVM {self.name}>"
