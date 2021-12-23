from airflow.utils.decorators import apply_defaults
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator
from blocksec_plugin.abis import TELLOR_ABI


class TellorOracleOperator(ContractInteractionOperator):
    template_fields = ['request_id', 'price']

    @apply_defaults
    def __init__(self,
                 request_id,
                 price,
                 *args,
                 **kwargs):
        super().__init__(abi_json=TELLOR_ABI, *args, **kwargs)
        self.request_id = request_id
        self.price = price
        self.function = self.contract.functions.submitValue

    def execute(self, context):
        self.function_args = {"requestId": self.request_id, "value": self.price}
        return super().execute(context)
