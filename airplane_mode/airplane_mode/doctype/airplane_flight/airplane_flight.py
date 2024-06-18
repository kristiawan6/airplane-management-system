# Copyright (c) 2024, William Kristiawan and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
	def before_submit(self):
		self.status = "Completed"

	@frappe.whitelist()
	def set_flight_status(self):
		flight = frappe.get_doc("Airplane Flight",)
		flight.status = "Completed"
		flight.save()
