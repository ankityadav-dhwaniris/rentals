# Copyright (c) 2025, BWH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RideBooking(Document):
	def validate(self):
		if not self.rate:
			self.rate = frappe.db.get_single_value("Rental Settings", "standard_rate")
		total_distance = 0
		for items in (self.items or []):
			total_distance += items.distance or 0
		
		self.total_amount = total_distance * self.rate
