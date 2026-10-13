"""
complaint.py
------------
Defines the Complaint class for the Citizen Complaint System.

DPG note (privacy): a Complaint stores NO personal data. It only keeps a
reference ID, a category, a district, a description and a status.
"""

import re

# ---- Tuples (constants that must never change) ----------------------------
CATEGORIES = ("Water", "Roads", "Electricity", "Health", "Sanitation")
STATUSES = ("Received", "In Review", "Resolved")
DISTRICTS = (
    "Bo", "Bombali", "Bonthe", "Falaba", "Kailahun", "Kambia", "Karene",
    "Kenema", "Koinadugu", "Kono", "Moyamba", "Port Loko", "Pujehun",
    "Tonkolili", "Western Area Rural", "Western Area Urban",
)


class Complaint:
    """A single citizen complaint, identified only by a reference ID."""

    # Class attribute: shared by ALL complaints, used to make unique IDs.
    _counter = 0

    def __init__(self, complaint_id, category, district, description,
                 status="Received"):
        # Instance attributes: different for every Complaint object.
        self.complaint_id = complaint_id
        self.category = category
        self.district = district
        self.description = description
        self.status = status

    # ---- Instance methods (work on ONE complaint) --------------------------
    def update_status(self, new_status):
        """Change the status. Returns True if valid, False otherwise."""
        if new_status not in STATUSES:  # validate against the tuple
            return False
        self.status = new_status
        return True

    def display_info(self):
        """Print the complaint in a clear, readable layout."""
        print(f"  ID          : {self.complaint_id}")
        print(f"  Category    : {self.category}")
        print(f"  District    : {self.district}")
        print(f"  Description : {self.description}")
        print(f"  Status      : {self.status}")

    # ---- Class methods (work on the CLASS, not one object) -----------------
    @classmethod
    def generate_id(cls):
        """Create the next unique ID, e.g. CMP-001, CMP-002 ..."""
        cls._counter += 1
        return f"CMP-{cls._counter:03d}"

    @classmethod
    def create(cls, category, district, description):
        """Factory: build a Complaint and give it an automatic ID."""
        return cls(cls.generate_id(), category, district, description)

    # ---- Static method (a helper that needs no object or class data) -------
    @staticmethod
    def is_valid_description(text):
        """
        Check a description is usable AND privacy-safe.
        Returns (is_valid, message) -- a tuple.
        """
        text = text.strip()
        if len(text) < 10:
            return (False, "Description must be at least 10 characters.")
        if len(text) > 300:
            return (False, "Description must be 300 characters or fewer.")
        # Privacy check: reject anything that looks like a phone number.
        if re.search(r"\d{7,}", text.replace(" ", "").replace("-", "")):
            return (False, "Please remove phone numbers or ID numbers "
                           "(privacy protection).")
        return (True, "OK")