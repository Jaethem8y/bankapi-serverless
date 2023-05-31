from fastapi import APIRouter

from src.controller import util_controller
from src.controller.audit import single_audit_controller 
from src.controller.audit import audit_length_controller
from src.controller.audit import filter_audit_controller

router = APIRouter()


router.include_router(audit_length_controller.router,prefix="/length")
router.include_router(single_audit_controller.router,prefix="/single")
router.include_router(filter_audit_controller.router)
router.include_router(util_controller.router)



