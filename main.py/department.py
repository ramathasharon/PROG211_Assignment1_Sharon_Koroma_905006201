"""
department.py
-------------
Defines the Department class. A Department ACTS ON Complaint objects,
which is the interaction between objects required by Task 1.
"""


class Department:
    """A government department that handles certain complaint categories."""

    def __init__(self, name, handles):
        self.name = name
        self.handles = handles  # a tuple of categories, e.g. ("Water",)

    def can_handle(self, complaint):
        """True if this department is responsible for the complaint."""
        return complaint.category in self.handles

    def review(self, complaint):
        """Move a complaint to 'In Review' (object interaction)."""
        if not self.can_handle(complaint):
            return f"{self.name} does not handle {complaint.category} complaints."
        complaint.update_status("In Review")
        return f"{self.name} is now reviewing {complaint.complaint_id}."

    def resolve(self, complaint):
        """Mark a complaint as 'Resolved' (object interaction)."""
        if not self.can_handle(complaint):
            return f"{self.name} does not handle {complaint.category} complaints."
        complaint.update_status("Resolved")
        return f"{self.name} resolved {complaint.complaint_id}."