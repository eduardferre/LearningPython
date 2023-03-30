import openai
import typer
import config

from rich import print
from rich.table import Table

def main():
    openai.api_key = config.api_key

    print("[bold green]DALL·E API with Python[/bold green]")

    table = Table("Command", "Description")
    table.add_row("exit", "Exit from application")

    while True:
        content = __prompt()
        num = typer.prompt("\nNumber of images to generate... ")

        response = openai.Image.create(
        prompt = content,
        n = int(num),
        size="1024x1024"
        )

        image_url = response['data']
        
        for url in image_url:
            print(f"[bold green]> [/bold green][green]{url['url']}[/green]")

def __prompt() -> str:
    prompt = typer.prompt("\nImage prompt to generate... ")

    if prompt == "exit":
        exit = typer.confirm("Are you sure?")
        if exit:
            print("Bye bye")
            raise typer.Abort()
        
        return __prompt()

    return prompt

if __name__ == "__main__":
    typer.run(main)