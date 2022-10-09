import random

from flet import *
from flet import colors

CIRCULAR_RADIUS = 30
CIRCULAR_STORE_WITH = 10
STAFF_LINE_HEIGHT = 10
APP_NAME = "识谱练习"


def createCircular(
        radius_number: int = CIRCULAR_RADIUS,
        circular_color: str = colors.BLACK,
        circular_width: int = CIRCULAR_STORE_WITH,
        circular_fill_color: str = colors.WHITE, data_value: str = None) -> CircleAvatar:
    """
    绘制圆环
    """
    return CircleAvatar(
        width=radius_number,
        height=radius_number,
        bgcolor=circular_color,
        data=data_value,
        content=CircleAvatar(
            width=radius_number - circular_width,
            height=radius_number - circular_width,
            bgcolor=circular_fill_color,
        )
    )


def createDivider(line_color: str = colors.BLACK,
                  line_height: int = STAFF_LINE_HEIGHT) -> Divider:
    """
    创建一线水平线
    """
    return Divider(color=line_color, height=line_height)


def createStack(divider_line: Divider, circle_avatar: CircleAvatar):
    return Stack(
        [
            Container(
                content=divider_line,
                alignment=Alignment(0, 0)
            ),
            Container(
                content=circle_avatar,
                alignment=Alignment(0, 0)
            )
        ],
        expand=True,
    )


def main(page: Page):
    page.title = APP_NAME
    page.vertical_alignment = "center"

    max_number = 5
    start_staff_value = 4
    max_staff_value = 7

    staff_list = []
    circular_list = []
    for number in range(max_number):
        top_circular = createCircular(data_value=start_staff_value)
        start_staff_value = start_staff_value - 1
        if start_staff_value < 1:
            start_staff_value = 7
        stack_view = createStack(createDivider(), top_circular)
        circular_list.append(top_circular)
        staff_list.append(stack_view)
        circular = createCircular(data_value=start_staff_value)
        start_staff_value = start_staff_value - 1
        if start_staff_value <= 0:
            start_staff_value = 7
        circular_list.append(circular)
        if number is not (max_number - 1):
            staff_list.append(
                Container(
                    content=circular,
                    alignment=Alignment(0, 0)
                )
            )


    def randomStaff(e):
        for item in circular_list:
            item.visible = False
        item_view = random.choice(circular_list)
        item_view.visible = True
        print(item_view.data)
        page.update()

    outlined_button = OutlinedButton("下一个", on_click=randomStaff)
    staff_list.append(outlined_button)

    m_column = Column(
        staff_list,
        spacing=1,
        expand=True
    )
    page.add(m_column)


flet.app(target=main)
