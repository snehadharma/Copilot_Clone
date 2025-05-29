from __future__ import annotations as _annotations

from fastapi import APIRouter
from fastui import AnyComponent, FastUI
from fastui import components as c

from shared import demo_page

router = APIRouter()

@router.get('/', response_model=FastUI, response_model_exclude=True)
def api_index() -> list[AnyComponent]:
    markdown="""\
This site provides a general-use LLM chatbot. 
"""
    return demo_page(c.Markdown(text=markdown))

@router.get('/{path:path}', status_code=404) 
async def api_404():
    return {"message": "not found"}