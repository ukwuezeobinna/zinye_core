__version__ = "0.0.1"

try:
	from frappe.integrations.frappe_providers import frappecloud_billing as _billing

	def _get_base_url():
		import frappe
		return frappe.conf.get("fc_base_url") or "https://frappecloud.com"

	_billing.get_base_url = _get_base_url
except ImportError:
	pass
