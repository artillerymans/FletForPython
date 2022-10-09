import flet
from flet import (
    Column,
    FloatingActionButton,
    Icon,
    NavigationRail,
    NavigationRailDestination,
    Page,
    Row,
    Text,
    VerticalDivider,
    icons, Ref,
)

def main(page: Page):

    mTextContent = Ref[Text]()
    mNavigationRail = Ref[NavigationRail]()
    mColumn = Ref[Column]()

    def on_page_change(e):
        print("Selected destination:", e.control.selected_index)
        mTextContent.current.value = f"Body!{e.control.selected_index}"
        page.update()


    def createColum(index: int) -> Column:
        print(index)
        mColumn.current.controls.pop()
        return Column([mTextContent.current], alignment="start", expand=True)





    rail = NavigationRail(
        selected_index=0,
        label_type="all",
        # extended=True,
        min_width=100,
        min_extended_width=400,
        leading=FloatingActionButton(icon=icons.CREATE, text="Add"),
        group_alignment=-0.9,
        destinations=[
            NavigationRailDestination(
                icon=icons.FAVORITE_BORDER, selected_icon=icons.FAVORITE, label="First"
            ),
            NavigationRailDestination(
                icon_content=Icon(icons.BOOKMARK_BORDER),
                selected_icon_content=Icon(icons.BOOKMARK),
                label="Second",
            ),
            NavigationRailDestination(
                icon=icons.SETTINGS_OUTLINED,
                selected_icon_content=Icon(icons.SETTINGS),
                label_content=Text("Settings"),
            ),
        ],
        on_change=on_page_change,
    )

    mText = Text(ref=mTextContent, value=f"Body!{rail.selected_index}")

    page.add(
        Row(
            [
                rail,
                VerticalDivider(width=1),
                createColum(rail.selected_index),
            ],
            expand=True,
        )
    )

flet.app(target=main)


