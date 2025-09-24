# Copyright (c) 2025, BWH and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = [{
		"fieldname": "make",
		"label": "Make",
		"fieldtype": "Data",
		"width": 100,
	}, {
		"fieldname": "total_revenue",
		"label": "Total Revenue",
		"fieldtype": "Currency",
		"width": 100,
		"options": "INR",
	}]
 
	data = frappe.get_all(
		'Ride Booking',
		fields=["SUM(total_amount) as total_revenue", "vehicle.make"],
		filters={
			"docstatus": 1,
		},
		group_by='make'
	)
 
	chart = {
		"data": {
			"labels": [x.make for x in data],
			"datasets": [
				{
					"values": [float(x.total_revenue or 0) for x in data],
				}
			],
		},
		"type": "pie",
	}

	return columns, data, None, chart, None
