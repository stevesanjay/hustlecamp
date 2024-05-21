import flet as ft

def reverse_string(string):
    return string[::-1]

def main(page: ft.Page):
    page.title = "Reverse String"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    input_field = ft.TextField(label="Enter a string")
    button = ft.ElevatedButton("Reverse", on_click=lambda _: reverse_string_button_clicked(page, input_field))
    page.add(input_field, button)

def reverse_string_button_clicked(page, input_field):
    input_string = input_field.value
    reversed_str = reverse_string(input_string)  # Rename variable to avoid conflict
    page.add(
        ft.Text(f"Original String: {input_string}"),
        ft.Text(f"Reversed String: {reversed_str}"),  # Use the renamed variable here
    )

if __name__== "__main__":
    ft.app(main)





"""
 flet run --web three.py
"""