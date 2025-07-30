# Introduction

Nfcflet for Flet.

## Examples

```
import flet as ft

from nfcflet import Nfcflet


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(

                ft.Container(height=150, width=300, alignment = ft.alignment.center, bgcolor=ft.Colors.PURPLE_200, content=Nfcflet(
                    tooltip="My new Nfcflet Control tooltip",
                    value = "My new Nfcflet Flet Control", 
                ),),

    )


ft.app(main)
```

## Classes

[Nfcflet](Nfcflet.md)


