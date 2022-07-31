from fastapi import APIRouter

from src.controller import util_controller
from src.controller import single_table_controller 
from src.controller import table_length_controller
from src.controller import filter_table_controller

router = APIRouter()


router.include_router(table_length_controller.router,prefix="/length")
router.include_router(single_table_controller.router,prefix="/single")
router.include_router(filter_table_controller.router)
router.include_router(util_controller.router)



