from typing import List, Any
from checkov.common.models.enums import CheckCategories
from checkov.arm.base_resource_value_check import BaseResourceValueCheck

#from checkov.terraform.checks.resource.azure.EventgridDomainNetworkAccess import EventgridDomainNetworkAccess

class EventgridDomainNetworkAccess(BaseResourceValueCheck):
    def __init__(self):
        name = "Ensure that Azure Event Grid Domain public network access is disabled"
        id = "CKV_AZURE_106"
        supported_resources = ("Microsoft.EventGrid/domains",)
        categories = [CheckCategories.NETWORKING]
        super().__init__(name=name,
                         id=id,
                         categories=categories,
                        supported_resources=supported_resources,
                         )

    def get_inspected_key(self) -> str:
        return "properties/publicNetworkAccess"

    def get_expected_value(self) -> str:
        return "Disabled"

check = EventgridDomainNetworkAccess()

