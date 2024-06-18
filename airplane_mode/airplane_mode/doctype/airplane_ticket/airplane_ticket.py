# Copyright (c) 2024, William Kristiawan and contributors
# For license information, please see license.txt

import frappe
import random
import string
from frappe.model.document import Document


class AirplaneTicket(Document):
	def before_save(self):
		if self.seat == None:
			self.generate_seat()
		self.cal_total_amount()
	
	def validate(self):
		unique_data = set()
		filtered_res = []
		for item in self.add_ons:
			if item.get('item') not in unique_data:
				filtered_res.append(item)
				unique_data.add(item.get('item'))
		self.set('add_ons', filtered_res)

	def before_submit(self):
		if (self.status != "Boarded"):
			frappe.throw("You can not submit ticket, ticket status must be boarded.")

	def cal_total_amount(self):
		total_ammount_add_ons = 0
		
		for ammount in self.add_ons:
			total_ammount_add_ons += ammount.amount
		self.total_amount = total_ammount_add_ons + float(self.flight_price)

	def generate_seat(self):
		seat_number = random.randint(1, 100)
		seat_letter = random.choice(string.ascii_uppercase[:5])
		self.seat= f"{seat_number}{seat_letter}"
