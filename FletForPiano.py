import random

from flet import *
from flet import colors
from flet.alignment import center_left, center

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
                    bgcolor=circular_fill_color
                )
            )


def createDivider(line_color: str = colors.BLACK,
                  line_height: int = STAFF_LINE_HEIGHT) -> Divider:
    """
    创建一线水平线
    """
    return Divider(color=line_color, height=line_height)


def createStack(divider_line: Divider, circle: CircleAvatar):
    return Stack(
        [
            Container(
                content=circle,
                alignment=Alignment(0, 0)
            ),
            Container(
                content=divider_line,
                alignment=Alignment(0, 0)
            )
        ],
        expand=True
    )


def createOutLine(divider_line: Divider, circle: CircleAvatar):
    return Row(
        [
            Container(
                expand=1
            ),
            Stack(
                [
                    Container(
                        content=circle,
                        alignment=center,
                    ),
                    Container(
                        content=divider_line,
                        alignment=center,
                    )
                ],
                width=250,
                height=CIRCULAR_RADIUS
            ),
            Container(
                expand=1
            )
        ],
        alignment="center",
        vertical_alignment="center",

    )


last_choice_int = 0


def main(page: Page):
    page.title = APP_NAME
    page.vertical_alignment = "center"
    staff_list = []
    circular_list = []

    # 上加4线
    max_number = 5
    start_staff_value = 7
    for number in range(max_number):
        top_circular = createCircular(data_value=start_staff_value)
        circular_list.append(top_circular)
        start_staff_value = start_staff_value - 1
        if start_staff_value < 1:
            start_staff_value = 7
        stack_view = createOutLine(createDivider(), top_circular)
        staff_list.append(stack_view)
        circular = createCircular(data_value=start_staff_value)
        circular_list.append(circular)
        start_staff_value = start_staff_value - 1
        if start_staff_value <= 0:
            start_staff_value = 7
        staff_list.append(
            Container(
                content=circular,
                alignment=Alignment(0, 0)
            )
        )

    start_staff_value = 4
    max_staff_value = 7
    # 中间五线谱
    for number in range(max_number):
        top_circular = createCircular(data_value=start_staff_value)
        circular_list.append(top_circular)
        start_staff_value = start_staff_value - 1
        if start_staff_value < 1:
            start_staff_value = 7
        stack_view = createStack(createDivider(), top_circular)

        staff_list.append(stack_view)
        circular = createCircular(data_value=start_staff_value)
        circular_list.append(circular)
        start_staff_value = start_staff_value - 1
        if start_staff_value <= 0:
            start_staff_value = 7
        staff_list.append(
            Container(
                content=circular,
                alignment=Alignment(0, 0)
            )
        )

    # 下加3线
    max_number = 3
    start_staff_value = 1
    for number in range(max_number):
        top_circular = createCircular(data_value=start_staff_value)
        circular_list.append(top_circular)
        start_staff_value = start_staff_value - 1
        if start_staff_value < 1:
            start_staff_value = 7
        stack_view = createOutLine(createDivider(), top_circular)
        staff_list.append(stack_view)
        circular = createCircular(data_value=start_staff_value)
        circular_list.append(circular)
        start_staff_value = start_staff_value - 1
        if start_staff_value <= 0:
            start_staff_value = 7
        staff_list.append(
            Container(
                content=circular,
                alignment=Alignment(0, 0)
            )
        )

    def randomStaff(e):
        for item in circular_list:
            item.visible = False
        while_status = True
        global last_choice_int
        while while_status:
            item_view = random.choice(circular_list)
            if int(item_view.data) != last_choice_int:
                item_view.visible = True
                last_choice_int = int(item_view.data)
                while_status = False
        page.update()

    outlined_button = OutlinedButton("Random", on_click=randomStaff)
    staff_list.append(outlined_button)

    def checkAllStaff(e):
        for item in circular_list:
            print("item data = ", item.data, ", item visible = ", item.visible)

    check_button = OutlinedButton("Check Visible", on_click=checkAllStaff)
    staff_list.append(check_button)

    m_column = Column(
        staff_list,
        spacing=1,
        expand=True,
        alignment="center"
    )

    page.add(Stack(
        [
            m_column,
            Image(
                src=f"https://pic.ntimg.cn/file/20160530/22432193_145108213861_2.jpg",
                width=200,
                height=200,
                fit="contain",
                bottom=150,
                top=150
            )
        ],
        expand=True
    ))


flet.app(target=main)
