import frappe


@frappe.whitelist(allow_guest=True)
def get_emoji():
	return "🚗" 

def get_permission_query_conditions_for_vehicle(user):
    return "name = 1"