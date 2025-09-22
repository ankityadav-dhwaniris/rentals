# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Driver(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		enabled: DF.Check
		first_name: DF.Data
		full_name: DF.Data | None
		last_name: DF.Data | None
		license_number: DF.Data
		phone_number: DF.Phone | None
		profile_image: DF.AttachImage | None
	# end: auto-generated types
	
	def before_save(self):
		if self.first_name and self.last_name:
			self.full_name = f"{self.first_name} {self.last_name}"
		elif self.first_name:
			self.full_name = self.first_name
		else:
			self.full_name = ""
