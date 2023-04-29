from typing import Dict, List, Tuple, Any, Optional

class OptimizerResults:
    def __init__(self, results: Any, extras: Optional[Dict[str, Any]] = None) -> None:
        """
        Creates OptimizerResults object.

        Args:
            results (Any):
                results object produced by optimization problem
            extras (Dict[str, Any]):
                key (str): extra label
                val (Any): extra value
        """
        self._results: Any = results
        self._extras: Dict[str, Any] = extras if extras is not None else {}

    @property
    def results(self) -> Any:
        return self._results

    @property
    def extras(self) -> Dict[str, Any]:
        return self._extras


class AgriculturalOptimization:
    """
    This class is used to optimize the agricultural production of a farm using crop rotaion.
    
    """
    REQUIRED_PARAMS = ["area","yeild","soil","price","fertizer_need","impactFactor","fertilizer_price","Enviorment","I","J","K"]
    def __init__(self, params) -> None:
        """
        Set up DistributedEnergyOptimizer object.

        Args:
            params (dict): required params specificed by REQUIRED_PARAMS
                key (str): param name
                val (Any): param values
        """

        for label in self.REQUIRED_PARAMS:  # make sure we have all the required params
            if label not in params:
                raise ValueError(f"Please provide {label} in params.")
        
        self.params = params.copy()
