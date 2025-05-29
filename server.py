import asyncio
from itertools import chain
from typing import AsyncIterable

from fastapi import APIRouter
from fastui import FastUI, components as c

router = APIRouter()

@router.get('/chatbot', response_model=FastUI, response_model_exclude=True)
def render_server() -> str:
    return "hello from the server"