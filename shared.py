from __future__ import annotations as _annotations

from fastui import AnyComponent
from fastui import components as c
from fastui.events import GoToEvent

def demo_page(*components: AnyComponent, title: str | None = None) -> list[AnyComponent]:
    return [
        c.PageTitle(text=f'FastUI Demo — {title}' if title else 'FastUI Demo'),
        c.Navbar(
            title='FastUI ChatBot',
            title_event=GoToEvent(url="/"),
            start_links=[
                c.Link(
                    components=[c.Text(text='Copilot API')],
                    on_click=GoToEvent(url='/serverapi'),
                    active='startwith:/serverapi'
                )
            ]
        ),
        c.Page(
            components=[
                *((c.Heading(text=title),) if title else ()),
                *components,
            ],
        ),
    ]