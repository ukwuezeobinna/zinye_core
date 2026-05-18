__version__ = "0.0.1"

try:
	from frappe.integrations.frappe_providers import frappecloud_billing as _billing

	def _get_base_url():
		import frappe
		return frappe.conf.get("fc_base_url") or "https://frappecloud.com"

	_billing.get_base_url = _get_base_url
except ImportError:
	pass

try:
	import hrms.subscription_utils as _sub_utils
	import requests as _requests

	def _has_subscription(secret_key) -> bool:
		if not secret_key:
			return False
		import frappe
		base_url = frappe.conf.get("fc_base_url") or "https://frappecloud.com"
		url = f"{base_url}/api/method/press.api.developer.marketplace.get_subscription_status?secret_key={secret_key}"
		try:
			response = _requests.request(method="POST", url=url, timeout=5)
			return response.json().get("message") == "Active"
		except Exception:
			return False

	_sub_utils.has_subscription = _has_subscription
except ImportError:
	pass
