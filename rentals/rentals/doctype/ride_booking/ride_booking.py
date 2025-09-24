# Copyright (c) 2025, BWH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RideBooking(Document):
	def validate(self):
		if not self.rate:
			frappe.throw("Please provide a rate for the ride")
		total_distance = 0
		for items in (self.items or []):
			total_distance += items.distance or 0
		
		self.total_amount = total_distance * self.rate
