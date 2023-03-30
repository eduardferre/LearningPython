import openai
import typer
import config

from rich import print
from rich.table import Table

from PIL import Image
import requests
from io import BytesIO


def main():
    openai.api_key = config.api_key

    print("[bold green]ChatGPT API with Python[/bold green]")

    table = Table("Command", "Description")
    table.add_row("exit", "Exit from application")
    table.add_row("new", "Create a new conversation")

    print(table)

    context = {
            "role": "system", #it defines a context
            "content": "You are helpful assistant."}
    messages = [context]

    while True:
        
        content = __prompt()

        if content == "new":
            print("New conversation has been created")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content})

        print(f"[bold green]> [/bold green][green]{response_content}[/green]")

def __prompt() -> str:
    prompt = typer.prompt("\nQuestion... ")

    if prompt == "exit":
        exit = typer.confirm("Are you sure?")
        if exit:
            print("Bye bye")
            raise typer.Abort()
        
        return __prompt()

    return prompt
    

if __name__ == "__main__":
    typer.run(main)